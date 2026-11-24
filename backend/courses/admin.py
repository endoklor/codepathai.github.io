from django.contrib import admin

from .models import CodeExample, Course, Lesson, ProgrammingLanguage, Task, TaskAttempt, UserProgress


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


class CourseInline(admin.TabularInline):
    model = Course
    extra = 1


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CourseInline]


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


class CodeExampleInline(admin.StackedInline):
    model = CodeExample
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'level', 'order')
    list_filter = ('language', 'level')
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'block_title', 'course', 'order', 'xp_reward')
    list_filter = ('course__language', 'course__level', 'block_title')
    inlines = [CodeExampleInline, TaskInline]


@admin.register(CodeExample)
class CodeExampleAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'title', 'order')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'task_type', 'xp_reward', 'order')
    list_filter = ('task_type',)


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'completed', 'completed_at')
    list_filter = ('completed',)


@admin.register(TaskAttempt)
class TaskAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'is_correct', 'created_at')
    list_filter = ('is_correct',)
