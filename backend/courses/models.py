from django.conf import settings
from django.db import models


class ProgrammingLanguage(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    slug = models.SlugField('URL', unique=True)
    description = models.TextField('Описание', blank=True)
    icon = models.CharField('Иконка (emoji/класс)', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'
        ordering = ['name']

    def __str__(self):
        return self.name


class Course(models.Model):
    # Исходные 4 уровня — используются существующими курсами (сейчас: JavaScript).
    LEVEL_BEGINNER = 'beginner'
    LEVEL_BASIC = 'basic'
    LEVEL_INTERMEDIATE = 'intermediate'
    LEVEL_ADVANCED = 'advanced'
    # Дополнительные ступени Python и отдельные карточки для блоков 4 и 5.
    LEVEL_ELEMENTARY = 'elementary'
    LEVEL_UPPER_INTERMEDIATE = 'upper_intermediate'
    LEVEL_MIDDLE = 'middle'
    LEVEL_BLOCK_04 = 'block_04'
    LEVEL_BLOCK_05 = 'block_05'
    LEVEL_CHOICES = [
        (LEVEL_BEGINNER, 'Начальный'),
        (LEVEL_BASIC, 'Базовый'),
        (LEVEL_ELEMENTARY, 'Elementary'),
        (LEVEL_INTERMEDIATE, 'Средний'),
        (LEVEL_BLOCK_04, 'Блок 4. Циклы, строки и коллекции'),
        (LEVEL_BLOCK_05, 'Блок 5. ООП и инженерная культура кода'),
        (LEVEL_UPPER_INTERMEDIATE, 'Upper-Intermediate'),
        (LEVEL_ADVANCED, 'Продвинутый'),
        (LEVEL_MIDDLE, 'Middle Developer'),
    ]

    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE, related_name='courses')
    level = models.CharField('Уровень сложности', max_length=20, choices=LEVEL_CHOICES)
    title = models.CharField('Название курса', max_length=150)
    description = models.TextField('Описание', blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['language', 'order']
        unique_together = ('language', 'level')

    def __str__(self):
        return f'{self.language} — {self.get_level_display()}'

    def progress_percent(self, user):
        """Процент пройденных уроков курса для конкретного пользователя."""
        total = self.lessons.count()
        if not total or not user or not user.is_authenticated:
            return 0
        completed = UserProgress.objects.filter(
            user=user, lesson__course=self, completed=True
        ).count()
        return round(completed * 100 / total)

    def is_completed_by(self, user):
        return self.lessons.exists() and self.progress_percent(user) == 100


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField('Заголовок', max_length=150)
    # Название тематического блока внутри курса (например, «Блок 7. Функции»).
    # Уроки с одинаковым block_title, идущие подряд по order, визуально группируются
    # на странице курса. Пустая строка (у старого контента без блоков) группировки не создаёт —
    # уроки просто отображаются одним списком, как раньше.
    block_title = models.CharField('Блок / тема', max_length=150, blank=True)
    theory = models.TextField('Теория', blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    xp_reward = models.PositiveIntegerField('Награда XP', default=10)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['course', 'order']

    def __str__(self):
        return self.title

    def solved_task_ids(self, user):
        """ID заданий урока, которые пользователь уже решил верно."""
        if not user or not user.is_authenticated:
            return set()
        return set(
            TaskAttempt.objects.filter(user=user, task__lesson=self, is_correct=True)
            .values_list('task_id', flat=True)
        )

    def all_tasks_solved_by(self, user):
        task_ids = set(self.tasks.values_list('id', flat=True))
        if not task_ids:
            return True
        return task_ids.issubset(self.solved_task_ids(user))


class CodeExample(models.Model):
    """Пример кода внутри урока. У одного урока может быть несколько примеров."""

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='code_examples')
    title = models.CharField('Заголовок примера', max_length=150, blank=True)
    code = models.TextField('Код')
    explanation = models.TextField('Пояснение к примеру', blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Пример кода'
        verbose_name_plural = 'Примеры кода'
        ordering = ['lesson', 'order']

    def __str__(self):
        return self.title or f'Пример к «{self.lesson}»'


class Task(models.Model):
    TYPE_TEST = 'test'
    TYPE_PRACTICE = 'practice'
    TASK_TYPES = [
        (TYPE_TEST, 'Тест'),
        (TYPE_PRACTICE, 'Практическое задание'),
    ]

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='tasks')
    task_type = models.CharField('Тип', max_length=20, choices=TASK_TYPES, default=TYPE_PRACTICE)
    question = models.TextField('Вопрос / задание')
    hint = models.CharField('Подсказка', max_length=255, blank=True)
    correct_answer = models.TextField('Правильный ответ', help_text='Ожидаемый ответ или ключевые слова')
    xp_reward = models.PositiveIntegerField('Награда XP', default=5)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['lesson', 'order']

    def __str__(self):
        return f'{self.lesson} — {self.question[:40]}'


class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='user_progress')
    completed = models.BooleanField('Пройден', default=False)
    completed_at = models.DateTimeField('Дата завершения', null=True, blank=True)

    class Meta:
        verbose_name = 'Прогресс пользователя'
        verbose_name_plural = 'Прогресс пользователей'
        unique_together = ('user', 'lesson')

    def __str__(self):
        return f'{self.user} — {self.lesson} ({"пройден" if self.completed else "в процессе"})'


class TaskAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='task_attempts')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attempts')
    submitted_answer = models.TextField('Ответ пользователя', blank=True)
    is_correct = models.BooleanField('Верно', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Попытка выполнения задания'
        verbose_name_plural = 'Попытки выполнения заданий'
        ordering = ['-created_at']
