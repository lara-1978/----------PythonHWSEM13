# Задача 2. Чат
# Реализуйте программу - чат, в котором могут участвовать сразу несколько человек, то
# есть программа может работать одновременно для нескольких пользователей.
# При запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
# 1. Посмотреть текущий текст чата
# 2. Отправить сообщение (затем вводит сообщение). Действия запрашиваются бесконечно.

class Chat:
    def __init__(self, filename='text.txt'):
        self.filename = filename

    def message(self):
        try:
            with open(self.filename, mode='r', encoding='utf-8') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('Служебное сообщение: Пока ни чего нет\n')

    def add_message(self, name, message):
        with open(self.filename, mode='a', encoding='utf-8') as file:
            file.write(f'{name}: {message}\n')

    def run(self):
        name = input("Как вас зовут? ")
        while True:
            print('"Чтобы увидеть текущий текст чата введите 1, чтобы написать сообщение введите 2')
            response = input("Введите 1 или 2: ")
            if response == '1':
                self.message()
            elif response == '2':
                new_message = input("Введите сообщение: ")
                self.add_message(name, new_message)
            else:
                print("Неизвестная команда\n")

if __name__ == "__main__":
    chat = Chat()
    chat.run()






