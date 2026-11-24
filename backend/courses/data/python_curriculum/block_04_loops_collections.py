"""
Блок 4. Циклы, строки и коллекции. Уроки 71–102.

Уровень курса: Intermediate. Внутренний порядок в курсе — 33–64.
До урока 90 в примерах не используются словари; списки появляются в уроке 84.
Практики, тренажёры и отладка составляют 16 отдельных занятий.
"""

from courses.models import Course

LESSONS = [
    {
        "title": "for и range(): повторяем действия и накапливаем результат",
        "theory": "Цикл for берёт очередное значение из строки или range и выполняет для него тело с отступом. range(стоп) выдаёт числа от 0 до значения перед стопом; range(старт, стоп) задаёт границы, а третий аргумент — шаг. Переменная цикла по очереди получает каждое значение. Для суммы заведите накопитель до цикла, для количества — счётчик.\n\nВыбирайте for, когда число шагов или последовательность известны заранее. В цикле можно перебрать символы строки напрямую, а range удобен для чисел. Ловушка: правая граница range не включается, поэтому диапазон от 1 до N записывается как range(1, N + 1). Это частая ошибка на единицу.",
        "examples": [
            {
                "title": "Сумма от 1 до N",
                "code": "n = 5\ntotal = 0\nfor number in range(1, n + 1):\n    total += number\nprint(total)\n# Вывод: 15",
                "explanation": "Накопитель начинается с нуля, а range включает N через границу N + 1."
            },
            {
                "title": "Символы с номерами",
                "code": "word = \"код\"\nposition = 1\nfor symbol in word:\n    print(position, symbol)\n    position += 1\n# Вывод:\n# 1 к\n# 2 о\n# 3 д",
                "explanation": "Счётчик позиции увеличивается внутри цикла после вывода символа."
            }
        ],
        "tasks": [
            {
                "question": "Напишите цикл for, который выводит числа от 1 до 10.",
                "hint": "Учитывайте, что правая граница range не включается.",
                "answer": [
                    "for number in range(1, 11):\n    print(number)",
                    "for number in range(10):\n    print(number + 1)"
                ]
            },
            {
                "question": "Напишите функцию суммы чётных чисел от 1 до n.",
                "hint": "Можно проверять остаток от деления или взять шаг 2.",
                "answer": [
                    "def sum_even(n):\n    total = 0\n    for number in range(1, n + 1):\n        if number % 2 == 0:\n            total += number\n    return total",
                    "def sum_even(n):\n    total = 0\n    for number in range(2, n + 1, 2):\n        total += number\n    return total"
                ]
            },
            {
                "question": "Напишите функцию, которая считает гласные в строке text.",
                "hint": "Перебирайте символы строки и проверяйте вхождение в строку гласных.",
                "answer": [
                    "def count_vowels(text):\n    count = 0\n    for symbol in text.lower():\n        if symbol in \"аеёиоуыэюя\":\n            count += 1\n    return count",
                    "def count_vowels(text):\n    vowels = \"аеёиоуыэюя\"\n    total = 0\n    for symbol in text:\n        if symbol.lower() in vowels:\n            total += 1\n    return total"
                ]
            },
            {
                "question": "Сколько раз выполнится тело цикла for _ in range(5)?",
                "hint": "Последнее число будет на единицу меньше правой границы.",
                "answer": "5"
            }
        ]
    },
    {
        "title": "Тренажёр: «for»",
        "theory": "Решайте задачи по нарастающей. В части A отрабатывается один цикл и одна операция. В части B соединяются ввод, условие и накопитель. В части C важны два цикла и аккуратное расположение print: таблица печатается строками, а не одним длинным числом.\n\nДля каждого решения проверьте минимальный ввод, ноль и несколько обычных значений. Ловушка диапазона остаётся актуальной: если нужен последний номер N, правая граница range должна быть N + 1. В задании на факториал договоритесь, что факториал нуля равен единице.",
        "examples": [
            {
                "title": "Накопление и счётчик",
                "code": "def count_multiples_of_three(n):\n    count = 0\n    for number in range(1, n + 1):\n        if number % 3 == 0:\n            count += 1\n    return count\n\nprint(count_multiples_of_three(10))\n# Вывод: 3",
                "explanation": "Один шаблон цикла можно использовать для подсчёта, заменив условие."
            },
            {
                "title": "Вложенный цикл для таблицы",
                "code": "for row in range(1, 4):\n    line = \"\"\n    for column in range(1, 4):\n        line += f\"{row * column:3}\"\n    print(line)\n# Вывод:\n#   1  2  3\n#   2  4  6\n#   3  6  9",
                "explanation": "Внутренний цикл строит одну строку, внешний выводит её после завершения."
            }
        ],
        "tasks": [
            {
                "question": "A1. Напишите функцию, которая выводит числа от 1 до n включительно.",
                "hint": "Используйте правую границу n + 1.",
                "answer": [
                    "def show_to_n(n):\n    for number in range(1, n + 1):\n        print(number)",
                    "def show_to_n(n):\n    for number in range(n):\n        print(number + 1)"
                ]
            },
            {
                "question": "A2. Напишите функцию, которая выводит обратный отсчёт от n до 1.",
                "hint": "У range можно задать отрицательный шаг.",
                "answer": [
                    "def countdown(n):\n    for number in range(n, 0, -1):\n        print(number)",
                    "def countdown(n):\n    for number in range(n, 1 - 1, -1):\n        print(number)"
                ]
            },
            {
                "question": "A3. Напишите функцию, которая печатает все числа до n, кратные трём.",
                "hint": "Можно использовать range с шагом 3.",
                "answer": [
                    "def multiples_of_three(n):\n    for number in range(3, n + 1, 3):\n        print(number)",
                    "def multiples_of_three(n):\n    for number in range(1, n + 1):\n        if number % 3 == 0:\n            print(number)"
                ]
            },
            {
                "question": "Что выведет print(5 * 2) и сколько раз выполнится тело for _ in range(5)?",
                "hint": "Правая граница range не включается.",
                "answer": "10 и 5 раз"
            },
            {
                "question": "B1. Напишите функцию суммы цифр положительного числа n без преобразования в строку.",
                "hint": "На каждой итерации отделяйте последнюю цифру через остаток от 10.",
                "answer": [
                    "def digit_sum(n):\n    total = 0\n    while n > 0:\n        total += n % 10\n        n //= 10\n    return total",
                    "def digit_sum(n):\n    total = 0\n    for digit in str(n):\n        total += int(digit)\n    return total"
                ]
            },
            {
                "question": "B2. Напишите функцию factorial(n), которая возвращает произведение от 1 до n.",
                "hint": "Начните накопитель с 1; для n = 0 ответ тоже 1.",
                "answer": [
                    "def factorial(n):\n    result = 1\n    for number in range(1, n + 1):\n        result *= number\n    return result",
                    "def variable_1(variable_2):\n    variable_3 = 1\n    for variable_4 in range(1, variable_2 + 1):\n        variable_3 *= variable_4\n    return variable_3"
                ]
            },
            {
                "question": "B3. Напишите функцию average_input(n), которая считывает n чисел и возвращает среднее; при n <= 0 верните None.",
                "hint": "Суммируйте вводы в цикле, затем разделите на n.",
                "answer": [
                    "def average_input(n):\n    if n <= 0:\n        return None\n    total = 0\n    for _ in range(n):\n        total += float(input())\n    return total / n",
                    "def variable_1(variable_2):\n    if variable_2 <= 0:\n        return None\n    variable_3 = 0\n    for variable_4 in range(variable_2):\n        variable_3 += float(input())\n    return variable_3 / variable_2"
                ]
            },
            {
                "question": "B4. Напишите функцию count_symbol(text, target), которая считает точные совпадения символа циклом.",
                "hint": "Не используйте метод count: цель задания — счётчик в цикле.",
                "answer": [
                    "def count_symbol(text, target):\n    count = 0\n    for symbol in text:\n        if symbol == target:\n            count += 1\n    return count",
                    "def variable_1(variable_2, variable_3):\n    variable_4 = 0\n    for variable_5 in variable_2:\n        if variable_5 == variable_3:\n            variable_4 += 1\n    return variable_4"
                ]
            },
            {
                "question": "B5. Сколько чисел от 1 до 100 включительно делятся на 3 или на 5? Напишите функцию подсчёта.",
                "hint": "Используйте одно условие с or и увеличивайте счётчик один раз.",
                "answer": [
                    "def count_3_or_5():\n    count = 0\n    for number in range(1, 101):\n        if number % 3 == 0 or number % 5 == 0:\n            count += 1\n    return count",
                    "def variable_1():\n    variable_2 = 0\n    for variable_3 in range(1, 101):\n        if variable_3 % 3 == 0 or variable_3 % 5 == 0:\n            variable_2 += 1\n    return variable_2"
                ]
            },
            {
                "question": "C1. Напишите функцию multiplication_table(), которая печатает таблицу умножения от 1 до 9 сеткой.",
                "hint": "Внешний цикл отвечает за строки, внутренний — за столбцы.",
                "answer": [
                    "def multiplication_table():\n    for row in range(1, 10):\n        line = \"\"\n        for column in range(1, 10):\n            line += f\"{row * column:4}\"\n        print(line)",
                    "def variable_1():\n    for variable_2 in range(1, 10):\n        variable_3 = ''\n        for variable_4 in range(1, 10):\n            variable_3 += f'{variable_2 * variable_4:4}'\n        print(variable_3)"
                ]
            },
            {
                "question": "C2. Напишите функцию staircase(height), которая возвращает лесенку из символов #.",
                "hint": "На строке номер row добавляйте row символов и перевод строки.",
                "answer": [
                    "def staircase(height):\n    result = \"\"\n    for row in range(1, height + 1):\n        result += \"#\" * row\n        if row < height:\n            result += \"\\n\"\n    return result",
                    "def staircase(height):\n    result = \"\"\n    for row in range(height):\n        for _ in range(row + 1):\n            result += \"#\"\n        if row < height - 1:\n            result += \"\\n\"\n    return result"
                ]
            }
        ]
    },
    {
        "title": "while: цикл по условию и защита от зависания",
        "theory": "while повторяет тело, пока условие истинно. Он подходит, когда число повторений заранее неизвестно: например, пока сумма не достигла цели или пока пользователь не ввёл стоп-сигнал. Переменная условия должна меняться так, чтобы цикл когда-нибудь завершился; Ctrl+C останавливает зависшую программу.\n\nДля известного диапазона обычно проще for; для условия, зависящего от данных, удобнее while. Ловушка: если забыть обновить число в условии, программа повторит один и тот же шаг бесконечно. Проверьте, что каждое прохождение цикла приближает к выходу, и предусмотрите граничный ввод 0 или отрицательное значение.",
        "examples": [
            {
                "title": "Обратный отсчёт",
                "code": "number = 3\nwhile number > 0:\n    print(number)\n    number -= 1\nprint(\"Старт!\")\n# Вывод:\n# 3\n# 2\n# 1\n# Старт!",
                "explanation": "После каждого вывода счётчик уменьшается и условие становится ложным."
            },
            {
                "title": "Сумма до нуля",
                "code": "total = 0\nnumber = int(input(\"Число (0 — конец): \"))\nwhile number != 0:\n    total += number\n    number = int(input(\"Число (0 — конец): \"))\nprint(total)\n# Ввод: 2, 3, 0\n# Вывод: 5",
                "explanation": "Условие выхода проверяется по последнему введённому значению."
            }
        ],
        "tasks": [
            {
                "question": "Напишите функцию, которая считает количество цифр положительного числа через while.",
                "hint": "Уменьшайте число целочисленным делением на 10.",
                "answer": [
                    "def count_digits(number):\n    count = 0\n    while number > 0:\n        count += 1\n        number //= 10\n    return count",
                    "def count_digits(number):\n    count = 0\n    while number:\n        count += 1\n        number //= 10\n    return count"
                ]
            },
            {
                "question": "Напишите функцию steps_to_over_1000(number) для положительного number; верните None, если число не положительное.",
                "hint": "Предполагается положительное число; удваивайте его до превышения 1000.",
                "answer": [
                    "def steps_to_over_1000(number):\n    if number <= 0:\n        return None\n    steps = 0\n    while number <= 1000:\n        number *= 2\n        steps += 1\n    return steps",
                    "def variable_1(variable_2):\n    if variable_2 <= 0:\n        return None\n    variable_3 = 0\n    while variable_2 <= 1000:\n        variable_2 *= 2\n        variable_3 += 1\n    return variable_3"
                ]
            },
            {
                "question": "Вклад начинает с положительной суммы start и растёт на положительный rate процентов в год. За сколько лет он удвоится?",
                "hint": "Предполагаются положительные start и rate; умножайте сумму на 1 + rate / 100.",
                "answer": [
                    "def years_to_double(start, rate):\n    if start <= 0 or rate <= 0:\n        return None\n    target = start * 2\n    balance = start\n    years = 0\n    while balance < target:\n        balance *= 1 + rate / 100\n        years += 1\n    return years",
                    "def variable_1(variable_2, variable_3):\n    if variable_2 <= 0 or variable_3 <= 0:\n        return None\n    variable_4 = variable_2 * 2\n    variable_5 = variable_2\n    variable_6 = 0\n    while variable_5 < variable_4:\n        variable_5 *= 1 + variable_3 / 100\n        variable_6 += 1\n    return variable_6"
                ]
            },
            {
                "question": "Что произойдёт, если условие while остаётся True и ни одна переменная цикла не меняется?",
                "hint": "Цикл не дойдёт до обычного выхода.",
                "answer": "бесконечный цикл"
            }
        ]
    },
    {
        "title": "break, continue и повторный ввод до верного ответа",
        "theory": "break немедленно выходит из ближайшего цикла, continue пропускает остаток текущей итерации и переходит к следующей. Шаблон while True с выходом через break удобен для повторного запроса: сначала прочитайте ответ, затем проверьте его и явно выйдите при успехе.\n\nКоличество попыток можно хранить в счётчике и завершать цикл после установленного лимита. Ловушка: если continue стоит до шага счётчика, счётчик может никогда не измениться и цикл зависнет. Размещайте обязательное изменение состояния так, чтобы оно выполнялось и при пропуске итерации, либо перестройте ветвление.",
        "examples": [
            {
                "title": "Три попытки пароля",
                "code": "attempts = 0\nsuccess = False\nwhile attempts < 3:\n    password = input(\"Пароль: \")\n    attempts += 1\n    if password == \"python\":\n        print(\"Вход выполнен\")\n        success = True\n        break\nif not success:\n    print(\"Попытки закончились\")\n# Ввод: неверный, python\n# Вывод: Вход выполнен",
                "explanation": "Флаг success заменяет конструкцию while-else: после цикла видно, был ли пароль верным."
            },
            {
                "title": "Пропуск отрицательных чисел",
                "code": "total = 0\nfor number in range(-2, 4):\n    if number < 0:\n        continue\n    total += number\nprint(total)\n# Вывод: 6",
                "explanation": "Цикл перебирает числа диапазона и пропускает отрицательные через continue."
            }
        ],
        "tasks": [
            {
                "question": "Напишите функцию, которая просит возраст повторно, пока не получит целое число от 0 до 120.",
                "hint": "Обработайте ValueError и проверяйте диапазон перед return.",
                "answer": [
                    "def ask_age():\n    while True:\n        try:\n            age = int(input(\"Возраст: \"))\n        except ValueError:\n            print(\"Введите целое число\")\n            continue\n        if 0 <= age <= 120:\n            return age",
                    "def variable_1():\n    while True:\n        try:\n            variable_2 = int(input('Возраст: '))\n        except ValueError:\n            print('Введите целое число')\n            continue\n        if 0 <= variable_2 <= 120:\n            return variable_2"
                ]
            },
            {
                "question": "Напишите функцию суммы чисел до ввода stop; нечисловые значения пропускайте.",
                "hint": "Для преобразования используйте try/except ValueError, для выхода — break.",
                "answer": [
                    "def sum_until_stop():\n    total = 0\n    while True:\n        text = input()\n        if text == \"stop\":\n            break\n        try:\n            total += float(text)\n        except ValueError:\n            continue\n    return total",
                    "def variable_1():\n    variable_2 = 0\n    while True:\n        variable_3 = input()\n        if variable_3 == 'stop':\n            break\n        try:\n            variable_2 += float(variable_3)\n        except ValueError:\n            continue\n    return variable_2"
                ]
            },
            {
                "question": "Найдите первое число, делящееся на 7, в диапазоне от start до stop включительно. Верните None, если его нет.",
                "hint": "Цикл можно закончить через break после первого совпадения.",
                "answer": [
                    "def first_multiple_of_seven(start, stop):\n    for number in range(start, stop + 1):\n        if number % 7 == 0:\n            return number\n    return None",
                    "def first_multiple_of_seven(start, stop):\n    number = start\n    while number <= stop:\n        if number % 7 == 0:\n            return number\n        number += 1\n    return None"
                ]
            },
            {
                "question": "Почему continue до увеличения счётчика опасен в цикле while?",
                "hint": "Условие может видеть одно и то же значение бесконечно.",
                "answer": "счётчик не меняется и цикл не завершается"
            }
        ]
    },
    {
        "title": "Вложенные циклы и шаблоны алгоритмов",
        "theory": "Вложенный цикл запускает внутренний цикл для каждого шага внешнего. Так строят прямоугольники, таблицы и перебирают пары значений. Размещайте print на нужном уровне: внутри обоих циклов печатается один элемент, после внутреннего цикла — целая строка.\n\nНакопитель, счётчик, флаг и поиск минимума/максимума — повторяющиеся шаблоны. Перед началом внутреннего подсчёта инициализируйте локальный накопитель внутри внешнего цикла. Ловушка: если сбросить его снаружи, суммы разных строк смешаются; если поставить инициализацию не в тот отступ, результат будет неверным.",
        "examples": [
            {
                "title": "Прямоугольник из символов",
                "code": "rows = 3\ncolumns = 5\nfor row in range(rows):\n    line = \"\"\n    for column in range(columns):\n        line += \"*\"\n    print(line)\n# Вывод:\n# *****\n# *****\n# *****",
                "explanation": "Внутренний цикл формирует строку из columns символов."
            },
            {
                "title": "Поиск с флагом",
                "code": "target = 7\nfound = False\nfor number in range(1, 10):\n    if number == target:\n        found = True\n        break\nprint(found)\n# Вывод: True",
                "explanation": "Флаг хранит факт нахождения, а break прекращает ненужный поиск."
            }
        ],
        "tasks": [
            {
                "question": "Напишите функцию, которая возвращает прямоугольник из N строк и M символов # в каждой строке.",
                "hint": "Собирайте строку во внутреннем цикле и переносите строку между рядами.",
                "answer": [
                    "def rectangle(n, m):\n    result = \"\"\n    for row in range(n):\n        for column in range(m):\n            result += \"#\"\n        if row < n - 1:\n            result += \"\\n\"\n    return result",
                    "def rectangle(n, m):\n    line = \"#\" * m\n    result = \"\"\n    for row in range(n):\n        if row:\n            result += \"\\n\"\n        result += line\n    return result"
                ]
            },
            {
                "question": "Напишите функцию, которая печатает все пары чисел от 1 до n с суммой target.",
                "hint": "Два цикла перебирают первое и второе число; не печатайте пару дважды.",
                "answer": [
                    "def print_pairs(n, target):\n    for first in range(1, n + 1):\n        for second in range(first, n + 1):\n            if first + second == target:\n                print(first, second)",
                    "def variable_1(variable_2, variable_3):\n    for variable_4 in range(1, variable_2 + 1):\n        for variable_5 in range(variable_4, variable_2 + 1):\n            if variable_4 + variable_5 == variable_3:\n                print(variable_4, variable_5)"
                ]
            },
            {
                "question": "Напишите функцию поиска максимума из N введённых чисел, сохраняя только текущий рекорд.",
                "hint": "Первое число задаёт начальный максимум, остальные сравниваются с ним.",
                "answer": [
                    "def read_max(n):\n    largest = float(input())\n    for _ in range(n - 1):\n        number = float(input())\n        if number > largest:\n            largest = number\n    return largest",
                    "def variable_1(variable_2):\n    variable_3 = float(input())\n    for variable_4 in range(variable_2 - 1):\n        variable_5 = float(input())\n        if variable_5 > variable_3:\n            variable_3 = variable_5\n    return variable_3"
                ]
            },
            {
                "question": "Где нужно обнулять сумму для каждой строки прямоугольной таблицы?",
                "hint": "Накопитель должен начинать заново для следующей строки.",
                "answer": "внутри внешнего цикла"
            }
        ]
    },
    {
        "title": "Тренажёр: «while и вложенные циклы»",
        "theory": "В части A тренируются остановка по условию и обновление счётчика. В части B несколько шагов образуют алгоритм: деление числа на цифры, поиск делителей или остатки для FizzBuzz. В части C нужно наблюдать за изменением состояния игры или узора после каждого шага.\n\nДля каждого цикла заранее назовите условие выхода и переменную, которая его изменяет. Проверяйте ноль, отрицательное значение, пустой ввод и случай, когда ответ найден сразу. Ловушка: continue не должен перескочить через единственное изменение счётчика.",
        "examples": [
            {
                "title": "Степени двойки через while",
                "code": "number = 1\nwhile number <= 20:\n    print(number)\n    number *= 2\n# Вывод:\n# 1\n# 2\n# 4\n# 8\n# 16",
                "explanation": "Условие ограничивает диапазон, а умножение изменяет переменную цикла."
            },
            {
                "title": "FizzBuzz до 15",
                "code": "for number in range(1, 16):\n    if number % 15 == 0:\n        print(\"FizzBuzz\")\n    elif number % 3 == 0:\n        print(\"Fizz\")\n    elif number % 5 == 0:\n        print(\"Buzz\")\n    else:\n        print(number)\n# Вывод:\n# 1\n# 2\n# Fizz\n# 4\n# Buzz\n# Fizz\n# 7\n# 8\n# Fizz\n# Buzz\n# 11\n# Fizz\n# 13\n# 14\n# FizzBuzz",
                "explanation": "Проверка делимости на 15 идёт первой, потому что число также делится на 3 и на 5."
            }
        ],
        "tasks": [
            {
                "question": "A1. Напишите функцию, которая считает от 1 до n через while.",
                "hint": "Изменяйте счётчик на каждой итерации.",
                "answer": [
                    "def count_to(n):\n    number = 1\n    while number <= n:\n        print(number)\n        number += 1",
                    "def variable_1(variable_2):\n    variable_3 = 1\n    while variable_3 <= variable_2:\n        print(variable_3)\n        variable_3 += 1"
                ]
            },
            {
                "question": "A2. Напишите функцию, которая читает строки до слова stop и возвращает количество непустых строк.",
                "hint": "Проверяйте стоп-слово до увеличения счётчика.",
                "answer": [
                    "def count_until_stop():\n    count = 0\n    while True:\n        text = input().strip()\n        if text == \"stop\":\n            return count\n        if text:\n            count += 1",
                    "def variable_1():\n    variable_2 = 0\n    while True:\n        variable_3 = input().strip()\n        if variable_3 == 'stop':\n            return variable_2\n        if variable_3:\n            variable_2 += 1"
                ]
            },
            {
                "question": "A3. Напечатайте степени двойки, не превышающие limit.",
                "hint": "Начните с 1 и умножайте значение на 2.",
                "answer": [
                    "def print_powers(limit):\n    value = 1\n    while value <= limit:\n        print(value)\n        value *= 2",
                    "def variable_1(variable_2):\n    variable_3 = 1\n    while variable_3 <= variable_2:\n        print(variable_3)\n        variable_3 *= 2"
                ]
            },
            {
                "question": "B1. Напишите функцию FizzBuzz для чисел от 1 до n.",
                "hint": "Проверяйте кратность 15 раньше кратности 3 и 5.",
                "answer": [
                    "def fizzbuzz(n):\n    for number in range(1, n + 1):\n        if number % 15 == 0:\n            print(\"FizzBuzz\")\n        elif number % 3 == 0:\n            print(\"Fizz\")\n        elif number % 5 == 0:\n            print(\"Buzz\")\n        else:\n            print(number)",
                    "def variable_1(variable_2):\n    for variable_3 in range(1, variable_2 + 1):\n        if variable_3 % 15 == 0:\n            print('FizzBuzz')\n        elif variable_3 % 3 == 0:\n            print('Fizz')\n        elif variable_3 % 5 == 0:\n            print('Buzz')\n        else:\n            print(variable_3)"
                ]
            },
            {
                "question": "B2. Напишите функцию is_prime(n), которая проверяет простое число циклом.",
                "hint": "Числа меньше 2 не простые; ищите делитель до n включительно.",
                "answer": [
                    "def is_prime(n):\n    if n < 2:\n        return False\n    for divisor in range(2, n):\n        if n % divisor == 0:\n            return False\n    return True",
                    "def is_prime(n):\n    if n < 2:\n        return False\n    divisor = 2\n    while divisor < n:\n        if n % divisor == 0:\n            return False\n        divisor += 1\n    return True"
                ]
            },
            {
                "question": "B3. Напишите функцию gcd(a, b), которая находит НОД алгоритмом Евклида.",
                "hint": "Пока b не равен нулю, заменяйте пару на b и остаток a % b.",
                "answer": [
                    "def gcd(a, b):\n    while b != 0:\n        a, b = b, a % b\n    return abs(a)",
                    "def variable_1(variable_2, variable_3):\n    while variable_3 != 0:\n        variable_2, variable_3 = (variable_3, variable_2 % variable_3)\n    return abs(variable_2)"
                ]
            },
            {
                "question": "B4. Напишите функцию, которая считает количество цифр положительного числа через while.",
                "hint": "После подсчёта делите число на 10 без остатка.",
                "answer": [
                    "def count_digits(n):\n    count = 0\n    while n > 0:\n        count += 1\n        n //= 10\n    return count",
                    "def variable_1(variable_2):\n    variable_3 = 0\n    while variable_2 > 0:\n        variable_3 += 1\n        variable_2 //= 10\n    return variable_3"
                ]
            },
            {
                "question": "B5. Напишите функцию суммы цифр положительного числа через while.",
                "hint": "Добавляйте n % 10 и удаляйте последнюю цифру через // 10.",
                "answer": [
                    "def digit_sum(n):\n    total = 0\n    while n > 0:\n        total += n % 10\n        n //= 10\n    return total",
                    "def variable_1(variable_2):\n    variable_3 = 0\n    while variable_2 > 0:\n        variable_3 += variable_2 % 10\n        variable_2 //= 10\n    return variable_3"
                ]
            },
            {
                "question": "C1. Напишите функцию pyramid(height), которая возвращает центрированную пирамиду из #.",
                "hint": "В строке row пробелов становится меньше, а символов — на два больше.",
                "answer": [
                    "def pyramid(height):\n    result = \"\"\n    for row in range(height):\n        if row:\n            result += \"\\n\"\n        result += \" \" * (height - row - 1) + \"#\" * (2 * row + 1)\n    return result",
                    "def variable_1(variable_2):\n    variable_3 = ''\n    for variable_4 in range(variable_2):\n        if variable_4:\n            variable_3 += '\\n'\n        variable_3 += ' ' * (variable_2 - variable_4 - 1) + '#' * (2 * variable_4 + 1)\n    return variable_3"
                ]
            },
            {
                "question": "C2. Напишите функцию fib_until(limit), которая печатает числа Фибоначчи до границы.",
                "hint": "Обновляйте два последних числа через временные значения.",
                "answer": [
                    "def fib_until(limit):\n    first, second = 0, 1\n    while first <= limit:\n        print(first)\n        first, second = second, first + second",
                    "def variable_1(variable_2):\n    variable_3, variable_4 = (0, 1)\n    while variable_3 <= variable_2:\n        print(variable_3)\n        variable_3, variable_4 = (variable_4, variable_3 + variable_4)"
                ]
            },
            {
                "question": "C3. Напишите функцию угадывания: она получает secret, читает догадки и сообщает больше/меньше до совпадения.",
                "hint": "После правильной догадки выйдите из цикла через break.",
                "answer": [
                    "def play_until(secret):\n    while True:\n        guess = int(input())\n        if guess == secret:\n            print(\"Угадали\")\n            break\n        if guess < secret:\n            print(\"Больше\")\n        else:\n            print(\"Меньше\")",
                    "def variable_1(variable_2):\n    while True:\n        variable_3 = int(input())\n        if variable_3 == variable_2:\n            print('Угадали')\n            break\n        if variable_3 < variable_2:\n            print('Больше')\n        else:\n            print('Меньше')"
                ]
            }
        ]
    },
    {
        "title": "Практика: «Угадай число»",
        "theory": "Соберите игру, в которой компьютер загадывает число от 1 до 100, а игрок получает подсказки «больше» или «меньше». В минимальной версии нужен один цикл и проверка попадания. Затем добавьте ограничение в семь попыток, повтор игры и отдельные счётчики побед и поражений.\n\nОбработайте нечисловой ввод, пустую строку, число вне диапазона и повторную догадку. Повторное число не должно съедать попытку, если таково правило игры. Вынесите одну игру в функцию, а цикл повторных партий — в отдельную функцию или точку входа.",
        "examples": [
            {
                "title": "Одна партия",
                "code": "import random\nrandom.seed(7)\n\nsecret = random.randint(1, 100)\nwhile True:\n    guess = int(input(\"Ваш вариант: \"))\n    if guess == secret:\n        print(\"Угадали!\")\n        break\n    if guess < secret:\n        print(\"Больше\")\n    else:\n        print(\"Меньше\")\n# Ввод: 42\n# Вывод: Угадали!",
                "explanation": "Случайное число создаётся один раз перед циклом, иначе догадка будет сравниваться с новой целью."
            },
            {
                "title": "Лимит попыток и защита ввода",
                "code": "secret = 42\nattempts = 0\nwhile attempts < 7:\n    text = input(\"Число от 1 до 100: \").strip()\n    try:\n        guess = int(text)\n    except ValueError:\n        print(\"Введите целое число\")\n        continue\n    if not 1 <= guess <= 100:\n        print(\"Число вне диапазона\")\n        continue\n    attempts += 1\n    if guess == secret:\n        print(\"Победа\")\n        break\n    print(\"Больше\" if guess < secret else \"Меньше\")\n# Ввод: abc, 42\n# Вывод:\n# Введите целое число\n# Победа",
                "explanation": "Неверный формат и выход за диапазон не расходуют одну из семи попыток."
            }
        ],
        "tasks": [
            {
                "question": "Этап 1. Напишите функцию одной партии с подсказками и выходом при верной догадке.",
                "hint": "Загадка задаётся параметром, чтобы пример можно было проверять без случайности.",
                "answer": [
                    "def play(secret):\n    while True:\n        guess = int(input())\n        if guess == secret:\n            print(\"Угадали\")\n            break\n        if guess < secret:\n            print(\"Больше\")\n        else:\n            print(\"Меньше\")",
                    "def variable_1(variable_2):\n    while True:\n        variable_3 = int(input())\n        if variable_3 == variable_2:\n            print('Угадали')\n            break\n        if variable_3 < variable_2:\n            print('Больше')\n        else:\n            print('Меньше')"
                ]
            },
            {
                "question": "Этап 2. Добавьте не более семи допустимых попыток.",
                "hint": "Считайте попытку только после проверки диапазона.",
                "answer": [
                    "def play(secret):\n    attempts = 0\n    while attempts < 7:\n        guess = int(input())\n        if not 1 <= guess <= 100:\n            print(\"Введите число от 1 до 100\")\n            continue\n        attempts += 1\n        if guess == secret:\n            print(\"Победа\")\n            return True\n        print(\"Больше\" if guess < secret else \"Меньше\")\n    return False",
                    "def variable_1(variable_2):\n    variable_3 = 0\n    while variable_3 < 7:\n        variable_4 = int(input())\n        if not 1 <= variable_4 <= 100:\n            print('Введите число от 1 до 100')\n            continue\n        variable_3 += 1\n        if variable_4 == variable_2:\n            print('Победа')\n            return True\n        print('Больше' if variable_4 < variable_2 else 'Меньше')\n    return False"
                ]
            },
            {
                "question": "Этап 3. Добавьте обработку пустого и нечислового ввода.",
                "hint": "Преобразование int поместите в try/except ValueError.",
                "answer": [
                    "def read_guess():\n    while True:\n        try:\n            return int(input().strip())\n        except ValueError:\n            print(\"Введите целое число\")",
                    "def variable_1():\n    while True:\n        try:\n            return int(input().strip())\n        except ValueError:\n            print('Введите целое число')"
                ]
            },
            {
                "question": "Этап 4. Добавьте счётчики побед и поражений и вопрос «сыграть ещё?».",
                "hint": "Храните количество побед и поражений в двух отдельных целых переменных.",
                "answer": [
                    "wins = 0\nlosses = 0\nagain = \"да\"\nwhile again == \"да\":\n    won = play(42)\n    if won:\n        wins += 1\n    else:\n        losses += 1\n    print(\"Побед:\", wins, \"Поражений:\", losses)\n    again = input(\"Сыграть ещё? \").strip().lower()",
                    "variable_1 = 0\nvariable_2 = 0\nvariable_3 = 'да'\nwhile variable_3 == 'да':\n    variable_4 = variable_5(42)\n    if variable_4:\n        variable_1 += 1\n    else:\n        variable_2 += 1\n    print('Побед:', variable_1, 'Поражений:', variable_2)\n    variable_3 = input('Сыграть ещё? ').strip().lower()"
                ]
            },
            {
                "question": "Этап 5. Разделите игру и повтор партий на функции.",
                "hint": "Одна функция играет раунд и возвращает True или False, другая обновляет счёт.",
                "answer": [
                    "def play_round(secret):\n    attempts = 0\n    while attempts < 7:\n        try:\n            guess = int(input())\n        except ValueError:\n            continue\n        if not 1 <= guess <= 100:\n            continue\n        attempts += 1\n        if guess == secret:\n            return True\n        print(\"Больше\" if guess < secret else \"Меньше\")\n    return False",
                    "def variable_1(variable_2):\n    variable_3 = 0\n    while variable_3 < 7:\n        try:\n            variable_4 = int(input())\n        except ValueError:\n            continue\n        if not 1 <= variable_4 <= 100:\n            continue\n        variable_3 += 1\n        if variable_4 == variable_2:\n            return True\n        print('Больше' if variable_4 < variable_2 else 'Меньше')\n    return False"
                ]
            }
        ]
    },
    {
        "title": "Отладка: «Ломаем циклы»",
        "theory": "При отладке сначала найдите состояние цикла: начальное значение, условие и шаг. Затем проверьте одно прохождение вручную и сравните с ожидаемым. Если вывод повторяется бесконечно, ищите переменную условия, которая не меняется; если пропускается крайнее значение — проверьте границы range.\n\nИсправляйте один дефект за раз и после каждого исправления повторяйте короткий пример. Особое внимание уделите отступу return и месту сброса накопителя: оба дефекта могут давать правдоподобный, но неполный результат.",
        "examples": [
            {
                "title": "Ошибка на единицу",
                "code": "total = 0\nfor number in range(1, 5):\n    total += number\nprint(total)\n# Вывод: 10",
                "explanation": "Правая граница range не включается."
            },
            {
                "title": "Зависание из-за шага счётчика",
                "code": "number = 1\nwhile number <= 3:\n    print(number)\n    number += 1\n# Вывод:\n# 1\n# 2\n# 3",
                "explanation": "Условие становится ложным, потому что number увеличивается."
            }
        ],
        "tasks": [
            {
                "question": "Фрагмент должен сложить числа от 1 до n, но не включает n. Исправьте диапазон.",
                "hint": "Правая граница должна быть на единицу больше n.",
                "answer": [
                    "for number in range(1, n + 1):\n    total += number",
                    "for variable_1 in range(1, variable_2 + 1):\n    variable_3 += variable_1"
                ]
            },
            {
                "question": "Фрагмент зависает: while number <= n: print(number). Добавьте безопасный шаг.",
                "hint": "Счётчик нужно увеличить внутри тела.",
                "answer": [
                    "while number <= n:\n    print(number)\n    number += 1",
                    "while variable_1 <= variable_2:\n    print(variable_1)\n    variable_1 += 1"
                ]
            },
            {
                "question": "Нужно напечатать итог один раз, но print(total) стоит внутри цикла. Исправьте отступ.",
                "hint": "Вывод разместите после завершения цикла.",
                "answer": [
                    "for number in range(1, n + 1):\n    total += number\nprint(total)",
                    "for variable_1 in range(1, variable_2 + 1):\n    variable_3 += variable_1\nprint(variable_3)"
                ]
            },
            {
                "question": "Функция возвращает сумму после первого числа. Переместите return за пределы цикла.",
                "hint": "Цикл должен завершиться до возврата накопителя.",
                "answer": [
                    "def sum_numbers(n):\n    total = 0\n    for number in range(1, n + 1):\n        total += number\n    return total",
                    "def variable_1(variable_2):\n    variable_3 = 0\n    for variable_4 in range(1, variable_2 + 1):\n        variable_3 += variable_4\n    return variable_3"
                ]
            },
            {
                "question": "Накопитель total обнуляется внутри цикла. Перенесите инициализацию.",
                "hint": "Начальное значение задаётся один раз перед циклом.",
                "answer": [
                    "total = 0\nfor number in range(1, n + 1):\n    total += number",
                    "variable_1 = 0\nfor variable_2 in range(1, variable_3 + 1):\n    variable_1 += variable_2"
                ]
            },
            {
                "question": "В цикле while continue стоит перед number += 1. Исправьте ветвление так, чтобы счётчик менялся при пропуске.",
                "hint": "Можно увеличить счётчик до continue.",
                "answer": [
                    "if number < 0:\n    number += 1\n    continue\nnumber += 1",
                    "if number < 0:\n    number += 1\nelse:\n    process(number)\n    number += 1"
                ]
            }
        ]
    },
    {
        "title": "Индексы и срезы: достаём части строки",
        "theory": "len(text) возвращает длину строки. Индексация начинается с нуля: text[0] — первый символ; отрицательный индекс -1 указывает на последний. Срез text[a:b] берёт символы от a до b, не включая правую границу. Можно опустить начало или конец: text[:b], text[a:].\n\nСрез безопасно возвращает доступную часть даже при границе за длиной строки, а обычный индекс может вызвать IndexError. Строки неизменяемы: присваивание text[0] = \"А\" завершится ошибкой. Методы и срезы создают новые строки, поэтому результат нужно сохранить. Ловушка: не обращайтесь к text[0], пока не проверили, что строка непустая.",
        "examples": [
            {
                "title": "Первая и последняя буква",
                "code": "word = \"Python\"\nprint(word[0])\nprint(word[-1])\n# Вывод:\n# P\n# n",
                "explanation": "Индекс 0 — первый символ, -1 — последний."
            },
            {
                "title": "Разворот строки",
                "code": "text = \"казах\"\nreversed_text = text[::-1]\nprint(reversed_text)\n# Вывод: хазак",
                "explanation": "Срез с шагом -1 читает символы с конца к началу."
            }
        ],
        "tasks": [
            {
                "question": "Напишите функцию, которая возвращает три первых символа text, даже если строка короче.",
                "hint": "Срез не падает, если правая граница больше длины строки.",
                "answer": [
                    "def first_three(text):\n    return text[:3]",
                    "def variable_1(variable_2):\n    return variable_2[:3]"
                ]
            },
            {
                "question": "Напишите функцию, которая проверяет: строка заканчивается тем же символом, с которого начинается. Пустая строка даёт False.",
                "hint": "Проверьте длину до обращения по индексу.",
                "answer": [
                    "def same_ends(text):\n    return len(text) > 0 and text[0] == text[-1]",
                    "def variable_1(variable_2):\n    return len(variable_2) > 0 and variable_2[0] == variable_2[-1]"
                ]
            },
            {
                "question": "Из строки date вида 2026-11-20 извлеките год.",
                "hint": "Возьмите срез до первого дефиса.",
                "answer": [
                    "def get_year(date):\n    return date[:4]",
                    "def get_year(date):\n    return date[0:4]"
                ]
            },
            {
                "question": "Почему text[0] может вызвать IndexError, а text[:1] для пустой строки не падает?",
                "hint": "Индекс требует существующий символ, срез допускает границы вне строки.",
                "answer": "индекс обращается к символу, срез возвращает доступную часть"
            },
            {
                "question": "Почему text[0] = \"А\" не заменяет первый символ строки?",
                "hint": "Строка неизменяема; соберите новую строку или используйте метод.",
                "answer": "строки неизменяемы"
            }
        ]
    },
    {
        "title": "Методы строк",
        "theory": "Методы строк возвращают новые значения, потому что строка неизменяема. lower() и upper() меняют регистр в результате, strip() убирает пробелы по краям, replace() заменяет фрагмент, find() ищет позицию или возвращает -1, count() считает вхождения.\n\nsplit() делит строку на части, join() соединяет части через разделитель, startswith() и endswith() проверяют начало и конец, isdigit() проверяет, состоят ли символы из цифр. Результат любого преобразования нужно сохранить или передать дальше. Ловушка: вызов name.upper() без присваивания не меняет исходную строку.",
        "examples": [
            {
                "title": "Нормализация ввода",
                "code": "name = input(\"Имя: \").strip().title()\nprint(name)\n# Ввод: \"  аЛиЯ   \"\n# Вывод: Алия",
                "explanation": "Цепочка получает новую строку на каждом шаге: сначала очищает края, затем оформляет регистр."
            },
            {
                "title": "Разбор строки",
                "code": "record = \"Иван Петров 25\"\nparts = record.split()\nname = parts[0] + \" \" + parts[1]\nage = int(parts[2])\nprint(name, age)\n# Вывод: Иван Петров 25",
                "explanation": "split() без аргумента разбивает по любому числу пробелов и возвращает части."
            }
        ],
        "tasks": [
            {
                "question": "Напишите код, который убирает внешние пробелы и приводит имя к виду Иван Петров.",
                "hint": "Сначала strip(), затем title().",
                "answer": [
                    "clean_name = input().strip().title()",
                    "name = input()\nclean_name = name.strip().title()"
                ]
            },
            {
                "question": "Напишите функцию подсчёта слов в предложении, используя split().",
                "hint": "Пустая строка после split() даёт пустой результат.",
                "answer": [
                    "def word_count(text):\n    return len(text.split())",
                    "def variable_1(variable_2):\n    return len(variable_2.split())"
                ]
            },
            {
                "question": "Напишите выражение, которое заменяет все пробелы в text на дефисы.",
                "hint": "Метод возвращает новую строку.",
                "answer": [
                    "result = text.replace(\" \", \"-\")",
                    "variable_1 = variable_2.replace(' ', '-')"
                ]
            },
            {
                "question": "После name.upper() исходная строка name изменилась?",
                "hint": "Строки неизменяемы; результат нужно присвоить.",
                "answer": "нет"
            }
        ]
    },
    {
        "title": "Форматирование вывода: f-строки, числа и выравнивание",
        "theory": "f-строка вставляет значения выражений в фигурные скобки. Формат .2f показывает два знака после запятой, а ширина поля задаёт минимальное число символов. Символы <, > и ^ выравнивают содержимое влево, вправо или по центру. Разделитель тысяч можно добавить спецификатором числа.\n\nПеревод строки записывается как \\n, табуляция — как \\t; они полезны для отчётов и таблиц. Чтобы получить пробел вместо запятой-разделителя тысяч, можно преобразовать отформатированную строку через replace. Ловушка: ширина поля не обрезает длинный текст, а только задаёт минимум.",
        "examples": [
            {
                "title": "Выровненный чек",
                "code": "item = \"Чай\"\nprice = 1250.5\nprint(f\"{item:<12}{price:>10.2f}\")\n# Вывод:\n# Чай            1250.50",
                "explanation": "Название занимает поле шириной 12 слева, цена выравнивается вправо с двумя знаками."
            },
            {
                "title": "Разделители и рамка",
                "code": "amount = 1250000.5\nformatted = f\"{amount:,.2f}\".replace(\",\", \" \")\nword = \"Python\"\nprint(formatted)\nprint(f\"|{word:^12}|\")\n# Вывод:\n# 1 250 000.50\n# |   Python   |",
                "explanation": "replace меняет запятые на пробелы, а ^ размещает слово по центру поля."
            }
        ],
        "tasks": [
            {
                "question": "Напишите f-строку для цены price с двумя знаками после точки.",
                "hint": "Используйте спецификатор .2f.",
                "answer": [
                    "f\"{price:.2f}\"",
                    "f'{variable_1:.2f}'"
                ]
            },
            {
                "question": "Напечатайте три названия и цены как выровненные колонки шириной 12 и 10.",
                "hint": "Используйте < для названия и > для цены.",
                "answer": [
                    "print(f\"{name:<12}{price:>10.2f}\")",
                    "print(f'{variable_1:<12}{variable_2:>10.2f}')"
                ]
            },
            {
                "question": "Получите строку 1 250 000.50 из числа 1250000.5.",
                "hint": "Сначала поставьте разделители тысяч, затем замените запятые на пробелы.",
                "answer": [
                    "formatted = f\"{amount:,.2f}\".replace(\",\", \" \")",
                    "variable_1 = f'{variable_2:,.2f}'.replace(',', ' ')"
                ]
            },
            {
                "question": "Что делает ширина поля 5, если строка длиннее пяти символов?",
                "hint": "Ширина задаёт минимум, а не обрезание.",
                "answer": "оставляет строку целиком"
            }
        ]
    },
    {
        "title": "Тренажёр: «Строки»",
        "theory": "Здесь вы комбинируете индексы, срезы и методы строк. Для каждого задания выберите простое решение, затем проверьте пустую строку, один символ, пробелы по краям и символы разного регистра. Преобразования не меняют исходную строку: сохраняйте результат.\n\nВ заданиях уровня C соедините несколько шагов, но не используйте ord или chr. Разворот разрешён срезом [::-1]. Для капитализации слов можно применить split(), а затем соединить части; результат split() — список, это единственное знакомство с ним до урока 84.",
        "examples": [
            {
                "title": "Палиндром без учёта регистра",
                "code": "def is_palindrome(text):\n    cleaned = text.lower().replace(\" \", \"\")\n    return cleaned == cleaned[::-1]\n\nprint(is_palindrome(\"А роза упала на лапу Азора\"))\n# Вывод: True",
                "explanation": "Сначала нормализуются регистр и пробелы, затем сравниваются прямой и обратный текст."
            },
            {
                "title": "Простая проверка email",
                "code": "def looks_like_email(text):\n    at_position = text.find(\"@\")\n    dot_position = text.find(\".\", at_position + 1)\n    return at_position > 0 and dot_position > at_position + 1 and dot_position < len(text) - 1\n\nprint(looks_like_email(\"a@site.kz\"))\n# Вывод: True",
                "explanation": "Это учебная базовая проверка: она ищет @ и точку после неё, но не заменяет полноценную проверку адреса."
            }
        ],
        "tasks": [
            {
                "question": "A1. Напишите функцию, которая считает длину строки и возвращает первый и последний символ отдельно; для пустой строки верните два пустых значения.",
                "hint": "Проверьте пустоту до индексации.",
                "answer": [
                    "def ends(text):\n    if not text:\n        return \"\", \"\"\n    return text[0], text[-1]",
                    "def variable_1(variable_2):\n    if not variable_2:\n        return ('', '')\n    return (variable_2[0], variable_2[-1])"
                ]
            },
            {
                "question": "A2. Напишите функцию разворота строки.",
                "hint": "Используйте разрешённый срез с шагом -1.",
                "answer": [
                    "def reverse_text(text):\n    return text[::-1]",
                    "def variable_1(variable_2):\n    return variable_2[::-1]"
                ]
            },
            {
                "question": "A3. Напишите функцию, которая возвращает text в верхнем регистре.",
                "hint": "Сохраните результат метода.",
                "answer": [
                    "def upper_text(text):\n    return text.upper()",
                    "def variable_1(variable_2):\n    return variable_2.upper()"
                ]
            },
            {
                "question": "B1. Проверьте палиндром, игнорируя регистр и пробелы.",
                "hint": "Удалите пробелы, затем сравните строку с её разворотом.",
                "answer": [
                    "def is_palindrome(text):\n    cleaned = text.lower().replace(\" \", \"\")\n    return cleaned == cleaned[::-1]",
                    "def variable_1(variable_2):\n    variable_3 = variable_2.lower().replace(' ', '')\n    return variable_3 == variable_3[::-1]"
                ]
            },
            {
                "question": "B2. Напишите функцию, которая удаляет все пробелы из строки.",
                "hint": "Можно заменить пробел пустой строкой.",
                "answer": [
                    "def remove_spaces(text):\n    return text.replace(\" \", \"\")",
                    "def remove_spaces(text):\n    return \"\".join(text.split())"
                ]
            },
            {
                "question": "B3. Посчитайте слова в строке, разделённые любым числом пробелов.",
                "hint": "split() без аргумента пропускает лишние пробелы.",
                "answer": [
                    "def word_count(text):\n    return len(text.split())",
                    "def variable_1(variable_2):\n    return len(variable_2.split())"
                ]
            },
            {
                "question": "B4. Замените в строке все символы x на y.",
                "hint": "Метод возвращает новую строку.",
                "answer": [
                    "def replace_x(text):\n    return text.replace(\"x\", \"y\")",
                    "def variable_1(variable_2):\n    return variable_2.replace('x', 'y')"
                ]
            },
            {
                "question": "B5. Посчитайте количество цифр в строке циклом.",
                "hint": "Для каждого символа проверьте isdigit().",
                "answer": [
                    "def digit_count(text):\n    count = 0\n    for symbol in text:\n        if symbol.isdigit():\n            count += 1\n    return count",
                    "def variable_1(variable_2):\n    variable_3 = 0\n    for variable_4 in variable_2:\n        if variable_4.isdigit():\n            variable_3 += 1\n    return variable_3"
                ]
            },
            {
                "question": "C1. Замаскируйте номер карты: оставьте последние четыре цифры, остальные замените на *.",
                "hint": "Проверьте длину и используйте срез конца строки.",
                "answer": [
                    "def mask_card(number):\n    return \"*\" * max(0, len(number) - 4) + number[-4:]",
                    "def variable_1(variable_2):\n    return '*' * max(0, len(variable_2) - 4) + variable_2[-4:]"
                ]
            },
            {
                "question": "C2. Приведите каждое слово в строке к виду с заглавной первой буквой, не используя title().",
                "hint": "Можно разбить split(), обработать части и соединить пробелом.",
                "answer": [
                    "def capitalize_words(text):\n    result = \"\"\n    for word in text.split():\n        if result:\n            result += \" \"\n        result += word[0].upper() + word[1:].lower()\n    return result",
                    "def capitalize_words(text):\n    parts = text.split()\n    result = \"\"\n    index = 0\n    while index < len(parts):\n        if index:\n            result += \" \"\n        word = parts[index]\n        result += word[0].upper() + word[1:].lower()\n        index += 1\n    return result"
                ]
            },
            {
                "question": "C3. Напишите простую проверку email: @ должен быть не первым символом, а точка должна идти после @ и не быть последней.",
                "hint": "Используйте find с начальной позицией после @.",
                "answer": [
                    "def simple_email(text):\n    at = text.find(\"@\")\n    dot = text.find(\".\", at + 1)\n    return at > 0 and dot > at + 1 and dot < len(text) - 1",
                    "def variable_1(variable_2):\n    variable_3 = variable_2.find('@')\n    variable_4 = variable_2.find('.', variable_3 + 1)\n    return variable_3 > 0 and variable_4 > variable_3 + 1 and (variable_4 < len(variable_2) - 1)"
                ]
            }
        ]
    },
    {
        "title": "Практика: «Шифр Цезаря и проверка надёжности пароля»",
        "theory": "В первой части реализуйте шифрование и расшифровку через строку-алфавит и find(). Символы вне алфавита оставляйте без изменений. Перед вычислением нового индекса уменьшайте сдвиг по модулю длины алфавита; так работают и большие, и отрицательные сдвиги.\n\nВо второй части оцените пароль по длине и наличию цифр, строчных и заглавных букв, специальных символов. Всё решение постройте на строках и цикле. Пустая строка должна получить слабую оценку. Это учебная оценка признаков, а не криптографическая проверка стойкости пароля.",
        "examples": [
            {
                "title": "Шифрование и расшифровка",
                "code": "ALPHABET = \"abcdefghijklmnopqrstuvwxyz\"\n\ndef caesar(text, shift):\n    result = \"\"\n    shift %= len(ALPHABET)\n    for symbol in text:\n        lower = symbol.lower()\n        position = ALPHABET.find(lower)\n        if position == -1:\n            result += symbol\n        else:\n            encoded = ALPHABET[(position + shift) % len(ALPHABET)]\n            result += encoded.upper() if symbol.isupper() else encoded\n    return result\n\nprint(caesar(\"Abc!\", 2))\n# Вывод: Cde!",
                "explanation": "find находит позицию буквы; остальные символы копируются без изменения."
            },
            {
                "title": "Флаги надёжности",
                "code": "def password_strength(password):\n    has_digit = False\n    has_lower = False\n    has_upper = False\n    has_special = False\n    for symbol in password:\n        if symbol.isdigit():\n            has_digit = True\n        elif symbol.islower():\n            has_lower = True\n        elif symbol.isupper():\n            has_upper = True\n        else:\n            has_special = True\n    score = int(len(password) >= 8) + int(has_digit) + int(has_lower) + int(has_upper) + int(has_special)\n    if score <= 2:\n        return \"слабый\"\n    if score <= 4:\n        return \"средний\"\n    return \"сильный\"\n\nprint(password_strength(\"Abc123!x\"))\n# Вывод: сильный",
                "explanation": "Каждый признак учитывается один раз; пустой пароль не набирает баллы."
            }
        ],
        "tasks": [
            {
                "question": "Этап 1. Напишите caesar(text, shift) для строчных букв английского алфавита.",
                "hint": "Используйте find и индекс по модулю длины строки алфавита.",
                "answer": [
                    "ALPHABET = \"abcdefghijklmnopqrstuvwxyz\"\ndef caesar(text, shift):\n    result = \"\"\n    for symbol in text:\n        position = ALPHABET.find(symbol)\n        if position == -1:\n            result += symbol\n        else:\n            result += ALPHABET[(position + shift) % len(ALPHABET)]\n    return result",
                    "variable_1 = 'abcdefghijklmnopqrstuvwxyz'\n\ndef variable_2(variable_3, variable_4):\n    variable_5 = ''\n    for variable_6 in variable_3:\n        variable_7 = variable_1.find(variable_6)\n        if variable_7 == -1:\n            variable_5 += variable_6\n        else:\n            variable_5 += variable_1[(variable_7 + variable_4) % len(variable_1)]\n    return variable_5"
                ]
            },
            {
                "question": "Этап 2. Добавьте расшифровку отрицательным сдвигом и сохранение знаков препинания.",
                "hint": "Проверьте индекс -1 и примените отрицательный сдвиг.",
                "answer": [
                    "def decode(text, shift):\n    return caesar(text, -shift)",
                    "def variable_1(variable_2, variable_3):\n    return variable_4(variable_2, -variable_3)"
                ]
            },
            {
                "question": "Этап 3. Обработайте заглавные буквы и сдвиги больше длины алфавита.",
                "hint": "Нормализуйте индекс по длине алфавита и верните регистр исходного символа.",
                "answer": [
                    "def caesar(text, shift):\n    alphabet = \"abcdefghijklmnopqrstuvwxyz\"\n    result = \"\"\n    for symbol in text:\n        position = alphabet.find(symbol.lower())\n        if position == -1:\n            result += symbol\n        else:\n            encoded = alphabet[(position + shift) % len(alphabet)]\n            result += encoded.upper() if symbol.isupper() else encoded\n    return result",
                    "def variable_1(variable_2, variable_3):\n    variable_4 = 'abcdefghijklmnopqrstuvwxyz'\n    variable_5 = ''\n    for variable_6 in variable_2:\n        variable_7 = variable_4.find(variable_6.lower())\n        if variable_7 == -1:\n            variable_5 += variable_6\n        else:\n            variable_8 = variable_4[(variable_7 + variable_3) % len(variable_4)]\n            variable_5 += variable_8.upper() if variable_6.isupper() else variable_8\n    return variable_5"
                ]
            },
            {
                "question": "Этап 4. Напишите функцию, которая проверяет наличие цифры, строчной и заглавной буквы циклом.",
                "hint": "Для каждого признака заведите отдельный флаг.",
                "answer": [
                    "def has_required_kinds(password):\n    digit = False\n    lower = False\n    upper = False\n    for symbol in password:\n        if symbol.isdigit():\n            digit = True\n        if symbol.islower():\n            lower = True\n        if symbol.isupper():\n            upper = True\n    return digit and lower and upper",
                    "def variable_1(variable_2):\n    variable_3 = False\n    variable_4 = False\n    variable_5 = False\n    for variable_6 in variable_2:\n        if variable_6.isdigit():\n            variable_3 = True\n        if variable_6.islower():\n            variable_4 = True\n        if variable_6.isupper():\n            variable_5 = True\n    return variable_3 and variable_4 and variable_5"
                ]
            },
            {
                "question": "Этап 5. Оцените пароль как слабый, средний или сильный по длине и четырём флагам.",
                "hint": "Не используйте коллекции; храните признаки в отдельных переменных.",
                "answer": [
                    "def strength(password):\n    digit = lower = upper = special = False\n    for symbol in password:\n        if symbol.isdigit(): digit = True\n        elif symbol.islower(): lower = True\n        elif symbol.isupper(): upper = True\n        else: special = True\n    score = int(len(password) >= 8) + int(digit) + int(lower) + int(upper) + int(special)\n    if score <= 2: return \"слабый\"\n    if score <= 4: return \"средний\"\n    return \"сильный\"",
                    "def variable_1(variable_2):\n    variable_3 = variable_4 = variable_5 = variable_6 = False\n    for variable_7 in variable_2:\n        if variable_7.isdigit():\n            variable_3 = True\n        elif variable_7.islower():\n            variable_4 = True\n        elif variable_7.isupper():\n            variable_5 = True\n        else:\n            variable_6 = True\n    variable_8 = int(len(variable_2) >= 8) + int(variable_3) + int(variable_4) + int(variable_5) + int(variable_6)\n    if variable_8 <= 2:\n        return 'слабый'\n    if variable_8 <= 4:\n        return 'средний'\n    return 'сильный'"
                ]
            }
        ]
    },
    {
        "title": "Списки: создаём, читаем, изменяем",
        "theory": "Список хранит упорядоченные значения, к которым обращаются по индексу. Методы append и extend добавляют элементы, insert вставляет по позиции, remove удаляет первое совпадение, pop удаляет и возвращает элемент, del удаляет по индексу. in проверяет принадлежность, count считает совпадения, index ищет позицию.\n\nСрезы создают новый список из части исходного. Ловушка: b = a не копирует список — обе переменные указывают на один объект, и изменение через b видно через a. Для поверхностной копии используйте a.copy() или полный срез a[:]. Вложенные изменяемые элементы при этом остаются общими.",
        "examples": [
            {
                "title": "Список покупок",
                "code": "shopping = [\"хлеб\", \"чай\"]\nshopping.append(\"молоко\")\nshopping.insert(1, \"сыр\")\nshopping.remove(\"чай\")\nprint(\", \".join(shopping))\n# Вывод: хлеб, сыр, молоко",
                "explanation": "Методы меняют исходный список; итоговый порядок: хлеб, сыр, молоко."
            },
            {
                "title": "Срез и копия",
                "code": "numbers = [10, 20, 30, 40, 50]\nmiddle = numbers[1:4]\ncopy = numbers.copy()\ncopy.append(60)\nprint(middle)\nprint(numbers)\n# Вывод:\n# [20, 30, 40]\n# [10, 20, 30, 40, 50]",
                "explanation": "Срез и copy создают отдельные внешние списки."
            }
        ],
        "tasks": [
            {
                "question": "Добавьте \"молоко\" в конец списка items.",
                "hint": "Используйте метод для одного нового элемента.",
                "answer": [
                    "items.append(\"молоко\")",
                    "variable_1.append('молоко')"
                ]
            },
            {
                "question": "Напишите код, который получает последние три элемента списка values.",
                "hint": "Срез можно начать с отрицательного индекса.",
                "answer": [
                    "last_three = values[-3:]",
                    "last_three = values[len(values) - 3:]"
                ]
            },
            {
                "question": "Безопасно удалите первый элемент списка values, если он не пуст.",
                "hint": "Проверьте длину перед pop или del.",
                "answer": [
                    "if values:\n    values.pop(0)",
                    "if len(values) > 0:\n    del values[0]"
                ]
            },
            {
                "question": "Почему изменение b после b = a меняет и a?",
                "hint": "Обе переменные ссылаются на один список.",
                "answer": "b = a не копирует список"
            }
        ]
    },
    {
        "title": "Перебор и обработка списков",
        "theory": "for перебирает элементы списка; enumerate добавляет номер, zip проходит по нескольким последовательностям парами. sorted(list) возвращает новый упорядоченный список, а list.sort() меняет список на месте. reverse() также меняет порядок на месте. min, max и sum помогают получить минимум, максимум и сумму чисел.\n\nЛовушка: результат sort() равен None, поэтому запись result = values.sort() не создаёт отсортированную копию. Ещё одна ловушка — удалять элементы из списка во время обхода: индексы сдвигаются, и часть значений пропускается. Создайте новый список подходящих значений или удаляйте по заранее продуманным индексам.",
        "examples": [
            {
                "title": "Нумерованный вывод",
                "code": "names = [\"Алия\", \"Мирас\", \"Жанна\"]\nfor number, name in enumerate(names, start=1):\n    print(number, name)\n# Вывод:\n# 1 Алия\n# 2 Мирас\n# 3 Жанна",
                "explanation": "enumerate возвращает пары номер-элемент."
            },
            {
                "title": "Пары через zip",
                "code": "names = [\"Алия\", \"Мирас\"]\nscores = [5, 4]\nfor name, score in zip(names, scores):\n    print(f\"{name}: {score}\")\n# Вывод:\n# Алия: 5\n# Мирас: 4",
                "explanation": "zip останавливается, когда заканчивается самая короткая последовательность."
            }
        ],
        "tasks": [
            {
                "question": "Напишите функцию среднего значения списка чисел. Для пустого списка верните None.",
                "hint": "Проверьте пустой список до деления.",
                "answer": [
                    "def average(values):\n    if not values:\n        return None\n    return sum(values) / len(values)",
                    "def variable_1(variable_2):\n    if not variable_2:\n        return None\n    return sum(variable_2) / len(variable_2)"
                ]
            },
            {
                "question": "Напечатайте каждый элемент values с номером, начиная с 1.",
                "hint": "Передайте start=1 в enumerate.",
                "answer": [
                    "for number, value in enumerate(values, start=1):\n    print(number, value)",
                    "for variable_1, variable_2 in enumerate(variable_3, start=1):\n    print(variable_1, variable_2)"
                ]
            },
            {
                "question": "Отсортируйте имена по длине, не меняя исходный список.",
                "hint": "sorted принимает функцию ключа и возвращает новый список.",
                "answer": [
                    "result = sorted(names, key=len)",
                    "variable_1 = sorted(variable_2, key=len)"
                ]
            },
            {
                "question": "Что вернёт result после result = values.sort()?",
                "hint": "sort меняет values на месте и не возвращает новый список.",
                "answer": "None"
            },
            {
                "question": "Почему нельзя удалять элементы списка прямо во время for по этому же списку?",
                "hint": "После удаления индексы сдвигаются и часть значений может быть пропущена.",
                "answer": "изменение списка во время обхода сдвигает индексы"
            }
        ]
    },
    {
        "title": "Вложенные списки: таблицы и матрицы",
        "theory": "Матрица — список строк, где каждая строка тоже список. К элементу обращаются двумя индексами: matrix[row][column]. Для обхода строк используйте вложенные циклы; для суммы строки обнуляйте накопитель при начале каждой новой строки.\n\nВложенную структуру можно построить comprehension-ом: внешний цикл создаёт строки, внутренний — значения. Ловушка: [[0] * 3] * 3 повторяет ссылку на одну строку три раза; изменение одного элемента будет заметно во всех строках. Создавайте отдельный внутренний список для каждой строки.",
        "examples": [
            {
                "title": "Таблица умножения",
                "code": "table = [[row * column for column in range(1, 4)] for row in range(1, 4)]\nfor row in table:\n    print(row)\n# Вывод:\n# [1, 2, 3]\n# [2, 4, 6]\n# [3, 6, 9]",
                "explanation": "Внешняя comprehension создаёт строки, внутренняя — значения каждой строки."
            },
            {
                "title": "Сумма каждой строки",
                "code": "matrix = [[1, 2, 3], [4, 5, 6]]\nfor row in matrix:\n    line = \"\"\n    for value in row:\n        if line:\n            line += \" \"\n        line += str(value)\n    print(line)\n# Вывод:\n# 1 2 3\n# 4 5 6",
                "explanation": "Накопитель total сбрасывается внутри внешнего цикла."
            }
        ],
        "tasks": [
            {
                "question": "Напишите функцию суммы главной диагонали квадратной матрицы.",
                "hint": "Индекс строки и столбца диагонали совпадает.",
                "answer": [
                    "def diagonal_sum(matrix):\n    if not matrix:\n        return 0\n    total = 0\n    for index in range(len(matrix)):\n        total += matrix[index][index]\n    return total",
                    "def variable_1(variable_2):\n    if not variable_2:\n        return 0\n    variable_3 = 0\n    for variable_4 in range(len(variable_2)):\n        variable_3 += variable_2[variable_4][variable_4]\n    return variable_3"
                ]
            },
            {
                "question": "Напечатайте матрицу как строки чисел, разделённых пробелами.",
                "hint": "Преобразуйте каждый элемент в строку и соедините их.",
                "answer": [
                    "for row in matrix:\n    line = \"\"\n    for value in row:\n        if line:\n            line += \" \"\n        line += str(value)\n    print(line)",
                    "for variable_1 in variable_2:\n    variable_3 = ''\n    for variable_4 in variable_1:\n        if variable_3:\n            variable_3 += ' '\n        variable_3 += str(variable_4)\n    print(variable_3)"
                ]
            },
            {
                "question": "Транспонируйте прямоугольную матрицу matrix в новую матрицу.",
                "hint": "Внешний цикл идёт по столбцам исходной матрицы.",
                "answer": [
                    "transposed = [[row[column] for row in matrix] for column in range(len(matrix[0]))]",
                    "variable_1 = [[variable_2[variable_3] for variable_2 in variable_4] for variable_3 in range(len(variable_4[0]))]"
                ]
            },
            {
                "question": "Почему изменение matrix[0][0] после [[0] * 3] * 3 меняет значение и в других строках?",
                "hint": "Повторяется ссылка на одну строку.",
                "answer": "все строки ссылаются на один список"
            }
        ]
    },
    {
        "title": "Кортежи: неизменяемые наборы и распаковка",
        "theory": "Кортеж похож на список, но после создания его элементы нельзя заменить. Он подходит для фиксированных связанных значений, например координат точки или имени и результата вычисления. Кортеж можно распаковать в несколько переменных, если число переменных совпадает с числом элементов.\n\nЗапятая создаёт кортеж, а круглые скобки часто только группируют выражение. Поэтому (5) — число, а (5,) — кортеж из одного элемента. Python позволяет обменять значения двух переменных через распаковку: left, right = right, left.",
        "examples": [
            {
                "title": "Координаты и распаковка",
                "code": "point = (4, 7)\nx, y = point\nprint(x, y)\n# Вывод: 4 7",
                "explanation": "Кортеж хранит пару координат, а распаковка назначает каждую координату отдельно."
            },
            {
                "title": "Функция возвращает минимум и максимум",
                "code": "def min_max(values):\n    smallest = min(values)\n    largest = max(values)\n    return smallest, largest\n\nlow, high = min_max([3, 9, 2])\nprint(low, high)\n# Вывод: 2 9",
                "explanation": "Несколько значений после return образуют кортеж."
            }
        ],
        "tasks": [
            {
                "question": "Обменяйте значения a и b одной строкой.",
                "hint": "Используйте распаковку справа налево.",
                "answer": [
                    "a, b = b, a",
                    "variable_1, variable_2 = (variable_2, variable_1)"
                ]
            },
            {
                "question": "Преобразуйте список values в кортеж, а затем обратно в список.",
                "hint": "Вызовите конструкторы tuple и list.",
                "answer": [
                    "as_tuple = tuple(values)\nback_to_list = list(as_tuple)",
                    "variable_1 = tuple(variable_2)\nvariable_3 = list(variable_1)"
                ]
            },
            {
                "question": "Распакуйте запись (name, age, city) в три переменные.",
                "hint": "Число переменных должно совпасть с числом элементов.",
                "answer": [
                    "name, age, city = record",
                    "variable_1, variable_2, variable_3 = variable_4"
                ]
            },
            {
                "question": "Как создать кортеж из одного числа 5?",
                "hint": "Нужна запятая после элемента.",
                "answer": "(5,)"
            }
        ]
    },
    {
        "title": "Тренажёр: «Списки и кортежи»",
        "theory": "Проверьте базовые действия со списками, затем соедините несколько операций в одной задаче. Для удаления дубликатов с сохранением порядка создавайте новый список и добавляйте значение только при первом появлении. Для второго по величине значения отдельно решите, учитывать ли повторения; в этой задаче считаются разные значения.\n\nВ задачах на слияние и разворот следите за крайними случаями: пустой список, один элемент, одинаковые значения и K больше длины. Не используйте сложные срезы с шагом, кроме разворота; учебная цель — понять проход по списку.",
        "examples": [
            {
                "title": "Удаление повторов с сохранением порядка",
                "code": "def unique_in_order(values):\n    result = []\n    for value in values:\n        if value not in result:\n            result.append(value)\n    return result\n\nprint(unique_in_order([2, 1, 2, 3, 1]))\n# Вывод: [2, 1, 3]",
                "explanation": "Проверка in сохраняет первое появление значения."
            },
            {
                "title": "Слияние отсортированных списков",
                "code": "def merge_sorted(left, right):\n    result = []\n    i = 0\n    j = 0\n    while i < len(left) and j < len(right):\n        if left[i] <= right[j]:\n            result.append(left[i])\n            i += 1\n        else:\n            result.append(right[j])\n            j += 1\n    result.extend(left[i:])\n    result.extend(right[j:])\n    return result\n\nprint(merge_sorted([1, 4], [2, 3]))\n# Вывод: [1, 2, 3, 4]",
                "explanation": "Два индекса двигаются по спискам, а оставшаяся часть добавляется в конце."
            }
        ],
        "tasks": [
            {
                "question": "A1. Напишите функцию суммы элементов списка. Для пустого списка верните 0.",
                "hint": "Можно использовать sum или накопитель.",
                "answer": [
                    "def total(values):\n    return sum(values)",
                    "def total(values):\n    result = 0\n    for value in values:\n        result += value\n    return result"
                ]
            },
            {
                "question": "A2. Напишите функцию разворота списка.",
                "hint": "Используйте срез с шагом -1 или цикл.",
                "answer": [
                    "def reverse_list(values):\n    return values[::-1]",
                    "def reverse_list(values):\n    result = []\n    for index in range(len(values) - 1, -1, -1):\n        result.append(values[index])\n    return result"
                ]
            },
            {
                "question": "B1. Удалите дубликаты, сохранив первое появление каждого значения.",
                "hint": "Создайте новый список и проверяйте in перед append.",
                "answer": [
                    "def unique(values):\n    result = []\n    for value in values:\n        if value not in result:\n            result.append(value)\n    return result",
                    "def variable_1(variable_2):\n    variable_3 = []\n    for variable_4 in variable_2:\n        if variable_4 not in variable_3:\n            variable_3.append(variable_4)\n    return variable_3"
                ]
            },
            {
                "question": "B2. Найдите второй по величине различный элемент; если его нет, верните None.",
                "hint": "Можно получить различные значения в новый список и отсортировать.",
                "answer": [
                    "def second_largest(values):\n    unique_values = []\n    for value in values:\n        if value not in unique_values:\n            unique_values.append(value)\n    if len(unique_values) < 2:\n        return None\n    unique_values.sort()\n    return unique_values[-2]",
                    "def second_largest(values):\n    ordered = sorted(values)\n    largest = max(values)\n    for value in reversed(ordered):\n        if value < largest:\n            return value\n    return None"
                ]
            },
            {
                "question": "B3. Объедините два списка, сохраняя каждое значение один раз.",
                "hint": "Добавляйте второй список по одному элементу, проверяя результат через in.",
                "answer": [
                    "def merge_unique(first, second):\n    result = []\n    for value in first + second:\n        if value not in result:\n            result.append(value)\n    return result",
                    "def variable_1(variable_2, variable_3):\n    variable_4 = []\n    for variable_5 in variable_2 + variable_3:\n        if variable_5 not in variable_4:\n            variable_4.append(variable_5)\n    return variable_4"
                ]
            },
            {
                "question": "B4. Подсчитайте чётные числа в списке.",
                "hint": "Используйте счётчик и остаток от деления на 2.",
                "answer": [
                    "def count_even(values):\n    count = 0\n    for value in values:\n        if value % 2 == 0:\n            count += 1\n    return count",
                    "def count_even(values):\n    return len([value for value in values if value % 2 == 0])"
                ]
            },
            {
                "question": "C1. Слейте два уже отсортированных списка, не сортируя весь результат заново.",
                "hint": "Сравнивайте текущие элементы и продвигайте соответствующий индекс.",
                "answer": [
                    "def merge(left, right):\n    result = []\n    i = j = 0\n    while i < len(left) and j < len(right):\n        if left[i] <= right[j]:\n            result.append(left[i]); i += 1\n        else:\n            result.append(right[j]); j += 1\n    result.extend(left[i:]); result.extend(right[j:])\n    return result",
                    "def variable_1(variable_2, variable_3):\n    variable_4 = []\n    variable_5 = variable_6 = 0\n    while variable_5 < len(variable_2) and variable_6 < len(variable_3):\n        if variable_2[variable_5] <= variable_3[variable_6]:\n            variable_4.append(variable_2[variable_5])\n            variable_5 += 1\n        else:\n            variable_4.append(variable_3[variable_6])\n            variable_6 += 1\n    variable_4.extend(variable_2[variable_5:])\n    variable_4.extend(variable_3[variable_6:])\n    return variable_4"
                ]
            },
            {
                "question": "C2. Поверните список вправо на k позиций. Пустой список верните без изменений.",
                "hint": "Сначала уменьшите k по длине списка, затем соедините две части.",
                "answer": [
                    "def rotate_right(values, k):\n    if not values:\n        return []\n    k %= len(values)\n    return values[-k:] + values[:-k] if k else values[:]",
                    "def variable_1(variable_2, variable_3):\n    if not variable_2:\n        return []\n    variable_3 %= len(variable_2)\n    return variable_2[-variable_3:] + variable_2[:-variable_3] if variable_3 else variable_2[:]"
                ]
            },
            {
                "question": "C3. Найдите длину самой длинной неубывающей подряд идущей последовательности.",
                "hint": "Храните длину текущего отрезка и лучший результат.",
                "answer": [
                    "def longest_run(values):\n    if not values:\n        return 0\n    current = best = 1\n    for index in range(1, len(values)):\n        if values[index] >= values[index - 1]:\n            current += 1\n        else:\n            current = 1\n        if current > best:\n            best = current\n    return best",
                    "def variable_1(variable_2):\n    if not variable_2:\n        return 0\n    variable_3 = variable_4 = 1\n    for variable_5 in range(1, len(variable_2)):\n        if variable_2[variable_5] >= variable_2[variable_5 - 1]:\n            variable_3 += 1\n        else:\n            variable_3 = 1\n        if variable_3 > variable_4:\n            variable_4 = variable_3\n    return variable_4"
                ]
            },
            {
                "question": "C4. Получите пары имени и оценки из двух списков одинаковой длины.",
                "hint": "zip соединяет значения по позициям.",
                "answer": [
                    "pairs = list(zip(names, scores))",
                    "variable_1 = list(zip(variable_2, variable_3))"
                ]
            }
        ]
    },
    {
        "title": "Практика: «Журнал оценок»",
        "theory": "Храните журнал как список кортежей: имя ученика и список его оценок. Реализуйте средний балл, лучшего и худшего ученика, рейтинг по убыванию и список учеников со средним ниже 3. Затем добавьте меню для записи нового ученика и добавления оценки.\n\nОтдельно обработайте ученика без оценок, пустой журнал и одинаковые средние. Для пустого журнала и ученика без оценок верните None или выведите понятное сообщение; не делите на ноль.",
        "examples": [
            {
                "title": "Средние баллы",
                "code": "students = [(\"Алия\", [5, 4, 5]), (\"Мирас\", [3, 4])]\nfor name, grades in students:\n    average = sum(grades) / len(grades)\n    print(name, average)\n# Вывод:\n# Алия 4.666666666666667\n# Мирас 3.5",
                "explanation": "Распаковка кортежа сразу даёт имя и список оценок."
            },
            {
                "title": "Список двоечников и рейтинг",
                "code": "students = [(\"Алия\", [5, 4]), (\"Мирас\", [2, 3]), (\"Жанна\", [4, 5])]\nfor name, grades in sorted(students, key=lambda student: sum(student[1]) / len(student[1]), reverse=True):\n    print(name)\n# Вывод:\n# Алия\n# Жанна\n# Мирас",
                "explanation": "Ключ сортировки вычисляет средний балл по списку оценок каждого кортежа."
            }
        ],
        "tasks": [
            {
                "question": "Этап 1. Напишите функцию среднего балла списка оценок; для пустого списка верните None.",
                "hint": "Проверьте длину до деления.",
                "answer": [
                    "def average(grades):\n    if not grades:\n        return None\n    return sum(grades) / len(grades)",
                    "def variable_1(variable_2):\n    if not variable_2:\n        return None\n    return sum(variable_2) / len(variable_2)"
                ]
            },
            {
                "question": "Этап 2. Найдите имя ученика с лучшим средним баллом. Пустой журнал даёт None.",
                "hint": "Инициализируйте лучший результат первым учеником.",
                "answer": [
                    "def best_student(students):\n    best_name = None\n    best_average = None\n    for name, grades in students:\n        if not grades:\n            continue\n        average = sum(grades) / len(grades)\n        if best_average is None or average > best_average:\n            best_name, best_average = name, average\n    return best_name",
                    "def variable_1(variable_2):\n    variable_3 = None\n    variable_4 = None\n    for variable_5, variable_6 in variable_2:\n        if not variable_6:\n            continue\n        variable_7 = sum(variable_6) / len(variable_6)\n        if variable_4 is None or variable_7 > variable_4:\n            variable_3, variable_4 = (variable_5, variable_7)\n    return variable_3"
                ]
            },
            {
                "question": "Этап 3. Верните новый список учеников по убыванию среднего. Учеников без оценок поместите в конец.",
                "hint": "Ключ сортировки должен выделять заполненные оценки и средний балл.",
                "answer": [
                    "def rating(students):\n    def score(student):\n        grades = student[1]\n        return (bool(grades), sum(grades) / len(grades) if grades else 0)\n    return sorted(students, key=score, reverse=True)",
                    "def variable_1(variable_2):\n\n    def variable_3(variable_4):\n        variable_5 = variable_4[1]\n        return (bool(variable_5), sum(variable_5) / len(variable_5) if variable_5 else 0)\n    return sorted(variable_2, key=variable_3, reverse=True)"
                ]
            },
            {
                "question": "Этап 4. Верните учеников со средним ниже 3. Пустые оценки пропускайте.",
                "hint": "Переберите пары и сравните среднее только для непустых оценок.",
                "answer": [
                    "def low_scores(students):\n    result = []\n    for name, grades in students:\n        if grades and sum(grades) / len(grades) < 3:\n            result.append(name)\n    return result",
                    "def variable_1(variable_2):\n    variable_3 = []\n    for variable_4, variable_5 in variable_2:\n        if variable_5 and sum(variable_5) / len(variable_5) < 3:\n            variable_3.append(variable_4)\n    return variable_3"
                ]
            },
            {
                "question": "Этап 5. Добавьте оценку ученику; если имени нет, добавьте новую запись.",
                "hint": "Кортеж неизменяем, поэтому замените запись новым кортежем.",
                "answer": [
                    "def add_grade(students, name, grade):\n    for index, (student_name, grades) in enumerate(students):\n        if student_name == name:\n            students[index] = (student_name, grades + [grade])\n            return\n    students.append((name, [grade]))",
                    "def variable_1(variable_2, variable_3, variable_4):\n    for variable_5, (variable_6, variable_7) in enumerate(variable_2):\n        if variable_6 == variable_3:\n            variable_2[variable_5] = (variable_6, variable_7 + [variable_4])\n            return\n    variable_2.append((variable_3, [variable_4]))"
                ]
            }
        ]
    },
    {
        "title": "Словари: ключи, значения и безопасный доступ",
        "theory": "Словарь связывает ключ со значением. Значение читают по ключу, новое добавляют присваиванием, существующее обновляют тем же способом. get(key, default) возвращает запасное значение, если ключа нет; оператор in проверяет наличие ключа. keys, values и items позволяют обходить ключи, значения или пары.\n\npop удаляет ключ и возвращает его значение; del удаляет ключ без возврата. Ловушка: обращение к отсутствующему ключу через квадратные скобки вызывает KeyError, поэтому для необязательного поля используйте get или проверку in. Список нельзя использовать ключом: ключ должен быть неизменяемым и хешируемым.",
        "examples": [
            {
                "title": "Товар и цена",
                "code": "prices = {\"чай\": 1200, \"хлеб\": 500}\nprices[\"молоко\"] = 700\nprices[\"чай\"] = 1250\nprint(prices.get(\"сыр\", 0))\n# Вывод: 0",
                "explanation": "get возвращает 0 для отсутствующего товара, не вызывая KeyError."
            },
            {
                "title": "Обход пар",
                "code": "prices = {\"чай\": 1200, \"хлеб\": 500}\nfor product, price in prices.items():\n    print(f\"{product}: {price} тг\")\n# Вывод:\n# чай: 1200 тг\n# хлеб: 500 тг",
                "explanation": "items() выдаёт пары ключ-значение для цикла."
            }
        ],
        "tasks": [
            {
                "question": "Создайте словарь products из двух списков names и prices.",
                "hint": "zip соединяет элементы по позициям; передайте пары в dict.",
                "answer": [
                    "products = dict(zip(names, prices))",
                    "variable_1 = dict(zip(variable_2, variable_3))"
                ]
            },
            {
                "question": "Обновите цену чая до 1300 и добавьте цену молока 700.",
                "hint": "Присваивание по ключу добавляет или заменяет значение.",
                "answer": [
                    "prices[\"чай\"] = 1300\nprices[\"молоко\"] = 700",
                    "variable_1['чай'] = 1300\nvariable_1['молоко'] = 700"
                ]
            },
            {
                "question": "Выведите названия товаров дороже 1000 тг.",
                "hint": "Обходите пары через items().",
                "answer": [
                    "for name, price in prices.items():\n    if price > 1000:\n        print(name)",
                    "for variable_1, variable_2 in variable_3.items():\n    if variable_2 > 1000:\n        print(variable_1)"
                ]
            },
            {
                "question": "Как прочитать необязательное поле city со значением по умолчанию «не указан»?",
                "hint": "Используйте get с двумя аргументами.",
                "answer": [
                    "city = person.get(\"city\", \"не указан\")",
                    "variable_1 = variable_2.get('city', 'не указан')"
                ]
            },
            {
                "question": "Какое исключение возникает при чтении отсутствующего ключа через data[\"city\"]?",
                "hint": "Ключ не найден в словаре.",
                "answer": "KeyError"
            },
            {
                "question": "Какое исключение возникает, если список использовать ключом словаря?",
                "hint": "Список изменяем и не может быть хешируемым ключом.",
                "answer": "TypeError"
            }
        ]
    },
    {
        "title": "Паттерны со словарями: подсчёт, группировка и вложенность",
        "theory": "Словарь удобно использовать как счётчик: прочитайте текущее значение через get(key, 0), прибавьте один и сохраните. Для группировки создавайте по ключу список и добавляйте в него значения. Вложенный словарь хранит несколько полей для каждого ключа.\n\nДля сортировки по значению передайте sorted() функцию key, которая возвращает нужное поле. setdefault(key, []) — ещё один способ создать список при первом появлении ключа. Ловушка: нельзя менять размер словаря во время обхода items(); Python выдаст RuntimeError. Обойдите копию ключей или сначала соберите ключи для удаления.",
        "examples": [
            {
                "title": "Частота слов",
                "code": "text = \"чай хлеб чай молоко хлеб чай\"\ncounts = {}\nfor word in text.split():\n    counts[word] = counts.get(word, 0) + 1\nprint(counts[\"чай\"], counts[\"хлеб\"], counts[\"молоко\"])\n# Вывод: 3 2 1",
                "explanation": "get с нулём удобно начинает счёт для нового ключа."
            },
            {
                "title": "Группировка по первой букве",
                "code": "words = [\"арбуз\", \"автор\", \"банан\"]\ngroups = {}\nfor word in words:\n    first = word[0]\n    groups.setdefault(first, []).append(word)\nprint(len(groups[\"а\"]), len(groups[\"б\"]))\n# Вывод: 2 1",
                "explanation": "setdefault создаёт список при первом появлении буквы, а затем добавляет слово в нужную группу."
            }
        ],
        "tasks": [
            {
                "question": "Посчитайте частоту каждого символа в строке text через словарь.",
                "hint": "Для каждого символа увеличивайте прежнее значение или начинайте с нуля.",
                "answer": [
                    "def char_counts(text):\n    counts = {}\n    for symbol in text:\n        counts[symbol] = counts.get(symbol, 0) + 1\n    return counts",
                    "def variable_1(variable_2):\n    variable_3 = {}\n    for variable_4 in variable_2:\n        variable_3[variable_4] = variable_3.get(variable_4, 0) + 1\n    return variable_3"
                ]
            },
            {
                "question": "Сгруппируйте числа по чётности в словарь с ключами чётные и нечётные.",
                "hint": "Создайте два списка и добавляйте туда числа по условию.",
                "answer": [
                    "def group_parity(numbers):\n    groups = {\"чётные\": [], \"нечётные\": []}\n    for number in numbers:\n        key = \"чётные\" if number % 2 == 0 else \"нечётные\"\n        groups[key].append(number)\n    return groups",
                    "def variable_1(variable_2):\n    variable_3 = {'чётные': [], 'нечётные': []}\n    for variable_4 in variable_2:\n        variable_5 = 'чётные' if variable_4 % 2 == 0 else 'нечётные'\n        variable_3[variable_5].append(variable_4)\n    return variable_3"
                ]
            },
            {
                "question": "Найдите самое частое слово; при равенстве оставьте первое встретившееся.",
                "hint": "Сначала посчитайте слова, затем пройдите исходную строку и обновляйте лучший результат только при большем счёте.",
                "answer": [
                    "def most_common_word(text):\n    counts = {}\n    for word in text.lower().split():\n        counts[word] = counts.get(word, 0) + 1\n    best = None\n    for word in text.lower().split():\n        if best is None or counts[word] > counts[best]:\n            best = word\n    return best",
                    "def variable_1(variable_2):\n    variable_3 = {}\n    for variable_4 in variable_2.lower().split():\n        variable_3[variable_4] = variable_3.get(variable_4, 0) + 1\n    variable_5 = None\n    for variable_4 in variable_2.lower().split():\n        if variable_5 is None or variable_3[variable_4] > variable_3[variable_5]:\n            variable_5 = variable_4\n    return variable_5"
                ]
            },
            {
                "question": "Почему нельзя удалять ключи словаря прямо во время обхода items()?",
                "hint": "Размер словаря изменяется в процессе итерации.",
                "answer": "RuntimeError"
            }
        ]
    },
    {
        "title": "Список словарей как «таблица данных»",
        "theory": "Список словарей удобно представляет строки таблицы: у каждой записи одинаковые ключи, а список задаёт порядок. Фильтруйте записи условием, сортируйте через sorted(key=...) и суммируйте выбранные поля. Для обновления найдите запись по идентификатору и измените нужное значение.\n\nНесколько независимых правил сортировки можно объединить в ключ-кортеж, например (отдел, -зарплата). Если поле необязательное, используйте get с запасным значением. Не изменяйте список во время обхода: сначала сформируйте новую выборку, а затем замените старую.",
        "examples": [
            {
                "title": "Фильтрация записей",
                "code": "employees = [\n    {\"name\": \"Алия\", \"department\": \"Продажи\", \"salary\": 450000},\n    {\"name\": \"Мирас\", \"department\": \"Разработка\", \"salary\": 600000},\n]\nselected = [person for person in employees if person[\"salary\"] >= 500000]\nprint(selected[0][\"name\"])\n# Вывод: Мирас",
                "explanation": "Условие работает с каждым словарём, а выбранные записи остаются словарями."
            },
            {
                "title": "Сумма по отделам",
                "code": "employees = [\n    {\"name\": \"Алия\", \"department\": \"Продажи\", \"salary\": 450000},\n    {\"name\": \"Мирас\", \"department\": \"Продажи\", \"salary\": 500000},\n]\ntotals = {}\nfor person in employees:\n    department = person[\"department\"]\n    totals[department] = totals.get(department, 0) + person[\"salary\"]\nprint(totals[\"Продажи\"])\n# Вывод: 950000",
                "explanation": "Словарь totals накапливает сумму зарплат каждой группы."
            }
        ],
        "tasks": [
            {
                "question": "Выберите из records записи, у которых поле active равно True.",
                "hint": "Соберите новый список через условие.",
                "answer": [
                    "active_records = [record for record in records if record[\"active\"]]",
                    "variable_1 = [variable_2 for variable_2 in variable_3 if variable_2['active']]"
                ]
            },
            {
                "question": "Найдите запись с максимальным полем score; если список пуст, верните None.",
                "hint": "Перед max проверьте пустой список или используйте цикл.",
                "answer": [
                    "def best_record(records):\n    if not records:\n        return None\n    return max(records, key=lambda record: record[\"score\"])",
                    "def best_record(records):\n    best = None\n    for record in records:\n        if best is None or record[\"score\"] > best[\"score\"]:\n            best = record\n    return best"
                ]
            },
            {
                "question": "Отсортируйте записи сначала по department, затем по name.",
                "hint": "Ключ может быть кортежем из двух полей.",
                "answer": [
                    "ordered = sorted(records, key=lambda record: (record[\"department\"], record[\"name\"]))",
                    "variable_1 = sorted(variable_2, key=lambda variable_3: (variable_3['department'], variable_3['name']))"
                ]
            },
            {
                "question": "Обновите salary записи с заданным id; если запись не найдена, верните False.",
                "hint": "Переберите записи и измените словарь при совпадении.",
                "answer": [
                    "def update_salary(records, target_id, salary):\n    for record in records:\n        if record[\"id\"] == target_id:\n            record[\"salary\"] = salary\n            return True\n    return False",
                    "def variable_1(variable_2, variable_3, variable_4):\n    for variable_5 in variable_2:\n        if variable_5['id'] == variable_3:\n            variable_5['salary'] = variable_4\n            return True\n    return False"
                ]
            }
        ]
    },
    {
        "title": "Множества: уникальность и операции над наборами",
        "theory": "Множество хранит уникальные хешируемые значения. add добавляет элемент, discard удаляет его без ошибки при отсутствии, remove сообщает об ошибке, если элемента нет. Операции |, &, - и ^ дают объединение, пересечение, разность и симметрическую разность.\n\nМножество удобно для проверки принадлежности и удаления повторов; порядок элементов не гарантирован. Ловушка: {} создаёт пустой словарь, а пустое множество создают через set(). Используйте set(values) для уникальных значений, но не полагайтесь на порядок результата.",
        "examples": [
            {
                "title": "Уникальные слова",
                "code": "words = \"чай хлеб чай молоко\".split()\nunique_words = set(words)\nprint(len(unique_words))\n# Вывод: 3",
                "explanation": "set удаляет повторяющиеся слова."
            },
            {
                "title": "Общие друзья",
                "code": "friends_a = {\"Алия\", \"Мирас\", \"Жанна\"}\nfriends_b = {\"Мирас\", \"Рустам\"}\nprint(sorted(friends_a & friends_b))\nprint(sorted(friends_a | friends_b))\n# Вывод:\n# ['Мирас']\n# ['Алия', 'Жанна', 'Мирас', 'Рустам']",
                "explanation": "Пересечение показывает общие имена, объединение — всех без повторов."
            }
        ],
        "tasks": [
            {
                "question": "Удалите дубликаты из списка values; порядок результата не важен.",
                "hint": "Создайте множество, затем список.",
                "answer": [
                    "unique_values = list(set(values))",
                    "variable_1 = list(set(variable_2))"
                ]
            },
            {
                "question": "Найдите общие значения двух списков first и second.",
                "hint": "Используйте операцию пересечения множеств.",
                "answer": [
                    "common = set(first) & set(second)",
                    "variable_1 = set(variable_2) & set(variable_3)"
                ]
            },
            {
                "question": "Проверьте, все ли символы word находятся в строке allowed.",
                "hint": "Множество символов удобно для in; не используйте порядок.",
                "answer": [
                    "def allowed_word(word, allowed):\n    allowed_chars = set(allowed)\n    for symbol in word:\n        if symbol not in allowed_chars:\n            return False\n    return True",
                    "def variable_1(variable_2, variable_3):\n    variable_4 = set(variable_3)\n    for variable_5 in variable_2:\n        if variable_5 not in variable_4:\n            return False\n    return True"
                ]
            },
            {
                "question": "Что создаёт выражение {}: пустое множество или пустой словарь?",
                "hint": "У пустого множества есть отдельный конструктор.",
                "answer": "пустой словарь"
            },
            {
                "question": "Гарантирует ли set сохранение исходного порядка?",
                "hint": "Порядок элементов множества не является гарантией.",
                "answer": "нет"
            }
        ]
    },
    {
        "title": "Тренажёр: «Словари и множества»",
        "theory": "В части A отрабатываются обращения по ключу и подсчёт. В части B соедините преобразования и операции над наборами. В части C придумайте структуру для нескольких требований сразу и проверьте повторяющиеся значения.\n\nДля подсчёта используйте get, проверку in или setdefault — выбирайте вариант, который делает шаг понятнее. Не полагайтесь на порядок элементов множества. В задачах на анаграммы сначала договоритесь, учитываются ли пробелы и регистр.",
        "examples": [
            {
                "title": "Счётчик через get",
                "code": "def frequencies(text):\n    result = {}\n    for symbol in text:\n        result[symbol] = result.get(symbol, 0) + 1\n    return result\n\ncounts = frequencies(\"aba\")\nprint(counts[\"a\"], counts[\"b\"])\n# Вывод: 2 1",
                "explanation": "Значение по умолчанию позволяет увеличить частоту при первом появлении символа."
            },
            {
                "title": "Общие слова двух текстов",
                "code": "first = set(\"чай хлеб молоко\".split())\nsecond = set(\"чай сыр хлеб\".split())\nprint(len(first & second))\n# Вывод: 2",
                "explanation": "Пересечение даёт значения, которые есть в обоих наборах."
            }
        ],
        "tasks": [
            {
                "question": "A1. Посчитайте частоту символов строки в словаре.",
                "hint": "При первом появлении частота равна нулю, затем увеличьте её.",
                "answer": [
                    "def count_chars(text):\n    result = {}\n    for symbol in text:\n        result[symbol] = result.get(symbol, 0) + 1\n    return result",
                    "def variable_1(variable_2):\n    variable_3 = {}\n    for variable_4 in variable_2:\n        variable_3[variable_4] = variable_3.get(variable_4, 0) + 1\n    return variable_3"
                ]
            },
            {
                "question": "A2. Прочитайте поле city, вернув «не указан», если ключа нет.",
                "hint": "Используйте get с запасным значением.",
                "answer": [
                    "city = person.get(\"city\", \"не указан\")",
                    "variable_1 = variable_2.get('city', 'не указан')"
                ]
            },
            {
                "question": "B1. Инвертируйте словарь с уникальными значениями.",
                "hint": "В цикле поменяйте ключ и значение местами.",
                "answer": [
                    "def invert(data):\n    result = {}\n    for key, value in data.items():\n        result[value] = key\n    return result",
                    "def variable_1(variable_2):\n    variable_3 = {}\n    for variable_4, variable_5 in variable_2.items():\n        variable_3[variable_5] = variable_4\n    return variable_3"
                ]
            },
            {
                "question": "B2. Объедините два словаря цен; значения второго заменяют совпадающие ключи первого.",
                "hint": "Создайте копию первого и обновите её вторым.",
                "answer": [
                    "def merge_prices(first, second):\n    result = first.copy()\n    result.update(second)\n    return result",
                    "def variable_1(variable_2, variable_3):\n    variable_4 = variable_2.copy()\n    variable_4.update(variable_3)\n    return variable_4"
                ]
            },
            {
                "question": "B3. Найдите общие элементы множеств first и second.",
                "hint": "Оператор пересечения — амперсанд.",
                "answer": [
                    "common = first & second",
                    "variable_1 = variable_2 & variable_3"
                ]
            },
            {
                "question": "B4. Верните уникальные слова текста без учёта регистра.",
                "hint": "Сначала нормализуйте строку и разделите на слова.",
                "answer": [
                    "def unique_words(text):\n    return set(text.lower().split())",
                    "def variable_1(variable_2):\n    return set(variable_2.lower().split())"
                ]
            },
            {
                "question": "C1. Проверьте, являются ли две строки анаграммами без учёта пробелов и регистра.",
                "hint": "Сравните частоты символов или отсортированные нормализованные строки.",
                "answer": [
                    "def are_anagrams(first, second):\n    first = first.replace(\" \", \"\").lower()\n    second = second.replace(\" \", \"\").lower()\n    return sorted(first) == sorted(second)",
                    "def are_anagrams(first, second):\n    def counts(text):\n        result = {}\n        for symbol in text.replace(\" \", \"\").lower():\n            result[symbol] = result.get(symbol, 0) + 1\n        return result\n    return counts(first) == counts(second)"
                ]
            },
            {
                "question": "C2. Сгруппируйте слова-анаграммы по отсортированной строке букв.",
                "hint": "Ключ словаря — отсортированные буквы; значение — список слов.",
                "answer": [
                    "def group_anagrams(words):\n    groups = {}\n    for word in words:\n        key = \"\".join(sorted(word.lower()))\n        groups.setdefault(key, []).append(word)\n    return list(groups.values())",
                    "def variable_1(variable_2):\n    variable_3 = {}\n    for variable_4 in variable_2:\n        variable_5 = ''.join(sorted(variable_4.lower()))\n        variable_3.setdefault(variable_5, []).append(variable_4)\n    return list(variable_3.values())"
                ]
            },
            {
                "question": "C3. Объедините словари продаж, складывая значения одинаковых товаров.",
                "hint": "Для каждого ключа второго словаря прибавьте сумму к предыдущей или нулю.",
                "answer": [
                    "def sum_sales(first, second):\n    result = first.copy()\n    for product, amount in second.items():\n        result[product] = result.get(product, 0) + amount\n    return result",
                    "def variable_1(variable_2, variable_3):\n    variable_4 = variable_2.copy()\n    for variable_5, variable_6 in variable_3.items():\n        variable_4[variable_5] = variable_4.get(variable_5, 0) + variable_6\n    return variable_4"
                ]
            },
            {
                "question": "C4. Создайте set из символов строки и проверьте, сколько в ней разных символов.",
                "hint": "Длина множества равна числу уникальных значений.",
                "answer": [
                    "different = len(set(text))",
                    "variable_1 = len(set(variable_2))"
                ]
            }
        ]
    },
    {
        "title": "Практика: «Телефонная книга»",
        "theory": "Храните записи в словаре: имя — ключ, значение — словарь с телефоном и городом. Добавьте функции поиска, изменения, удаления и вывода контактов по алфавиту. Телефон проверяйте через isdigit() и допустимую длину; имя нормализуйте для поиска без учёта регистра.\n\nСохраните книгу в JSON при выходе и загрузите при старте. Если файла нет, начинайте с пустой книги; повреждённый JSON обработайте понятным сообщением. Не допускайте дубликатов имён после нормализации и не удаляйте запись, если имя не найдено.",
        "examples": [
            {
                "title": "Проверка и добавление контакта",
                "code": "def valid_phone(phone):\n    return phone.isdigit() and 7 <= len(phone) <= 15\n\ndef add_contact(book, name, phone, city):\n    if not valid_phone(phone):\n        return False\n    book[name.strip()] = {\"phone\": phone, \"city\": city.strip()}\n    return True\nbook = {}\nadd_contact(book, \"Алия\", \"77001234567\", \"Алматы\")\nprint(book[\"Алия\"][\"phone\"])\n# Вывод: 77001234567",
                "explanation": "Функция возвращает признак успеха, чтобы меню могло показать результат."
            },
            {
                "title": "Загрузка и поиск",
                "code": "import json\nfrom pathlib import Path\n\nDATA_FILE = Path(\"phonebook.json\")\n\ndef load_book():\n    if not DATA_FILE.exists():\n        return {}\n    try:\n        return json.loads(DATA_FILE.read_text(encoding=\"utf-8\"))\n    except json.JSONDecodeError:\n        return {}\n\ndef find_contact(book, fragment):\n    return [name for name in book if fragment.lower() in name.lower()]\n\nbook = {\"Алия\": {\"phone\": \"77001234567\"}, \"Мирас\": {\"phone\": \"77007654321\"}}\nprint(\", \".join(sorted(find_contact(book, \"ал\"))))\n# Вывод: Алия",
                "explanation": "Отсутствующий или повреждённый файл даёт пустую книгу, поиск использует часть имени."
            }
        ],
        "tasks": [
            {
                "question": "Этап 1. Добавьте контакт и найдите его по точному имени.",
                "hint": "Запись хранится по ключу-имени.",
                "answer": [
                    "book[name] = {\"phone\": phone, \"city\": city}",
                    "variable_1[variable_2] = {'phone': variable_3, 'city': variable_4}"
                ]
            },
            {
                "question": "Этап 2. Измените телефон существующего контакта; неизвестное имя верните как False.",
                "hint": "Сначала проверьте ключ через in.",
                "answer": [
                    "def update_phone(book, name, phone):\n    if name not in book:\n        return False\n    book[name][\"phone\"] = phone\n    return True",
                    "def variable_1(variable_2, variable_3, variable_4):\n    if variable_3 not in variable_2:\n        return False\n    variable_2[variable_3]['phone'] = variable_4\n    return True"
                ]
            },
            {
                "question": "Этап 3. Удалите контакт и покажите все имена по алфавиту.",
                "hint": "pop с проверкой не выбрасывает KeyError.",
                "answer": [
                    "def delete_contact(book, name):\n    return book.pop(name, None)\n\nnames = sorted(book)",
                    "def variable_1(variable_2, variable_3):\n    return variable_2.pop(variable_3, None)\nvariable_4 = sorted(variable_2)"
                ]
            },
            {
                "question": "Этап 4. Загрузите книгу из JSON при старте и сохраните при выходе.",
                "hint": "Используйте json.load/dump и обработайте отсутствие файла.",
                "answer": [
                    "def save_book(book, path):\n    with open(path, \"w\", encoding=\"utf-8\") as file:\n        json.dump(book, file, ensure_ascii=False, indent=2)",
                    "def variable_1(variable_2, variable_3):\n    with open(variable_3, 'w', encoding='utf-8') as variable_4:\n        json.dump(variable_2, variable_4, ensure_ascii=False, indent=2)"
                ]
            },
            {
                "question": "Этап 5. Найдите контакты, имя которых содержит фрагмент без учёта регистра.",
                "hint": "Сравните lower() у имени и поисковой строки.",
                "answer": [
                    "def search_names(book, fragment):\n    return [name for name in book if fragment.lower() in name.lower()]",
                    "def variable_1(variable_2, variable_3):\n    return [variable_4 for variable_4 in variable_2 if variable_3.lower() in variable_4.lower()]"
                ]
            }
        ]
    },
    {
        "title": "Практика: «Аналитика заказов»",
        "theory": "Подготовьте 12–15 заказов как список словарей с клиентом, товаром, количеством, ценой и датой. Посчитайте выручку, сумму по клиентам и продажи каждого товара; найдите три наиболее продаваемых товара и выберите заказы выше порога.\n\nИспользуйте множество для уникальных клиентов и f-строки с выравниванием для отчёта. Проверяйте нулевое количество, одинаковые значения продаж, пустой список и дату в ожидаемом формате. Сначала напишите функции расчёта, затем соберите их вывод в один отчёт.",
        "examples": [
            {
                "title": "Выручка по заказам",
                "code": "orders = [\n    {\"client\": \"Алия\", \"product\": \"чай\", \"quantity\": 2, \"price\": 1200, \"date\": \"2026-11-01\"},\n    {\"client\": \"Мирас\", \"product\": \"хлеб\", \"quantity\": 3, \"price\": 500, \"date\": \"2026-11-02\"},\n    {\"client\": \"Алия\", \"product\": \"чай\", \"quantity\": 1, \"price\": 1200, \"date\": \"2026-11-03\"},\n    {\"client\": \"Жанна\", \"product\": \"сыр\", \"quantity\": 2, \"price\": 1800, \"date\": \"2026-11-04\"},\n    {\"client\": \"Мирас\", \"product\": \"чай\", \"quantity\": 4, \"price\": 1200, \"date\": \"2026-11-05\"},\n    {\"client\": \"Алия\", \"product\": \"хлеб\", \"quantity\": 2, \"price\": 500, \"date\": \"2026-11-06\"},\n    {\"client\": \"Жанна\", \"product\": \"чай\", \"quantity\": 1, \"price\": 1200, \"date\": \"2026-11-07\"},\n    {\"client\": \"Алия\", \"product\": \"сыр\", \"quantity\": 1, \"price\": 1800, \"date\": \"2026-11-08\"},\n    {\"client\": \"Мирас\", \"product\": \"хлеб\", \"quantity\": 1, \"price\": 500, \"date\": \"2026-11-09\"},\n    {\"client\": \"Жанна\", \"product\": \"чай\", \"quantity\": 2, \"price\": 1200, \"date\": \"2026-11-10\"},\n    {\"client\": \"Алия\", \"product\": \"чай\", \"quantity\": 3, \"price\": 1200, \"date\": \"2026-11-11\"},\n    {\"client\": \"Мирас\", \"product\": \"сыр\", \"quantity\": 1, \"price\": 1800, \"date\": \"2026-11-12\"},\n]\nrevenue = 0\nfor order in orders:\n    revenue += order[\"quantity\"] * order[\"price\"]\nprint(revenue)\n# Вывод: 25800",
                "explanation": "В каждой строке заказа стоимость умножается на количество и добавляется к общей сумме."
            },
            {
                "title": "Уникальные клиенты и дорогие заказы",
                "code": "orders = [\n    {\"client\": \"Алия\", \"quantity\": 2, \"price\": 2000},\n    {\"client\": \"Мирас\", \"quantity\": 1, \"price\": 2500},\n    {\"client\": \"Алия\", \"quantity\": 1, \"price\": 4000},\n    {\"client\": \"Жанна\", \"quantity\": 4, \"price\": 1000},\n    {\"client\": \"Мирас\", \"quantity\": 1, \"price\": 500},\n]\nclients = {order[\"client\"] for order in orders}\nexpensive = [order for order in orders if order[\"quantity\"] * order[\"price\"] > 3000]\nprint(len(clients), len(expensive))\n# Вывод: 3 3",
                "explanation": "Множество удаляет повторяющиеся имена, comprehension фильтрует записи."
            }
        ],
        "tasks": [
            {
                "question": "Этап 1. Напишите функцию общей выручки для списка orders.",
                "hint": "Для каждого заказа умножьте quantity на price.",
                "answer": [
                    "def total_revenue(orders):\n    total = 0\n    for order in orders:\n        total += order[\"quantity\"] * order[\"price\"]\n    return total",
                    "def total_revenue(orders):\n    amounts = [order[\"quantity\"] * order[\"price\"] for order in orders]\n    return sum(amounts)"
                ]
            },
            {
                "question": "Этап 2. Посчитайте выручку по каждому клиенту.",
                "hint": "Словарь накапливает сумму по ключу client.",
                "answer": [
                    "def revenue_by_client(orders):\n    totals = {}\n    for order in orders:\n        client = order[\"client\"]\n        totals[client] = totals.get(client, 0) + order[\"quantity\"] * order[\"price\"]\n    return totals",
                    "def variable_1(variable_2):\n    variable_3 = {}\n    for variable_4 in variable_2:\n        variable_5 = variable_4['client']\n        variable_3[variable_5] = variable_3.get(variable_5, 0) + variable_4['quantity'] * variable_4['price']\n    return variable_3"
                ]
            },
            {
                "question": "Этап 3. Найдите три товара с наибольшим количеством проданных единиц.",
                "hint": "Сначала накопите количество по товару, затем отсортируйте пары.",
                "answer": [
                    "def top_products(orders):\n    totals = {}\n    for order in orders:\n        product = order[\"product\"]\n        totals[product] = totals.get(product, 0) + order[\"quantity\"]\n    return sorted(totals.items(), key=lambda item: item[1], reverse=True)[:3]",
                    "def variable_1(variable_2):\n    variable_3 = {}\n    for variable_4 in variable_2:\n        variable_5 = variable_4['product']\n        variable_3[variable_5] = variable_3.get(variable_5, 0) + variable_4['quantity']\n    return sorted(variable_3.items(), key=lambda variable_6: variable_6[1], reverse=True)[:3]"
                ]
            },
            {
                "question": "Этап 4. Верните заказы, чья стоимость выше порога.",
                "hint": "Стоимость заказа равна quantity умножить на price.",
                "answer": [
                    "def above_threshold(orders, threshold):\n    return [order for order in orders if order[\"quantity\"] * order[\"price\"] > threshold]",
                    "def variable_1(variable_2, variable_3):\n    return [variable_4 for variable_4 in variable_2 if variable_4['quantity'] * variable_4['price'] > variable_3]"
                ]
            },
            {
                "question": "Этап 5. Верните множество уникальных клиентов.",
                "hint": "Создайте set из значений поля client.",
                "answer": [
                    "clients = {order[\"client\"] for order in orders}",
                    "variable_1 = {variable_2['client'] for variable_2 in variable_3}"
                ]
            },
            {
                "question": "Этап 6. Сформируйте строку таблицы с колонками «товар» и «сумма».",
                "hint": "Используйте ширину поля в f-строке.",
                "answer": [
                    "def row(product, amount):\n    return f\"{product:<16}{amount:>12.2f}\"",
                    "def variable_1(variable_2, variable_3):\n    return f'{variable_2:<16}{variable_3:>12.2f}'"
                ]
            }
        ]
    },
    {
        "title": "Выбор структуры данных: list, tuple, dict, set",
        "theory": "Выбирайте структуру по задаче. list хранит упорядоченный изменяемый набор и подходит для последовательности записей. tuple фиксирует небольшую группу связанных значений. dict связывает ключ с полями или быстрым доступом по имени, set хранит уникальные значения и удобен для проверки принадлежности.\n\nПроверка наличия в set или dict обычно быстрее, чем последовательный поиск в длинном list. Ловушка: поверхностная копия внешней структуры не копирует вложенные списки и словари. Глубокая копия копирует и вложенные объекты, но требует отдельного осознанного решения и обычно не нужна для простых данных.",
        "examples": [
            {
                "title": "Одна запись в разных структурах",
                "code": "names = [\"Алия\", \"Мирас\"]\npoint = (10, 20)\nprices = {\"чай\": 1200, \"хлеб\": 500}\nunique_letters = set(\"ананас\")\nprint(names[0], point[1], prices[\"чай\"], len(unique_letters))\n# Вывод: Алия 20 1200 3",
                "explanation": "Список хранит порядок, кортеж — пару координат, словарь — цену по ключу, множество — уникальные буквы."
            },
            {
                "title": "Поверхностная копия вложенных данных",
                "code": "original = [[1, 2], [3, 4]]\nshallow = original.copy()\nshallow[0].append(9)\nprint(original[0])\n# Вывод: [1, 2, 9]",
                "explanation": "Внешний список новый, но вложенная строка списка осталась общей."
            }
        ],
        "tasks": [
            {
                "question": "Создайте словарь телефонной книги так, чтобы имя было ключом, а телефон — значением.",
                "hint": "Для поиска по имени используйте отображение ключ → значение.",
                "answer": [
                    "phonebook = {}",
                    "phonebook = dict()"
                ]
            },
            {
                "question": "Напишите функцию, которая проверяет, входят ли все теги tags в разрешённый набор allowed.",
                "hint": "Создайте множество разрешённых значений и проверьте каждый тег циклом.",
                "answer": [
                    "def is_allowed(tags, allowed):\n    allowed_set = set(allowed)\n    for tag in tags:\n        if tag not in allowed_set:\n            return False\n    return True",
                    "def is_allowed(tags, allowed):\n    allowed_set = set(allowed)\n    return set(tags).issubset(allowed_set)"
                ]
            },
            {
                "question": "Напишите безопасное получение зарплаты сотрудника по имени; если имени нет, верните 0.",
                "hint": "Используйте get с запасным числом.",
                "answer": [
                    "def salary_of(salaries, name):\n    return salaries.get(name, 0)",
                    "def salary_of(salaries, name):\n    if name in salaries:\n        return salaries[name]\n    return 0"
                ]
            },
            {
                "question": "Почему поверхностная копия внешнего списка не отделяет вложенные списки?",
                "hint": "Копируется только внешний контейнер.",
                "answer": "вложенные объекты остаются общими"
            }
        ]
    },
    {
        "title": "Отладка: ищем баги в программах с коллекциями",
        "theory": "Начинайте с traceback: последняя строка называет исключение, а ближайшая строка кода показывает место сбоя. IndexError часто означает неправильный индекс списка, KeyError — отсутствующий ключ, TypeError с NoneType — попытку вызвать метод у None, ValueError — неудачное преобразование или недопустимое значение.\n\nДля пошаговой проверки используйте breakpoint(). В отладчике n выполняет следующую строку, c продолжает выполнение, p выражение показывает значение, q завершает сеанс. Сначала воспроизведите ошибку на маленьком примере, затем проверьте пустую коллекцию и отсутствующий ключ.",
        "examples": [
            {
                "title": "Поиск IndexError",
                "code": "values = [4, 8, 12]\nindex = 0\ntry:\n    while index <= len(values):\n        print(values[index])\n        index += 1\nexcept IndexError:\n    print(\"IndexError\")\n# Вывод:\n# 4\n# 8\n# 12\n# IndexError",
                "explanation": "Последний допустимый индекс равен len(values) - 1."
            },
            {
                "title": "Пошаговая проверка",
                "code": "def average(values):\n    breakpoint()\n    return sum(values) / len(values)\n\nprint(average([2, 4]))\n# Вывод: 3.0",
                "explanation": "В отладчике проверьте values командой p values, затем n и c."
            }
        ],
        "tasks": [
            {
                "question": "Исправьте цикл, который обращается к values[len(values)].",
                "hint": "Для индексов нужен диапазон от 0 до длины не включая её.",
                "answer": [
                    "for index in range(len(values)):\n    print(values[index])",
                    "for value in values:\n    print(value)"
                ]
            },
            {
                "question": "Код читает data[\"city\"], но ключ иногда отсутствует. Исправьте безопасно.",
                "hint": "Используйте get с понятным значением по умолчанию.",
                "answer": [
                    "city = data.get(\"city\", \"не указан\")",
                    "variable_1 = variable_2.get('city', 'не указан')"
                ]
            },
            {
                "question": "Функция load_data вернула None, а код вызывает result.append(x). Добавьте проверку.",
                "hint": "Сначала обработайте отсутствие результата.",
                "answer": [
                    "if result is None:\n    result = []\nresult.append(x)",
                    "if variable_1 is None:\n    variable_1 = []\nvariable_1.append(variable_2)"
                ]
            },
            {
                "question": "int(text) вызывает ValueError. Добавьте обработку неправильного ввода.",
                "hint": "Перехватите именно ValueError.",
                "answer": [
                    "try:\n    number = int(text)\nexcept ValueError:\n    number = 0",
                    "try:\n    variable_1 = int(variable_2)\nexcept ValueError:\n    variable_1 = 0"
                ]
            },
            {
                "question": "При отладке вы хотите перейти к следующей строке без входа в функцию. Какая команда?",
                "hint": "Одна буква pdb.",
                "answer": "n"
            },
            {
                "question": "Словарь нельзя изменять при обходе items(). Перепишите удаление отрицательных значений безопасно.",
                "hint": "Сначала соберите ключи, затем удаляйте их отдельным циклом.",
                "answer": [
                    "to_delete = [key for key, value in data.items() if value < 0]\nfor key in to_delete:\n    del data[key]",
                    "variable_1 = [variable_2 for variable_2, variable_3 in variable_4.items() if variable_3 < 0]\nfor variable_2 in variable_1:\n    del variable_4[variable_2]"
                ]
            },
            {
                "question": "Какими командами pdb перейти дальше, продолжить, посмотреть значение и выйти?",
                "hint": "Назовите команды по порядку: next, continue, print, quit.",
                "answer": "n, c, p, q"
            }
        ]
    },
    {
        "title": "Тренажёр-марафон: «Смешанные задачи»",
        "theory": "Здесь встречаются циклы, строки, списки, словари, функции, comprehensions и try/except. Перед решением выпишите вход, результат и крайние случаи. В задачах уровня B соедините два знакомых приёма; в уровне C спроектируйте алгоритм и разбейте его на функции.\n\nПроверяйте пустой ввод, ноль, отрицательное значение и повторяющиеся элементы. Если условие не уточняет порядок результата, укажите это в решении. Не используйте библиотечный метод, который подменяет главный приём конкретной задачи.",
        "examples": [
            {
                "title": "Подсчёт слов и фильтр",
                "code": "def long_words(text, minimum):\n    words = text.lower().split()\n    counts = {}\n    for word in words:\n        counts[word] = counts.get(word, 0) + 1\n    selected = [word for word in words if len(word) >= minimum]\n    return counts, selected\n\ncounts, selected = long_words(\"чай хлеб чай\", 4)\nprint(counts[\"чай\"], counts[\"хлеб\"], selected[0])\n# Вывод: 2 1 хлеб",
                "explanation": "Функция соединяет split, словарь частот и фильтр comprehension."
            },
            {
                "title": "Безопасная сумма чисел",
                "code": "def sum_text_values(text):\n    total = 0\n    for part in text.split():\n        try:\n            total += float(part)\n        except ValueError:\n            continue\n    return total\n\nprint(sum_text_values(\"10 -2.5 abc 4\"))\n# Вывод: 11.5",
                "explanation": "Нечисловая часть пропускается, а отрицательное дробное число учитывается."
            }
        ],
        "tasks": [
            {
                "question": "A1. Верните только слова длиной не меньше minimum.",
                "hint": "Разделите строку и отфильтруйте comprehension-ом.",
                "answer": [
                    "def long_words(text, minimum):\n    return [word for word in text.split() if len(word) >= minimum]",
                    "def variable_1(variable_2, variable_3):\n    return [variable_4 for variable_4 in variable_2.split() if len(variable_4) >= variable_3]"
                ]
            },
            {
                "question": "A2. Подсчитайте сумму целых чисел списка; неверные строки пропустите.",
                "hint": "Преобразуйте каждую строку внутри try/except ValueError.",
                "answer": [
                    "def safe_sum(parts):\n    total = 0\n    for part in parts:\n        try:\n            total += int(part)\n        except ValueError:\n            continue\n    return total",
                    "def variable_1(variable_2):\n    variable_3 = 0\n    for variable_4 in variable_2:\n        try:\n            variable_3 += int(variable_4)\n        except ValueError:\n            continue\n    return variable_3"
                ]
            },
            {
                "question": "A3. Верните первый символ, который встречается в строке ровно один раз.",
                "hint": "Сначала посчитайте частоты, затем пройдите исходную строку.",
                "answer": [
                    "def first_unique(text):\n    counts = {}\n    for symbol in text:\n        counts[symbol] = counts.get(symbol, 0) + 1\n    for symbol in text:\n        if counts[symbol] == 1:\n            return symbol\n    return None",
                    "def variable_1(variable_2):\n    variable_3 = {}\n    for variable_4 in variable_2:\n        variable_3[variable_4] = variable_3.get(variable_4, 0) + 1\n    for variable_4 in variable_2:\n        if variable_3[variable_4] == 1:\n            return variable_4\n    return None"
                ]
            },
            {
                "question": "B1. Удалите из списка отрицательные числа, сохранив порядок остальных.",
                "hint": "Создайте новый список по условию.",
                "answer": [
                    "def non_negative(numbers):\n    return [number for number in numbers if number >= 0]",
                    "def variable_1(variable_2):\n    return [variable_3 for variable_3 in variable_2 if variable_3 >= 0]"
                ]
            },
            {
                "question": "B2. Сгруппируйте слова по длине в словарь длина → список слов.",
                "hint": "Для каждого слова создайте список в словаре при первом появлении длины.",
                "answer": [
                    "def by_length(words):\n    result = {}\n    for word in words:\n        result.setdefault(len(word), []).append(word)\n    return result",
                    "def variable_1(variable_2):\n    variable_3 = {}\n    for variable_4 in variable_2:\n        variable_3.setdefault(len(variable_4), []).append(variable_4)\n    return variable_3"
                ]
            },
            {
                "question": "B3. Преобразуйте строку чисел в список float; плохие значения пропустите.",
                "hint": "Используйте цикл и обработку ValueError.",
                "answer": [
                    "def parse_numbers(text):\n    values = []\n    for part in text.split():\n        try:\n            values.append(float(part))\n        except ValueError:\n            pass\n    return values",
                    "def variable_1(variable_2):\n    variable_3 = []\n    for variable_4 in variable_2.split():\n        try:\n            variable_3.append(float(variable_4))\n        except ValueError:\n            pass\n    return variable_3"
                ]
            },
            {
                "question": "C1. Найдите два разных числа, сумма которых равна target; верните пару значений или None.",
                "hint": "Переберите пары вложенными циклами и не используйте один элемент дважды.",
                "answer": [
                    "def find_pair(numbers, target):\n    for i in range(len(numbers)):\n        for j in range(i + 1, len(numbers)):\n            if numbers[i] + numbers[j] == target:\n                return numbers[i], numbers[j]\n    return None",
                    "def variable_1(variable_2, variable_3):\n    for variable_4 in range(len(variable_2)):\n        for variable_5 in range(variable_4 + 1, len(variable_2)):\n            if variable_2[variable_4] + variable_2[variable_5] == variable_3:\n                return (variable_2[variable_4], variable_2[variable_5])\n    return None"
                ]
            },
            {
                "question": "C2. Подсчитайте продажи по категории и верните категорию с наибольшей суммой.",
                "hint": "Сначала накопите суммы в словаре, затем найдите максимум.",
                "answer": [
                    "def best_category(rows):\n    totals = {}\n    for row in rows:\n        category = row[\"category\"]\n        totals[category] = totals.get(category, 0) + row[\"amount\"]\n    return max(totals, key=totals.get) if totals else None",
                    "def variable_1(variable_2):\n    variable_3 = {}\n    for variable_4 in variable_2:\n        variable_5 = variable_4['category']\n        variable_3[variable_5] = variable_3.get(variable_5, 0) + variable_4['amount']\n    return max(variable_3, key=variable_3.get) if variable_3 else None"
                ]
            },
            {
                "question": "C3. Прочитайте строки до конца ввода, пропустите пустые и верните их число.",
                "hint": "Обработайте EOFError и проверяйте strip().",
                "answer": [
                    "def count_non_empty_input():\n    count = 0\n    while True:\n        try:\n            text = input()\n        except EOFError:\n            break\n        if text.strip():\n            count += 1\n    return count",
                    "def variable_1():\n    variable_2 = 0\n    while True:\n        try:\n            variable_3 = input()\n        except EOFError:\n            break\n        if variable_3.strip():\n            variable_2 += 1\n    return variable_2"
                ]
            },
            {
                "question": "C4. Проверьте, что все скобки в строке круглые и правильно закрыты.",
                "hint": "Используйте счётчик баланса; отрицательное значение означает лишнюю закрывающую скобку.",
                "answer": [
                    "def balanced(text):\n    balance = 0\n    for symbol in text:\n        if symbol == \"(\":\n            balance += 1\n        elif symbol == \")\":\n            balance -= 1\n            if balance < 0:\n                return False\n    return balance == 0",
                    "def variable_1(variable_2):\n    variable_3 = 0\n    for variable_4 in variable_2:\n        if variable_4 == '(':\n            variable_3 += 1\n        elif variable_4 == ')':\n            variable_3 -= 1\n            if variable_3 < 0:\n                return False\n    return variable_3 == 0"
                ]
            }
        ]
    },
    {
        "title": "Тренажёр: «Задачи с собеседований Junior»",
        "theory": "Решайте задачи изученными циклами и структурами данных. Для каждой запишите примеры входа и результата, включая пустой набор, один элемент и повторения. Сначала выберите простую структуру данных, затем объясните, зачем она нужна.\n\nВ этой подборке важны аккуратные границы и порядок. Two Sum должен использовать разные позиции; первый неповторяющийся символ возвращается в исходном порядке; скобки проверяются слева направо. Для выпрямления рассматривается один уровень вложенности.",
        "examples": [
            {
                "title": "Two Sum через словарь",
                "code": "def two_sum(numbers, target):\n    seen = {}\n    for index, number in enumerate(numbers):\n        needed = target - number\n        if needed in seen:\n            return seen[needed], index\n        seen[number] = index\n    return None\n\nprint(two_sum([2, 7, 11], 9))\n# Вывод: (0, 1)",
                "explanation": "Словарь запоминает уже встреченные числа и их индексы."
            },
            {
                "title": "Проверка скобок балансом",
                "code": "def valid_parentheses(text):\n    balance = 0\n    for symbol in text:\n        if symbol == \"(\":\n            balance += 1\n        elif symbol == \")\":\n            balance -= 1\n            if balance < 0:\n                return False\n    return balance == 0\n\nprint(valid_parentheses(\"(()())\"))\n# Вывод: True",
                "explanation": "Баланс не должен становиться отрицательным и должен закончиться нулём."
            }
        ],
        "tasks": [
            {
                "question": "1. Two Sum. Верните индексы двух разных элементов, сумма которых равна target.",
                "hint": "Можно перебрать пары; другой вариант хранит уже встреченные значения в словаре.",
                "answer": [
                    "def two_sum(numbers, target):\n    for i in range(len(numbers)):\n        for j in range(i + 1, len(numbers)):\n            if numbers[i] + numbers[j] == target:\n                return i, j\n    return None",
                    "def two_sum(numbers, target):\n    seen = {}\n    for i, value in enumerate(numbers):\n        if target - value in seen:\n            return seen[target - value], i\n        seen[value] = i\n    return None"
                ]
            },
            {
                "question": "2. Проверьте, являются ли строки анаграммами без учёта регистра и пробелов.",
                "hint": "Сравните отсортированные нормализованные символы или частоты.",
                "answer": [
                    "def anagram(a, b):\n    a = a.replace(\" \", \"\").lower()\n    b = b.replace(\" \", \"\").lower()\n    return sorted(a) == sorted(b)",
                    "def anagram(a, b):\n    def counts(text):\n        result = {}\n        for char in text.replace(\" \", \"\").lower():\n            result[char] = result.get(char, 0) + 1\n        return result\n    return counts(a) == counts(b)"
                ]
            },
            {
                "question": "3. Найдите первый неповторяющийся символ строки; если такого нет, верните None.",
                "hint": "Считайте символы, затем снова пройдите исходную строку.",
                "answer": [
                    "def first_unique(text):\n    counts = {}\n    for char in text:\n        counts[char] = counts.get(char, 0) + 1\n    for char in text:\n        if counts[char] == 1:\n            return char\n    return None",
                    "def variable_1(variable_2):\n    variable_3 = {}\n    for variable_4 in variable_2:\n        variable_3[variable_4] = variable_3.get(variable_4, 0) + 1\n    for variable_4 in variable_2:\n        if variable_3[variable_4] == 1:\n            return variable_4\n    return None"
                ]
            },
            {
                "question": "4. Проверьте правильность последовательности круглых скобок.",
                "hint": "Баланс не может стать отрицательным и должен завершиться нулём.",
                "answer": [
                    "def valid(text):\n    balance = 0\n    for char in text:\n        if char == \"(\":\n            balance += 1\n        elif char == \")\":\n            balance -= 1\n            if balance < 0:\n                return False\n    return balance == 0",
                    "def variable_1(variable_2):\n    variable_3 = 0\n    for variable_4 in variable_2:\n        if variable_4 == '(':\n            variable_3 += 1\n        elif variable_4 == ')':\n            variable_3 -= 1\n            if variable_3 < 0:\n                return False\n    return variable_3 == 0"
                ]
            },
            {
                "question": "5. Разверните порядок слов, сохранив сами слова.",
                "hint": "Разделите строку, пройдите части с конца и соедините.",
                "answer": [
                    "def reverse_words(text):\n    words = text.split()\n    result = []\n    for index in range(len(words) - 1, -1, -1):\n        result.append(words[index])\n    return \" \".join(result)",
                    "def reverse_words(text):\n    words = text.split()\n    words.reverse()\n    return \" \".join(words)"
                ]
            },
            {
                "question": "6. Верните список значений, которые встречаются больше одного раза, без повторов в ответе.",
                "hint": "Используйте множества seen и duplicates.",
                "answer": [
                    "def duplicates(values):\n    seen = set()\n    repeated = set()\n    for value in values:\n        if value in seen:\n            repeated.add(value)\n        seen.add(value)\n    return list(repeated)",
                    "def variable_1(variable_2):\n    variable_3 = set()\n    variable_4 = set()\n    for variable_5 in variable_2:\n        if variable_5 in variable_3:\n            variable_4.add(variable_5)\n        variable_3.add(variable_5)\n    return list(variable_4)"
                ]
            },
            {
                "question": "7. Слейте два отсортированных списка в один отсортированный.",
                "hint": "Сравнивайте элементы двумя индексами, затем добавьте остаток.",
                "answer": [
                    "def merge(a, b):\n    result = []\n    i = j = 0\n    while i < len(a) and j < len(b):\n        if a[i] <= b[j]:\n            result.append(a[i]); i += 1\n        else:\n            result.append(b[j]); j += 1\n    result.extend(a[i:]); result.extend(b[j:])\n    return result",
                    "def variable_1(variable_2, variable_3):\n    variable_4 = []\n    variable_5 = variable_6 = 0\n    while variable_5 < len(variable_2) and variable_6 < len(variable_3):\n        if variable_2[variable_5] <= variable_3[variable_6]:\n            variable_4.append(variable_2[variable_5])\n            variable_5 += 1\n        else:\n            variable_4.append(variable_3[variable_6])\n            variable_6 += 1\n    variable_4.extend(variable_2[variable_5:])\n    variable_4.extend(variable_3[variable_6:])\n    return variable_4"
                ]
            },
            {
                "question": "8. Верните top_k самых частых слов; при равенстве допустим любой порядок.",
                "hint": "Сначала подсчитайте частоты словаря, затем отсортируйте пары по значению.",
                "answer": [
                    "def top_k(text, k):\n    counts = {}\n    for word in text.lower().split():\n        counts[word] = counts.get(word, 0) + 1\n    ordered = sorted(counts.items(), key=lambda item: item[1], reverse=True)\n    return [word for word, count in ordered[:k]]",
                    "def variable_1(variable_2, variable_3):\n    variable_4 = {}\n    for variable_5 in variable_2.lower().split():\n        variable_4[variable_5] = variable_4.get(variable_5, 0) + 1\n    variable_6 = sorted(variable_4.items(), key=lambda variable_7: variable_7[1], reverse=True)\n    return [variable_5 for variable_5, variable_8 in variable_6[:variable_3]]"
                ]
            },
            {
                "question": "9. Разверните список списков на один уровень двумя циклами.",
                "hint": "Два цикла проходят внешние и внутренние элементы.",
                "answer": [
                    "def flatten(rows):\n    result = []\n    for row in rows:\n        for value in row:\n            result.append(value)\n    return result",
                    "def flatten(rows):\n    return [value for row in rows for value in row]"
                ]
            },
            {
                "question": "10. Реализуйте FizzBuzz от 1 до n.",
                "hint": "Сначала проверяйте делимость на 15, затем на 3 и 5.",
                "answer": [
                    "def fizzbuzz(n):\n    result = []\n    for number in range(1, n + 1):\n        if number % 15 == 0: result.append(\"FizzBuzz\")\n        elif number % 3 == 0: result.append(\"Fizz\")\n        elif number % 5 == 0: result.append(\"Buzz\")\n        else: result.append(str(number))\n    return result",
                    "def variable_1(variable_2):\n    variable_3 = []\n    for variable_4 in range(1, variable_2 + 1):\n        if variable_4 % 15 == 0:\n            variable_3.append('FizzBuzz')\n        elif variable_4 % 3 == 0:\n            variable_3.append('Fizz')\n        elif variable_4 % 5 == 0:\n            variable_3.append('Buzz')\n        else:\n            variable_3.append(str(variable_4))\n    return variable_3"
                ]
            }
        ]
    },
    {
        "title": "Практика: «Крестики-нолики в консоли»",
        "theory": "Храните поле как список из трёх строк-списков. Сначала научитесь печатать поле, затем принимайте координаты строки и столбца и проверяйте диапазон и занятость клетки. После каждого хода проверяйте строки, столбцы и две диагонали.\n\nИгра заканчивается победой или ничьей, когда свободных клеток не осталось. Не меняйте поле до проверки ввода. В бонусе бот получает список свободных координат и выбирает одну через random.choice; для пустого списка ход не делается.",
        "examples": [
            {
                "title": "Печать поля",
                "code": "board = [[\" \", \" \", \" \"], [\" \", \" \", \" \"], [\" \", \" \", \" \"]]\nfor row_index, row in enumerate(board):\n    print(f\" {row[0]} | {row[1]} | {row[2]} \")\n    if row_index < 2:\n        print(\"---+---+---\")\n# Вывод:\n#    |   |   \n# ---+---+---\n#    |   |   \n# ---+---+---\n#    |   |   ",
                "explanation": "Каждая строка печатается с разделителями, а горизонтальная линия появляется между строками."
            },
            {
                "title": "Проверка победы",
                "code": "def has_won(board, mark):\n    for row in board:\n        if row[0] == row[1] == row[2] == mark:\n            return True\n    for column in range(3):\n        if board[0][column] == board[1][column] == board[2][column] == mark:\n            return True\n    return board[0][0] == board[1][1] == board[2][2] == mark or board[0][2] == board[1][1] == board[2][0] == mark\n\nboard = [[\"X\", \"X\", \"X\"], [\" \", \"O\", \" \"], [\"O\", \" \", \"O\"]]\nprint(has_won(board, \"X\"))\n# Вывод: True",
                "explanation": "Победа проверяется по строкам, столбцам и обеим диагоналям."
            }
        ],
        "tasks": [
            {
                "question": "Этап 1. Создайте поле 3×3 и функцию печати.",
                "hint": "Используйте три отдельные строки списка.",
                "answer": [
                    "def new_board():\n    return [[\" \", \" \", \" \"], [\" \", \" \", \" \"], [\" \", \" \", \" \"]]\n\ndef show(board):\n    for row in board:\n        print(\"|\".join(row))",
                    "def variable_1():\n    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]\n\ndef variable_2(variable_3):\n    for variable_4 in variable_3:\n        print('|'.join(variable_4))"
                ]
            },
            {
                "question": "Этап 2. Проверьте координаты 0–2 и запретите занятые клетки.",
                "hint": "Верните False без изменения поля, если ход некорректен.",
                "answer": [
                    "def make_move(board, row, column, mark):\n    if not 0 <= row < 3 or not 0 <= column < 3:\n        return False\n    if board[row][column] != \" \":\n        return False\n    board[row][column] = mark\n    return True",
                    "def variable_1(variable_2, variable_3, variable_4, variable_5):\n    if not 0 <= variable_3 < 3 or not 0 <= variable_4 < 3:\n        return False\n    if variable_2[variable_3][variable_4] != ' ':\n        return False\n    variable_2[variable_3][variable_4] = variable_5\n    return True"
                ]
            },
            {
                "question": "Этап 3. Напишите проверку победы по строкам, столбцам и диагоналям.",
                "hint": "Проверяйте три равных символа, не считая пробел победой.",
                "answer": [
                    "def won(board, mark):\n    for i in range(3):\n        if board[i][0] == board[i][1] == board[i][2] == mark:\n            return True\n        if board[0][i] == board[1][i] == board[2][i] == mark:\n            return True\n    return board[0][0] == board[1][1] == board[2][2] == mark or board[0][2] == board[1][1] == board[2][0] == mark",
                    "def variable_1(variable_2, variable_3):\n    for variable_4 in range(3):\n        if variable_2[variable_4][0] == variable_2[variable_4][1] == variable_2[variable_4][2] == variable_3:\n            return True\n        if variable_2[0][variable_4] == variable_2[1][variable_4] == variable_2[2][variable_4] == variable_3:\n            return True\n    return variable_2[0][0] == variable_2[1][1] == variable_2[2][2] == variable_3 or variable_2[0][2] == variable_2[1][1] == variable_2[2][0] == variable_3"
                ]
            },
            {
                "question": "Этап 4. Определите ничью, если свободных клеток не осталось и победителя нет.",
                "hint": "Проверьте, что каждая клетка занята.",
                "answer": [
                    "def is_draw(board):\n    for row in board:\n        for cell in row:\n            if cell == \" \":\n                return False\n    return True",
                    "def variable_1(variable_2):\n    for variable_3 in variable_2:\n        for variable_4 in variable_3:\n            if variable_4 == ' ':\n                return False\n    return True"
                ]
            },
            {
                "question": "Этап 5. Соберите игровой цикл для двух игроков: ввод, ход, победа или ничья.",
                "hint": "После каждого успешного хода меняйте X на O и обратно.",
                "answer": [
                    "def play(board):\n    mark = \"X\"\n    while True:\n        row = int(input())\n        column = int(input())\n        if not make_move(board, row, column, mark):\n            continue\n        show(board)\n        if won(board, mark):\n            print(\"Победил\", mark)\n            break\n        if is_draw(board):\n            print(\"Ничья\")\n            break\n        mark = \"O\" if mark == \"X\" else \"X\"",
                    "def variable_1(variable_2):\n    variable_3 = 'X'\n    while True:\n        variable_4 = int(input())\n        variable_5 = int(input())\n        if not variable_6(variable_2, variable_4, variable_5, variable_3):\n            continue\n        variable_7(variable_2)\n        if variable_8(variable_2, variable_3):\n            print('Победил', variable_3)\n            break\n        if variable_9(variable_2):\n            print('Ничья')\n            break\n        variable_3 = 'O' if variable_3 == 'X' else 'X'"
                ]
            },
            {
                "question": "Этап 6. Добавьте бота, который выбирает свободную клетку случайно.",
                "hint": "Соберите свободные координаты вложенным циклом и проверьте пустой список.",
                "answer": [
                    "import random\n\ndef bot_move(board):\n    free_cells = []\n    for row in range(3):\n        for column in range(3):\n            if board[row][column] == \" \":\n                free_cells.append((row, column))\n    if not free_cells:\n        return False\n    row, column = random.choice(free_cells)\n    board[row][column] = \"O\"\n    return True",
                    "import random\n\ndef variable_1(variable_2):\n    variable_3 = []\n    for variable_4 in range(3):\n        for variable_5 in range(3):\n            if variable_2[variable_4][variable_5] == ' ':\n                variable_3.append((variable_4, variable_5))\n    if not variable_3:\n        return False\n    variable_4, variable_5 = random.choice(variable_3)\n    variable_2[variable_4][variable_5] = 'O'\n    return True"
                ]
            }
        ]
    },
    {
        "title": "Итоговый проект блока: «Викторина с таблицей рекордов»",
        "theory": "Разделите проект на quiz.py и storage.py. Вопрос храните словарём с текстом, вариантами ответа, правильным ответом и категорией; файл questions.json содержит список таких записей. Игровой модуль выбирает несколько вопросов, проверяет ввод и начисляет очки.\n\nstorage.py загружает и сохраняет records.json. При отсутствии файла начните с пустой таблицы, при повреждённом JSON сообщите об ошибке и не затирайте исходные данные. Покажите топ-5, добавьте фильтр по категории и вынесите запуск под if __name__ == \"__main__\". Проверьте неверный ввод, пустую категорию, пустой файл и повторный запуск.",
        "examples": [
            {
                "title": "questions.json и выбор вопросов",
                "code": "import random\nrandom.seed(2)\n\nquestions = [\n    {\"question\": \"Сколько будет 2 + 3?\", \"options\": [\"4\", \"5\", \"6\"], \"answer\": \"5\", \"category\": \"математика\"},\n    {\"question\": \"Какой тип хранит целые числа?\", \"options\": [\"int\", \"str\", \"bool\"], \"answer\": \"int\", \"category\": \"python\"},\n]\nselected = random.sample(questions, k=2)\nfor item in selected:\n    print(item[\"question\"])\n# Вывод:\n# Сколько будет 2 + 3?\n# Какой тип хранит целые числа?",
                "explanation": "random.sample выбирает неповторяющиеся вопросы, а словарь хранит поля вопроса."
            },
            {
                "title": "Хранение рекордов",
                "code": "import json\nfrom pathlib import Path\n\nRECORDS = Path(\"records.json\")\n\ndef load_records():\n    if not RECORDS.exists():\n        return []\n    try:\n        return json.loads(RECORDS.read_text(encoding=\"utf-8\"))\n    except json.JSONDecodeError:\n        raise ValueError(\"Файл рекордов повреждён\")\n\ndef top_five(records):\n    return sorted(records, key=lambda record: record[\"score\"], reverse=True)[:5]\n\nrecords = [{\"name\": \"Алия\", \"score\": 12}, {\"name\": \"Мирас\", \"score\": 15}, {\"name\": \"Жанна\", \"score\": 8}]\nfor item in top_five(records):\n    print(item[\"score\"])\n# Вывод:\n# 15\n# 12\n# 8",
                "explanation": "Загрузка не маскирует повреждённый JSON, а топ сортируется по score."
            }
        ],
        "tasks": [
            {
                "question": "Этап 1. Опишите вопрос словарём с question, options, answer и category.",
                "hint": "Проверьте, что правильный ответ входит в варианты.",
                "answer": [
                    "def make_question(question, options, answer, category):\n    if answer not in options:\n        raise ValueError(\"Ответ должен быть среди вариантов\")\n    return {\"question\": question, \"options\": options, \"answer\": answer, \"category\": category}",
                    "def variable_1(variable_2, variable_3, variable_4, variable_5):\n    if variable_4 not in variable_3:\n        raise ValueError('Ответ должен быть среди вариантов')\n    return {'question': variable_2, 'options': variable_3, 'answer': variable_4, 'category': variable_5}"
                ]
            },
            {
                "question": "Этап 2. Загрузите questions.json и выберите случайные N вопросов из категории.",
                "hint": "Отфильтруйте список, затем используйте random.sample; проверьте размер выборки.",
                "answer": [
                    "def choose_questions(questions, category, count):\n    import random\n    available = [item for item in questions if item[\"category\"] == category]\n    return random.sample(available, min(count, len(available)))",
                    "def variable_1(variable_2, variable_3, variable_4):\n    import random\n    variable_5 = [variable_6 for variable_6 in variable_2 if variable_6['category'] == variable_3]\n    return random.sample(variable_5, min(variable_4, len(variable_5)))"
                ]
            },
            {
                "question": "Этап 3. Проведите игру, проверьте выбор и подсчитайте очки.",
                "hint": "Сравнивайте ответ без учёта регистра; неверный номер варианта не должен завершать программу.",
                "answer": [
                    "def play(questions):\n    score = 0\n    for item in questions:\n        print(item[\"question\"])\n        answer = input(\"Ответ: \").strip()\n        if answer.lower() == item[\"answer\"].lower():\n            score += 1\n    return score",
                    "def variable_1(variable_2):\n    variable_3 = 0\n    for variable_4 in variable_2:\n        print(variable_4['question'])\n        variable_5 = input('Ответ: ').strip()\n        if variable_5.lower() == variable_4['answer'].lower():\n            variable_3 += 1\n    return variable_3"
                ]
            },
            {
                "question": "Этап 4. Сохраните имя, очки и дату в records.json и покажите топ-5.",
                "hint": "Храните рекорды списком словарей и сортируйте по score.",
                "answer": [
                    "def add_record(records, name, score, played_at):\n    records.append({\"name\": name, \"score\": score, \"date\": played_at})\n    records.sort(key=lambda record: record[\"score\"], reverse=True)\n    return records[:5]",
                    "def variable_1(variable_2, variable_3, variable_4, variable_5):\n    variable_2.append({'name': variable_3, 'score': variable_4, 'date': variable_5})\n    variable_2.sort(key=lambda variable_6: variable_6['score'], reverse=True)\n    return variable_2[:5]"
                ]
            },
            {
                "question": "Этап 5. Добавьте выбор категории и обработку отсутствующих и повреждённых файлов.",
                "hint": "FileNotFoundError можно трактовать как пустую историю; JSONDecodeError лучше показать отдельно.",
                "answer": [
                    "def load_json(path):\n    import json\n    try:\n        with open(path, encoding=\"utf-8\") as file:\n            return json.load(file)\n    except FileNotFoundError:\n        return []\n    except json.JSONDecodeError as error:\n        raise ValueError(\"Некорректный JSON\") from error",
                    "def variable_1(variable_2):\n    import json\n    try:\n        with open(variable_2, encoding='utf-8') as variable_3:\n            return json.load(variable_3)\n    except FileNotFoundError:\n        return []\n    except json.JSONDecodeError as error:\n        raise ValueError('Некорректный JSON') from variable_4"
                ]
            },
            {
                "question": "Этап 6. Добавьте точку запуска, таймер или статистику по категориям.",
                "hint": "Запуск меню поместите под стандартную проверку имени модуля.",
                "answer": [
                    "if __name__ == \"__main__\":\n    main()",
                    "if variable_1 == '__main__':\n    variable_2()"
                ]
            }
        ]
    }
]

BLOCK = {
    "level": Course.LEVEL_BLOCK_04,
    "block_title": "Блок 4. Циклы, строки и коллекции",
    "lessons": LESSONS,
}
