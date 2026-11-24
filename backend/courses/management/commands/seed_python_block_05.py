import json

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from courses.data.python_curriculum.block_05_oop import BLOCK
from courses.models import CodeExample, Course, Lesson, ProgrammingLanguage, Task
from courses.task_utils import CODE_OPTIONS_PREFIX, is_code_task as is_code_answer


class Command(BaseCommand):
    help = 'Добавляет или обновляет Блок 5 курса Python, сохраняя другие блоки и прогресс.'

    @transaction.atomic
    def handle(self, *args, **options):
        try:
            language = ProgrammingLanguage.objects.get(slug='python')
        except ProgrammingLanguage.DoesNotExist as error:
            raise CommandError('Сначала создайте курс Python командой seed_python_course.') from error

        level_order = [
            Course.LEVEL_BEGINNER,
            Course.LEVEL_ELEMENTARY,
            Course.LEVEL_INTERMEDIATE,
            Course.LEVEL_BLOCK_04,
            Course.LEVEL_BLOCK_05,
        ]
        Course.objects.filter(language=language, lessons__isnull=True).delete()
        for order, level in enumerate(level_order, start=1):
            Course.objects.filter(language=language, level=level).update(order=order)

        course, created = Course.objects.update_or_create(
            language=language,
            level=BLOCK['level'],
            defaults={
                'title': 'Python: Блок 5. ООП и инженерная культура кода',
                'description': (
                    'ООП и инженерная культура кода: классы, тестирование, '
                    'командная строка и итоговый проект.'
                ),
                'order': level_order.index(BLOCK['level']) + 1,
            },
        )

        example_count = 0
        task_count = 0
        for lesson_order, lesson_data in enumerate(BLOCK['lessons'], start=1):
            lesson, _ = Lesson.objects.update_or_create(
                course=course,
                order=lesson_order,
                defaults={
                    'title': lesson_data['title'],
                    'block_title': BLOCK['block_title'],
                    'theory': lesson_data['theory'],
                    'xp_reward': lesson_data.get('xp_reward', 10),
                },
            )

            for example_order, example in enumerate(lesson_data.get('examples', []), start=1):
                CodeExample.objects.update_or_create(
                    lesson=lesson,
                    order=example_order,
                    defaults={
                        'title': example.get('title', ''),
                        'code': example['code'],
                        'explanation': example.get('explanation', ''),
                    },
                )
                example_count += 1

            for task_order, task_data in enumerate(lesson_data.get('tasks', []), start=1):
                answer = task_data['answer']
                is_code_task = isinstance(answer, list) or is_code_answer(
                    task_data['question'], answer
                )
                Task.objects.update_or_create(
                    lesson=lesson,
                    order=task_order,
                    defaults={
                        'task_type': Task.TYPE_PRACTICE if is_code_task else Task.TYPE_TEST,
                        'question': task_data['question'],
                        'hint': task_data.get('hint', ''),
                        'correct_answer': (
                            CODE_OPTIONS_PREFIX + json.dumps(answer, ensure_ascii=False)
                            if is_code_task else answer
                        ),
                        'xp_reward': task_data.get('xp_reward', 5),
                    },
                )
                task_count += 1

        stale_lessons = Lesson.objects.filter(course=course).exclude(
            order__range=(1, len(BLOCK['lessons']))
        ).count()
        if stale_lessons:
            self.stdout.write(self.style.WARNING(
                f'Оставлены без изменений {stale_lessons} урока вне диапазона нового плана.'
            ))

        action = 'создан' if created else 'обновлён'
        self.stdout.write(self.style.SUCCESS(
            f'Блок 5 {action}: {len(BLOCK["lessons"])} урока, '
            f'{example_count} примеров и {task_count} заданий. Прогресс пользователя сохранён.'
        ))
