from datetime import date as _date, timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомная модель пользователя: вход по номеру телефона."""

    phone = models.CharField('Телефон', max_length=20, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username or self.phone


# Простая шкала уровней (XP, начиная с которого открывается уровень)
LEVEL_THRESHOLDS = [0, 100, 250, 450, 700, 1000, 1400, 1900, 2500, 3200]


class UserProfile(models.Model):
    """Профиль: XP, уровень, серия посещений, аватар."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    xp = models.PositiveIntegerField('Опыт (XP)', default=0)
    level = models.PositiveIntegerField('Уровень', default=1)
    streak = models.PositiveIntegerField('Серия посещений', default=0)
    last_visit_date = models.DateField('Последний визит', null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField('О себе', blank=True)

    def __str__(self):
        return f'Профиль {self.user}'

    def add_xp(self, amount: int):
        self.xp += amount
        self._recalculate_level()
        self.save(update_fields=['xp', 'level'])

    def _recalculate_level(self):
        level = 1
        for i, threshold in enumerate(LEVEL_THRESHOLDS):
            if self.xp >= threshold:
                level = i + 1
        self.level = level

    def register_visit(self, visit_date=None):
        """Обновляет серию посещений (стрик) при заходе пользователя."""
        visit_date = visit_date or _date.today()
        if self.last_visit_date == visit_date:
            return
        if self.last_visit_date == visit_date - timedelta(days=1):
            self.streak += 1
        else:
            self.streak = 1
        self.last_visit_date = visit_date
        self.save(update_fields=['streak', 'last_visit_date'])


class Achievement(models.Model):
    """Справочник достижений."""

    code = models.SlugField('Код', unique=True)
    title = models.CharField('Название', max_length=100)
    description = models.CharField('Описание', max_length=255)
    icon = models.CharField('Иконка (emoji/класс)', max_length=50, blank=True)

    def __str__(self):
        return self.title


class UserAchievement(models.Model):
    """Полученные пользователем достижения."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, related_name='earned_by')
    earned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'achievement')
        ordering = ['-earned_at']

    def __str__(self):
        return f'{self.user} — {self.achievement}'
