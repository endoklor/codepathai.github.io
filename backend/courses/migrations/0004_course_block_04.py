from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_lesson_block_title_alter_course_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(
                choices=[
                    ('beginner', 'Начальный'),
                    ('basic', 'Базовый'),
                    ('elementary', 'Elementary'),
                    ('intermediate', 'Средний'),
                    ('block_04', 'Блок 4. Циклы, строки и коллекции'),
                    ('upper_intermediate', 'Upper-Intermediate'),
                    ('advanced', 'Продвинутый'),
                    ('middle', 'Middle Developer'),
                ],
                max_length=20,
                verbose_name='Уровень сложности',
            ),
        ),
    ]
