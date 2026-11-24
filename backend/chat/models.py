from django.conf import settings
from django.db import models


class ChatMessage(models.Model):
    """Сообщение общего чата. Полная реализация — Этап 4 дорожной карты."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField('Текст', max_length=1000)
    created_at = models.DateTimeField('Отправлено', auto_now_add=True)
    is_deleted = models.BooleanField('Удалено', default=False)

    class Meta:
        verbose_name = 'Сообщение чата'
        verbose_name_plural = 'Сообщения чата'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.user}: {self.text[:30]}'
