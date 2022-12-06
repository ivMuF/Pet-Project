from typing import Any


class Cell:
    """ Класс, описывающий клутку """

    __states = {0: ' ', 1: 'O', 2: 'X'}  # Константы принято задавать капсом

    def __init__(self, index: int) -> None:
        self.index = index
        self.__state = 0

    def __str__(self) -> None:
        print(self.index, Cell.__states[self.__state])  # Ну ваще так делать неправильно.
        # Магический метод стр должен возвращать строку с информацией по классу, а не принтить.
        # Для принта лучше сделать отдельный метод

    def state_info(self) -> str:
        if self.__state == 0:
            return f'{self.index}'
        else: # Можно без else
            return f'{Cell.__states[self.__state]}'

    def get_state(self) -> int:
        return self.__state

    def set_state(self, num: int) -> None:
        self.__state = num


class Board:
    """ Класс, описывающий игровое поле и логику игры """

    def __init__(self) -> None:
        self.board = [Cell(index=i) for i in range(1, 10)]

    def __str__(self) -> list[Cell]: # Лучше юзать List из библиотеке typing
        return self.board

    def draw_board(self) -> None:
        print("-------------")
        for i in range(3):
            print(
                "|", self.board[0 + i * 3].state_info(), "|", self.board[1 + i * 3].state_info(),
                "|", self.board[2 + i * 3].state_info(), "|"
            )
            print("-------------")

    def board_check(self, num_state: int, num_cell: int) -> None:
        if self.board[num_cell - 1].get_state() == 0:
            self.board[num_cell - 1].set_state(num_state)
        else:
            print('Клетка уже занята')
            player = int(input('Выберите другую Клетку! '))
            self.board_check(num_state=num_state, num_cell=player)

    def check_win(self) -> Any:
        # TODO вот тут есть что исправить:
        #  - Зачем каждый раз задавать победные координаты, если их можно вынести в константу?
        #  - Метод check_win по логике должен возвращать bool, а не Any. Если кто-то победил - верни True, а там уже
        #  соответствующий метод
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.board[each[0]].state_info() == self.board[each[1]].state_info() == self.board[each[2]].state_info():
                return f'Победил: {self.board[each[0]].state_info()}'
        return False


my_board = Board()
count = 0
while True:
    # TODO тут тоже есть что исправить:
    #  - Почему флоу игры не сделать классом? С определенными состояниями и аттрибутами?
    #  - Также почему бы не сделать класс игрока, чтобы он был не обезличен, а имел имя,
    #  символ который он ставит на доске. Задача со *: попробуй инициализировать класс игрока с помощью classmethod,
    #  как это можно здесь использовать?
    my_board.draw_board()
    if my_board.check_win(): # TODO согласись выглядит странно (эта строчка и строчка ниже)
        print(my_board.check_win())
        break
    if count == 9:
        print('Победила: Дружба!')
        break
    elif count % 2 == 0:
        player_1 = int(input('Куда ставим "O"? '))
        my_board.board_check(num_state=1, num_cell=player_1)
    else:
        player_2 = int(input('Куда ставим "X"? '))
        my_board.board_check(num_state=2, num_cell=player_2)
    count += 1
