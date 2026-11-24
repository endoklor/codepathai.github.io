from collections import Counter
from datetime import timedelta
from hashlib import sha256

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.db.models.functions import TruncDate

from .models import Course, Lesson, ProgrammingLanguage, Task, TaskAttempt, UserProgress
from .task_utils import is_code_task, task_answer_is_correct


def _course_lesson_number_offset(course):
    """Количество уроков в предыдущих уровнях этого языка для сквозной нумерации."""
    return Lesson.objects.filter(
        course__language_id=course.language_id,
        course__order__lt=course.order,
    ).count()


def _previous_populated_course(course):
    return Course.objects.filter(
        language_id=course.language_id,
        order__lt=course.order,
        lessons__isnull=False,
    ).order_by('-order').first()


def _activity_heatmap(user, days=84):
    """Return real lesson/task activity, grouped into calendar days."""
    today = timezone.localdate()
    start = today - timedelta(days=days - 1)
    counts = Counter()
    completed_days = (
        UserProgress.objects.filter(
            user=user, completed=True, completed_at__date__gte=start,
        )
        .annotate(activity_day=TruncDate('completed_at'))
        .values('activity_day')
        .annotate(total=Count('id'))
    )
    attempt_days = (
        TaskAttempt.objects.filter(user=user, created_at__date__gte=start)
        .annotate(activity_day=TruncDate('created_at'))
        .values('activity_day')
        .annotate(total=Count('id'))
    )
    for row in completed_days:
        if row['activity_day']:
            counts[row['activity_day']] += row['total']
    for row in attempt_days:
        if row['activity_day']:
            counts[row['activity_day']] += row['total']

    cells = []
    for offset in range(days - 1, -1, -1):
        day = today - timedelta(days=offset)
        count = counts[day]
        cells.append({'date': day, 'count': count, 'level': min(4, count)})
    return cells, sum(bool(cell['count']) for cell in cells)


def _daily_challenge_task(user):
    """Choose a stable task from Python lessons the learner can currently reach."""
    tasks = Task.objects.filter(lesson__course__language__slug='python').order_by('id')
    if not (user.is_staff or user.is_superuser):
        completed_ids = UserProgress.objects.filter(
            user=user, completed=True,
        ).values_list('lesson_id', flat=True)
        current_lesson = (
            Lesson.objects.filter(course__language__slug='python')
            .exclude(id__in=completed_ids)
            .select_related('course')
            .order_by('course__order', 'order')
            .first()
        )
        if current_lesson:
            tasks = tasks.filter(
                Q(lesson__course__order__lt=current_lesson.course.order)
                | Q(
                    lesson__course__order=current_lesson.course.order,
                    lesson__order__lte=current_lesson.order,
                )
            )
    count = tasks.count()
    if not count:
        return None
    day = f'{user.pk}:{timezone.localdate().isoformat()}'
    index = int(sha256(day.encode('utf-8')).hexdigest(), 16) % count
    return tasks.select_related('lesson', 'lesson__course').all()[index]


@login_required
def home_view(request):
    """Главная страница (Dashboard): прогресс, серия, уровень, последние уроки."""
    profile = request.user.profile
    profile.register_visit()

    languages = ProgrammingLanguage.objects.all()
    language_rows = []
    for language in languages:
        courses = list(language.courses.filter(lessons__isnull=False).distinct())
        if courses:
            avg_progress = round(sum(c.progress_percent(request.user) for c in courses) / len(courses))
        else:
            avg_progress = 0
        language_rows.append({'language': language, 'progress': avg_progress, 'has_courses': bool(courses)})

    python_courses = list(
        Course.objects.filter(language__slug='python', lessons__isnull=False)
        .select_related('language')
        .distinct()
        .order_by('order')
    )
    python_course_rows = [
        {'course': course, 'progress': course.progress_percent(request.user)}
        for course in python_courses
    ]
    completed_lesson_ids = UserProgress.objects.filter(
        user=request.user, completed=True
    ).values_list('lesson_id', flat=True)
    continue_lesson = (
        Lesson.objects.filter(course__language__slug='python')
        .exclude(id__in=completed_lesson_ids)
        .select_related('course', 'course__language')
        .order_by('course__order', 'order')
        .first()
    )
    continue_lesson_number = (
        _course_lesson_number_offset(continue_lesson.course) + continue_lesson.order
        if continue_lesson else None
    )
    continue_course_progress = (
        continue_lesson.course.progress_percent(request.user) if continue_lesson else 0
    )
    lesson_preview = None
    if continue_lesson:
        lesson_preview = {
            'id': continue_lesson.id,
            'number': continue_lesson_number,
            'title': continue_lesson.title,
            'language': continue_lesson.course.language.name,
            'level': continue_lesson.course.get_level_display(),
            'theory': continue_lesson.theory,
            'examples': list(continue_lesson.code_examples.values('title', 'code', 'explanation')),
            'tasks': list(continue_lesson.tasks.values('question', 'hint')),
            'courseUrl': reverse('course_detail', args=[continue_lesson.course_id]),
            'lessonUrl': reverse('lesson_detail', args=[continue_lesson.id]),
        }
    completed_lessons = UserProgress.objects.filter(
        user=request.user, completed=True
    ).count()

    recent_progress = (
        UserProgress.objects.filter(user=request.user, completed=True)
        .select_related('lesson', 'lesson__course', 'lesson__course__language')
        .order_by('-completed_at')[:5]
    )
    heatmap_days, active_days = _activity_heatmap(request.user)
    daily_challenge = _daily_challenge_task(request.user)
    if daily_challenge:
        daily_challenge.is_code_task = is_code_task(
            daily_challenge.question,
            daily_challenge.correct_answer,
            daily_challenge.task_type,
        )
    daily_challenge_solved = (
        request.session.get(f'daily_challenge_{request.user.pk}') == timezone.localdate().isoformat()
    )
    return render(request, 'courses/home.html', {
        'profile': profile,
        'language_rows': language_rows,
        'python_course_rows': python_course_rows,
        'continue_lesson': continue_lesson,
        'lesson_preview': lesson_preview,
        'continue_lesson_number': continue_lesson_number,
        'continue_course_progress': continue_course_progress,
        'completed_lessons': completed_lessons,
        'recent_progress': recent_progress,
        'heatmap_days': heatmap_days,
        'active_days': active_days,
        'daily_challenge': daily_challenge,
        'daily_challenge_solved': daily_challenge_solved,
    })


@login_required
def submit_daily_challenge_view(request):
    if request.method != 'POST':
        return redirect('home')

    task = _daily_challenge_task(request.user)
    if not task or str(request.POST.get('task_id')) != str(task.id):
        messages.error(request, 'Ежедневное задание уже обновилось. Обновите страницу и попробуйте снова.')
        return redirect('home')

    today = timezone.localdate().isoformat()
    session_key = f'daily_challenge_{request.user.pk}'
    if request.session.get(session_key) == today:
        messages.info(request, 'Задание дня уже решено. Возвращайтесь за новым завтра!')
        return redirect('home')

    answer = request.POST.get('answer', '').strip()
    if not answer:
        messages.error(request, 'Введите ответ перед отправкой.')
        return redirect('home')

    if task_answer_is_correct(task, answer):
        request.user.profile.add_xp(50)
        request.session[session_key] = today
        messages.success(request, 'Верно! Начислено +50 XP за задание дня.')
    else:
        messages.error(request, 'Ответ пока неверный. Попробуйте ещё раз.')
    return redirect('home')


def language_list_view(request):
    languages = list(ProgrammingLanguage.objects.annotate(
        course_count=Count(
            'courses',
            filter=Q(courses__lessons__isnull=False),
            distinct=True,
        )
    ))
    for language in languages:
        courses = list(
            language.courses.filter(lessons__isnull=False)
            .distinct().prefetch_related('lessons').order_by('order')
        )
        language.catalog_courses = courses
        language.has_beginner_course = any(course.level == Course.LEVEL_BEGINNER for course in courses)
        language.search_text = ' '.join(
            [language.name, language.description]
            + [f'{course.title} {course.get_level_display()} {course.description}' for course in courses]
            + [lesson.title for course in courses for lesson in course.lessons.all()]
        )
    return render(request, 'courses/language_list.html', {'languages': languages})


def language_detail_view(request, slug):
    language = get_object_or_404(ProgrammingLanguage, slug=slug)
    courses = language.courses.filter(lessons__isnull=False).distinct()
    course_rows = [
        {'course': course, 'progress': course.progress_percent(request.user)}
        for course in courses
    ]
    return render(request, 'courses/language_detail.html', {
        'language': language,
        'course_rows': course_rows,
    })


@login_required
def course_detail_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = list(course.lessons.all())
    is_admin = request.user.is_staff or request.user.is_superuser
    number_offset = _course_lesson_number_offset(course)

    completed_ids = set(
        UserProgress.objects.filter(user=request.user, lesson__course=course, completed=True)
        .values_list('lesson_id', flat=True)
    )

    # Уроки открываются последовательно: первый доступен сразу,
    # каждый следующий — после прохождения предыдущего.
    lesson_rows = []
    unlocked = True
    if course.level in {Course.LEVEL_BLOCK_04, Course.LEVEL_BLOCK_05} and not is_admin:
        previous_course = _previous_populated_course(course)
        unlocked = not previous_course or previous_course.is_completed_by(request.user)
    for number, lesson in enumerate(lessons, start=1):
        is_completed = lesson.id in completed_ids
        lesson_rows.append({
            'lesson': lesson,
            'number': number_offset + number,
            'completed': is_completed,
            'unlocked': is_admin or unlocked,
        })
        unlocked = unlocked and is_completed

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'lesson_rows': lesson_rows,
        'progress_percent': course.progress_percent(request.user),
    })


@login_required
def lesson_detail_view(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    course = lesson.course
    is_admin = request.user.is_staff or request.user.is_superuser
    lesson_number = _course_lesson_number_offset(course) + lesson.order

    if not is_admin and course.level in {Course.LEVEL_BLOCK_04, Course.LEVEL_BLOCK_05}:
        previous_course = _previous_populated_course(course)
        if previous_course and not previous_course.is_completed_by(request.user):
            messages.error(request, 'Сначала пройдите предыдущий блок курса.')
            return redirect('course_detail', course_id=course.id)

    # Проверяем, что предыдущий урок курса пройден (последовательное открытие уроков)
    previous_lesson = course.lessons.filter(order__lt=lesson.order).order_by('-order').first()
    if not is_admin and previous_lesson and not UserProgress.objects.filter(
        user=request.user, lesson=previous_lesson, completed=True
    ).exists():
        messages.error(request, 'Сначала пройдите предыдущий урок этого курса.')
        return redirect('course_detail', course_id=course.id)

    tasks = lesson.tasks.all()
    for task in tasks:
        task.is_code_task = is_code_task(
            task.question,
            task.correct_answer,
            task.task_type,
        )
    code_examples = lesson.code_examples.all()
    progress, _ = UserProgress.objects.get_or_create(user=request.user, lesson=lesson)

    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        answer = request.POST.get('answer', '').strip()
        task = get_object_or_404(Task, id=task_id, lesson=lesson)
        is_correct = task_answer_is_correct(task, answer)
        TaskAttempt.objects.create(user=request.user, task=task, submitted_answer=answer, is_correct=is_correct)
        if is_correct:
            request.user.profile.add_xp(task.xp_reward)
            messages.success(request, f'Верно! +{task.xp_reward} XP')
        else:
            messages.error(request, 'Не совсем так — попробуй ещё раз или спроси AI-помощника.')
        return redirect('lesson_detail', lesson_id=lesson.id)

    solved_ids = lesson.solved_task_ids(request.user)
    can_complete = lesson.all_tasks_solved_by(request.user)

    return render(request, 'courses/lesson_detail.html', {
        'lesson': lesson,
        'lesson_number': lesson_number,
        'tasks': tasks,
        'code_examples': code_examples,
        'solved_ids': solved_ids,
        'progress': progress,
        'can_complete': can_complete,
    })


@login_required
def complete_lesson_view(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    course = lesson.course
    is_admin = request.user.is_staff or request.user.is_superuser
    if not is_admin and course.level in {Course.LEVEL_BLOCK_04, Course.LEVEL_BLOCK_05}:
        previous_course = _previous_populated_course(course)
        if previous_course and not previous_course.is_completed_by(request.user):
            messages.error(request, 'Сначала пройдите предыдущий блок курса.')
            return redirect('course_detail', course_id=course.id)
    progress, _ = UserProgress.objects.get_or_create(user=request.user, lesson=lesson)

    if progress.completed:
        return redirect('course_detail', course_id=lesson.course_id)

    if not lesson.all_tasks_solved_by(request.user):
        messages.error(request, 'Сначала правильно реши все задания урока.')
        return redirect('lesson_detail', lesson_id=lesson.id)

    progress.completed = True
    progress.completed_at = timezone.now()
    progress.save()
    request.user.profile.add_xp(lesson.xp_reward)
    messages.success(request, f'Урок пройден! +{lesson.xp_reward} XP')

    if course.is_completed_by(request.user):
        messages.success(request, f'Курс «{course}» полностью завершён! 🎉')

    return redirect('course_detail', course_id=course.id)
