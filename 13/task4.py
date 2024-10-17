# Задача 4. Счетчик Очков в Игрe
# Создайте класс GameScore для отслеживания очков игрока. В этом классе
# должны быть методы для добавления и уменьшения очков. Однако:
# ● Очки не могут быть отрицательными.
# ● Если игрок пытается добавить больше очков, чем 1000, должно быть
# выброшено исключение ScoreLimitExceededError.
# Создайте пользовательское исключение ScoreLimitExceededError.

# 

class ScoreLimitExceededError(Exception):
    def __init__(self):
        super().__init__("Очки не могут быть больше 1000.")  # Закрывающая скобка была здесь


class GameScore:
    def __init__(self):
        self.score = 0

    def add_score(self, points):
        if self.score + points > 1000:
            raise ScoreLimitExceededError()
        self.score += points

    def subtract_score(self, points):
        if self.score - points < 0:
            raise ValueError("Очки не могут быть отрицательными.")
        self.score -= points


# Пример использования
game_score = GameScore()
try:
    # Добавляем 500 очков
    game_score.add_score(500)
    print(f"Текущий счет: {game_score.score}")

    # Если напишем 600, вызовем исключение
    game_score.add_score(600)
except ScoreLimitExceededError as e:
    print(e)
except ValueError as e:
    print(e)

try:
    # Пытаемся вычесть больше очков, чем есть
    game_score.subtract_score(600)
except ValueError as e:
    print(e)

# Проверка работы метода subtract_score
try:
    game_score.subtract_score(100)
    print(f"Текущий счет после вычитания: {game_score.score}")
except ValueError as e:
    print(e)



   
        

