from django.urls import path

from . import views

urlpatterns = [
    path('languages/', views.language_list_view, name='language_list'),
    path('languages/<slug:slug>/', views.language_detail_view, name='language_detail'),
    path('courses/<int:course_id>/', views.course_detail_view, name='course_detail'),
    path('lessons/<int:lesson_id>/', views.lesson_detail_view, name='lesson_detail'),
    path('lessons/<int:lesson_id>/complete/', views.complete_lesson_view, name='complete_lesson'),
    path('daily-challenge/submit/', views.submit_daily_challenge_view, name='daily_challenge_submit'),
]
