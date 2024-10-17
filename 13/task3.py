# Задача 3. Счастливое число
# Напишите программу, которая запрашивает у пользователя число до тех пор,
# пока сумма этих чисел не станет больше либо равна 777.
# Каждое введенное число при этом дозаписывается в файл.
# Сделайте так, чтобы перед дозаписью программа с вероятностью 1 к 13
# выбрасывала пользователю случайное исключение и завершалась.

## variant 1
import random


def main():
    total_sum = 0
    filename = 'numbers.log'

    with open(filename, mode='w', encoding='utf-8') as f:
        while total_sum < 777:
            try:
                number = int(input("Введите число: "))
                total_sum += number
                f.write(f'{number}\n')  # Запись числа в файл

                # С вероятностью 1 к 13 выбрасываем исключение
                if random.randint(1, 13) == 1:
                    raise Exception("Случайное исключение! Программа завершена.")

                print(f"Текущая сумма: {total_sum}")

            except ValueError:
                print("Пожалуйста, введите корректное число.")
            except Exception as e:
                print(e)
                break

    print(f"Итоговая сумма: {total_sum}")


if __name__ == "__main__":
    main()







