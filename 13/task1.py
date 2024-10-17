#   Задание 1. Карма
# Один буддист-программист решил создать свой симулятор жизни, в котором
# нужно набрать 500 очков кармы (это константа), чтобы достичь просветления.
# Каждый день вызывается специальная функция one_day(), которая возвращает
# количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений:
# ● KillError,
# ● DrunkError,
# ● CarCrashError,
# ● GluttonyError,
# ● DepressionError.
# (Исключения нужно создать самостоятельно, при помощи наследования от Exception.)
# Напишите такую программу. Функцию оберните в бесконечный цикл, выход из
# которого возможен только при накоплении кармы до уровня константы.
# Исключения обработайте и запишите в отдельный лог karma.log.
# По итогу у вас может быть примерно такая структура программы:
# открываем файл

# цикл по набору кармы
# try
#  карма += one_day()
# except(ы) с указанием классов исключений, которые нужно поймать, добавляем запись в файл закрываем файл.

import random

KARMA = 500

class KillError(Exception):
    def __init__(self):
        super().__init__("Гибель. Вы погибли!")

class DrunkError(Exception):
    def __init__(self):
        super().__init__("Пьянство. Пьянству бой!")

class CarCrashError(Exception):
    def __init__(self):
        super().__init__("Авария! Вы попали в аварию!")

class GluttonyError(Exception):
    def __init__(self):
        super().__init__("Вы переели! Соблюдайте режим питания!")

class DepressionError(Exception):
    def __init__(self):
        super().__init__("Депрессия! Вы впали в депрессию")

def one_day():
    day_karma = random.randint(1, 7)
    if random.randint(1, 10) == 5:
        exception = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
        raise exception
    return day_karma

def main():
    karma = 0
    with open('karma.log', mode='w', encoding='utf-8') as f_logger:
        while True:
            try:
                karma += one_day()
                f_logger.write(f'Карма за день: {karma}\n')  # Записываем текущее значение кармы
            except Exception as e:
                f_logger.write(f'{e}\n')

            if karma >= KARMA:
                f_logger.write("Вы достигли Кармы!\n")
                break

    print("Вы достигли Кармы!")  # Выводим сообщение в консоль

if __name__ == "__main__":
    main()  # Вызов функции main
