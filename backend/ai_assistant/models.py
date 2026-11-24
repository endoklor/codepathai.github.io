from django.conf import settings
from django.db import models


class AIInteractionLog(models.Model):
    """История обращений к Grok API. Полная реализация — Этап 5 дорожной карты."""

    MODE_THEORY = 'theory'
    MODE_DEBUG = 'debug'
    MODE_EXPLAIN = 'explain'
    MODE_RECOMMEND = 'recommend'
    MODE_CHOICES = [
        (MODE_THEORY, 'Вопрос по теории'),
        (MODE_DEBUG, 'Разбор кода с ошибками'),
        (MODE_EXPLAIN, 'Объяснить код'),
        (MODE_RECOMMEND, 'Персональные рекомендации'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ai_logs')
    lesson = models.ForeignKey('courses.Lesson', on_delete=models.SET_NULL, null=True, blank=True)
    mode = models.CharField('Режим', max_length=20, choices=MODE_CHOICES, default=MODE_THEORY)
    prompt = models.TextField('Запрос пользователя')
    response = models.TextField('Ответ AI', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Обращение к AI'
        verbose_name_plural = 'Обращения к AI'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user} [{self.get_mode_display()}] {self.created_at:%d.%m.%Y %H:%M}'
