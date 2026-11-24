from datetime import timedelta

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import redirect, render
from django.utils import timezone

from courses.models import TaskAttempt, UserProgress
from .forms import ProfileEditForm, RegisterForm
from .models import LEVEL_THRESHOLDS


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=profile, user=request.user)

    achievements = request.user.achievements.select_related('achievement')
    completed_lessons = UserProgress.objects.filter(user=request.user, completed=True).count()

    # Реальные завершённые уроки и попытки заданий за последние 90 дней.
    today = timezone.localdate()
    start = today - timedelta(days=89)
    counts = {}
    for row in UserProgress.objects.filter(
        user=request.user, completed=True, completed_at__date__gte=start,
    ).annotate(day=TruncDate('completed_at')).values('day').annotate(total=Count('id')):
        if row['day']:
            counts[row['day']] = counts.get(row['day'], 0) + row['total']
    for row in TaskAttempt.objects.filter(
        user=request.user, created_at__date__gte=start,
    ).annotate(day=TruncDate('created_at')).values('day').annotate(total=Count('id')):
        if row['day']:
            counts[row['day']] = counts.get(row['day'], 0) + row['total']
    heatmap_days = []
    for offset in range(89, -1, -1):
        day = today - timedelta(days=offset)
        count = counts.get(day, 0)
        heatmap_days.append({'date': day, 'count': count, 'level': min(4, count)})
    next_threshold = next((threshold for threshold in LEVEL_THRESHOLDS if threshold > profile.xp), None)
    current_threshold = max((threshold for threshold in LEVEL_THRESHOLDS if threshold <= profile.xp), default=0)
    xp_to_next_level = next_threshold - current_threshold if next_threshold else 0
    xp_in_level = profile.xp - current_threshold if next_threshold else 0
    level_progress = round(xp_in_level * 100 / xp_to_next_level) if xp_to_next_level else 100

    return render(request, 'users/profile.html', {
        'profile': profile,
        'form': form,
        'achievements': achievements,
        'completed_lessons': completed_lessons,
        'heatmap_days': heatmap_days,
        'active_days': sum(bool(day['count']) for day in heatmap_days),
        'level_progress': level_progress,
        'xp_in_level': xp_in_level,
        'xp_to_next_level': xp_to_next_level,
    })
