import json

from django.core.management.base import BaseCommand
from django.db import transaction

from courses.data.python_curriculum import get_blocks
from courses.models import CodeExample, Course, Lesson, ProgrammingLanguage, Task
from courses.task_utils import CODE_OPTIONS_PREFIX, is_code_task as is_code_answer

# Уровни курса Python и отдельная карточка для каждого блока, доступного сейчас.
LEVEL_ORDER = [
    Course.LEVEL_BEGINNER,
    Course.LEVEL_ELEMENTARY,
    Course.LEVEL_INTERMEDIATE,
    Course.LEVEL_BLOCK_04,
    Course.LEVEL_BLOCK_05,
]

LEVEL_TITLES = {
    Course.LEVEL_BEGINNER: 'Beginner',
    Course.LEVEL_ELEMENTARY: 'Elementary',
    Course.LEVEL_INTERMEDIATE: 'Intermediate',
    Course.LEVEL_BLOCK_04: 'Блок 4. Циклы, строки и коллекции',
    Course.LEVEL_BLOCK_05: 'Блок 5. ООП и инженерная культура кода',
}

LEVEL_DESCRIPTIONS = {
    Course.LEVEL_BEGINNER: 'С абсолютного нуля: программа, интерпретатор, переменные, типы, условия, циклы.',
    Course.LEVEL_ELEMENTARY: 'Строки, списки, кортежи, множества и словари — рабочие инструменты каждого скрипта.',
    Course.LEVEL_INTERMEDIATE: 'Функции, comprehensions, модули и пакеты, файлы, исключения.',
    Course.LEVEL_BLOCK_04: 'Циклы, строки и коллекции: от отдельных команд до программ и проекта.',
    Course.LEVEL_BLOCK_05: 'ООП и инженерная культура кода: классы, тестирование, инструменты и проект.',
}

class Command(BaseCommand):
    help = (
        'Пересоздаёт курсы Python из данных '
        'courses/data/python_curriculum/. Полностью заменяет предыдущие курсы Python (включая '
        'старый короткий демо-курс), чтобы не было дублей. JavaScript и другие языки не трогает.'
    )

    @transaction.atomic
    def handle(self, *args, **options):
        language, _ = ProgrammingLanguage.objects.get_or_create(
            slug='python',
            defaults={
                'name': 'Python',
                'icon': '🐍',
                'description': 'От абсолютного нуля до уровня Middle Python Developer.',
            },
        )

        # Удаляем ВСЕ существующие курсы Python (в т.ч. старый демо-контент на 4 уровнях) —
        # каскадно удалятся их Lesson/CodeExample/Task/UserProgress/TaskAttempt по этому языку.
        # Прогресс пользователей по JavaScript и другим языкам не затрагивается.
        deleted, _ = Course.objects.filter(language=language).delete()
        if deleted:
            self.stdout.write(self.style.WARNING(
                'Удалены предыдущие курсы Python (включая прогресс пользователей по ним).'
            ))

        # Создаём курс для каждого уровня и блока — даже когда контента пока нет.
        # Так все заполненные блоки видны на странице языка.
        courses_by_level = {}
        for order, level in enumerate(LEVEL_ORDER, start=1):
            courses_by_level[level] = Course.objects.create(
                language=language,
                level=level,
                title=f'Python: {LEVEL_TITLES[level]}',
                description=LEVEL_DESCRIPTIONS[level],
                order=order,
            )

        blocks = get_blocks()
        if not blocks:
            self.stdout.write(self.style.WARNING(
                'Блоков с контентом пока нет (courses/data/python_curriculum/BLOCK_MODULES пуст) — '
                'созданы только пустые курсы-уровни. Контент добавляется постепенно, блок за блоком.'
            ))

        lesson_count = 0
        example_count = 0
        task_count = 0

        # order урока должен расти сквозно внутри одного курса (не сбрасываться в каждом блоке) —
        # от этого зависит существующая логика последовательной разблокировки в courses/views.py
        # (previous_lesson ищется как lesson с order на 1 меньше в пределах того же Course).
        next_order_by_level = {level: 0 for level in LEVEL_ORDER}

        for block in blocks:
            level = block['level']
            course = courses_by_level[level]
            for lesson_data in block['lessons']:
                next_order_by_level[level] += 1
                lesson = Lesson.objects.create(
                    course=course,
                    title=lesson_data['title'],
                    block_title=block['block_title'],
                    theory=lesson_data['theory'],
                    order=next_order_by_level[level],
                    xp_reward=lesson_data.get('xp_reward', 10),
                )
                lesson_count += 1

                for ex_order, example in enumerate(lesson_data.get('examples', []), start=1):
                    CodeExample.objects.create(
                        lesson=lesson,
                        title=example.get('title', ''),
                        code=example['code'],
                        explanation=example.get('explanation', ''),
                        order=ex_order,
                    )
                    example_count += 1

                for task_order, task in enumerate(lesson_data.get('tasks', []), start=1):
                    answer = task['answer']
                    is_code_task = isinstance(answer, list) or is_code_answer(
                        task['question'],
                        answer,
                    )
                    Task.objects.create(
                        lesson=lesson,
                        task_type=Task.TYPE_PRACTICE if is_code_task else Task.TYPE_TEST,
                        question=task['question'],
                        hint=task.get('hint', ''),
                        correct_answer=(
                            CODE_OPTIONS_PREFIX + json.dumps(answer, ensure_ascii=False)
                            if is_code_task else answer
                        ),
                        xp_reward=task.get('xp_reward', 5),
                        order=task_order,
                    )
                    task_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Курс Python пересоздан: {len(LEVEL_ORDER)} уровней, {lesson_count} уроков, '
            f'{example_count} примеров кода, {task_count} заданий.'
        ))
