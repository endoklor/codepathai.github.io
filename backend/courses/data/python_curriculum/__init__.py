"""
Данные полного курса Python для CodePath AI (Beginner -> Middle Developer).

Курс организован как последовательность тематических БЛОКОВ (из ТЗ: «Блок 1. Основы
программирования и Python», «Блок 12. ООП» и т.д.). Каждый блок относится к одному
из своей ступени courses.models.Course.LEVEL_* и содержит список уроков блока.

Формат одного блока (то, что должна содержать переменная BLOCK в файле block_XX_*.py):

    from courses.models import Course

    BLOCK = {
        'level': Course.LEVEL_BEGINNER,       # ступень курса Python для этого блока
        'block_title': 'Блок 1. Основы программирования и Python',
        'lessons': [
            {
                'title': 'Что такое программа и как её запускает компьютер',
                'theory': (
                    'Первый абзац...\n\n'
                    'Второй абзац...\n\n'
                    'Третий абзац (типичные ошибки/нюансы)...'
                ),
                'examples': [
                    {'title': '...', 'code': '...', 'explanation': '...'},
                    {'title': '...', 'code': '...', 'explanation': '...'},
                ],
                'tasks': [
                    {'question': '...', 'hint': '...', 'answer': '...'},
                    {'question': '...', 'hint': '...', 'answer': '...'},
                    {'question': '...', 'hint': '...', 'answer': '...'},
                ],
                # необязательно: 'xp_reward': 10,
            },
            ...
        ],
    }

Почему так, а не один большой файл:
  - можно добавлять/править один блок, не трогая остальные (точечные правки);
  - файлы не разрастаются до тысяч строк;
  - легко ревьюить diff по конкретной теме («добавь уроки по функциям» = правка
    одного файла block_07_functions.py, а не всего курса).

Порядок блоков в итоговом курсе задаётся порядком элементов в списке BLOCK_MODULES
ниже — именно он, а не имя файла, определяет порядок уроков внутри каждого уровня.
Уроки внутри уровня нумеруются сквозно (order растёт через все блоки этого уровня),
это важно для существующей логики последовательной разблокировки уроков
(courses/views.py опирается на возрастающий Lesson.order внутри одного Course).

Контент добавляется постепенно, блок за блоком, начиная с Beginner. Если список
BLOCK_MODULES пуст, seed_python_course создаёт только пустые курсы-уровни.
"""

import importlib

BLOCK_MODULES = [
    'block_01_basics',
    'block_02_conditions',
    'block_03_intermediate',
    'block_04_loops_collections',
    'block_05_oop',
]


def get_blocks():
    """Возвращает список блоков в порядке BLOCK_MODULES, импортируя каждый модуль лениво."""
    blocks = []
    for module_name in BLOCK_MODULES:
        module = importlib.import_module(f'.{module_name}', package=__name__)
        blocks.append(module.BLOCK)
    return blocks
