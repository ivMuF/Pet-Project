from typing import Any


class Cell:
    """ Класс, описывающий клутку """

    __states = {0: ' ', 1: 'O', 2: 'X'}

    def __init__(self, index: int) -> None:
        self.index = index
        self.__state = 0

    def __str__(self) -> None:
        print(self.index, Cell.__states[self.__state])

    def state_info(self) -> str:
        if self.__state == 0:
            return f'{self.index}'
        else:
            return f'{Cell.__states[self.__state]}'

    def get_state(self) -> int:
        return self.__state

    def set_state(self, num: int) -> None:
        self.__state = num


class Board:
    """ Класс, описывающий игровое поле и логику игры """

    def __init__(self) -> None:
        self.board = [Cell(index=i) for i in range(1, 10)]

    def __str__(self) -> list[Cell]:
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
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.board[each[0]].state_info() == self.board[each[1]].state_info() == self.board[each[2]].state_info():
                return f'Победил: {self.board[each[0]].state_info()}'
        return False


my_board = Board()
count = 0
while True:
    my_board.draw_board()
    if my_board.check_win():
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
