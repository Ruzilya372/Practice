# TODO здесь писать код

# 1. Класс, который описывает одну клетку поля:
class Cell:
    def __init__(self, number):
        self.number = number
        self.is_occupied = False  # Изначально клетка свободна
        self.pointer = str(number)  # Символ, который отображается (цифра или X/0)

    def __str__(self):
        return self.pointer


# 2. Класс, который описывает поле игры:
class Board:
    def __init__(self):
        # Генерируем 9 клеток
        self.cells = [Cell(number) for number in range(1, 10)]
        # Координаты для проверки победы (индексы клеток)
        self.win_coord = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтали
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикали
            (0, 4, 8), (2, 4, 6)  # диагонали
        )

    def draw_board(self):
        """Метод для красивой отрисовки поля"""
        print("-" * 13)
        for i in range(3):
            print(
                "|", self.cells[0 + i * 3],
                "|", self.cells[1 + i * 3],
                "|", self.cells[2 + i * 3],
                "|"
            )
            print("-" * 13)


# 3. Класс, который описывает поведение игрока:
class Player:
    def __init__(self, name, pointer):
        # У игрока должно быть имя и его символ (X или 0)
        self.name = name
        self.pointer = pointer

    def move(self, board):
        while True:
            try:
                number_cell = int(input(f"{self.name}, ваш ход, в какую клетку ставим {self.pointer}? "))
                if number_cell < 1 or number_cell > 9:
                    print("Введите число от 1 до 9!")
                    continue

                cell = board.cells[number_cell - 1]

                if not cell.is_occupied:
                    cell.is_occupied = True
                    cell.pointer = self.pointer
                    break
                else:
                    print("Эта клетка уже занята!")
            except ValueError:
                print("Пожалуйста, введите число!")


# 4. Класс, который управляет ходом игры:
class Game:
    def __init__(self, player_1, player_2):
        # Инициализирует поле, игроков и счетчик побед.
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = Board()
        self.player_1_wins = 0
        self.player_2_wins = 0
        self.draws = 0
        self.current_player = player_1

    def check_win(self):
        # Проверяет, есть ли победитель на текущем поле, используя self.board.win_coord.
        for coord in self.board.win_coord:
            symbols = [self.board.cells[i].pointer for i in coord]
            if symbols[0] == symbols[1] == symbols[2] and symbols[0] not in "123456789":
                return True
        return False


    def start_one_game(self):
        # Запускает цикл одной игры до победы или ничьей.
        self.board = Board()
        self.current_player = self.player_1
        moves = 0

        while True:
            self.board.draw_board()
            self.current_player.move(self.board)
            moves += 1

            if self.check_win():
                self.board.draw_board()
                print(f"{self.current_player.name} выиграл!")
                if self.current_player == self.player_1:
                    self.player_1_wins += 1
                else:
                    self.player_2_wins += 1
                break

            if moves == 9:
                self.board.draw_board()
                print("Ничья!")
                self.draws += 1
                break

            if self.current_player == self.player_1:
                self.current_player = self.player_2
            else:
                self.current_player = self.player_1


    def start_many_games(self):
        # Основной цикл. Предлагает играть еще раз после окончания одной партии.
        # Выводит общий счет.
        while True:
            self.start_one_game()

            print(f"{self.player_1.name} победил {self.player_1_wins} раз!")
            print(f"{self.player_2.name} победил {self.player_2_wins} раз!")
            print(f"Ничья: {self.draws}")

            while True:
                try:
                    continue_game = int(input("Продолжить игру? 1 - да, 0 - нет: "))
                    if continue_game == 0:
                        print("Игра окончена!")
                        return
                    elif continue_game == 1:
                        break
                    else:
                        print("Введите 1 или 0")
                except ValueError:
                    print("Введите 1 или 0.")
                


# Раскомментируйте код ниже, когда реализуете классы Player и Game

player1 = Player("Вася", "X")
player2 = Player("Петя", "0")

game = Game(player1, player2)
game.start_many_games()
