from typing import List, Optional


class Cell:
    """ Класс, описывающий клетку """

    STATES = {0: ' ', 1: 'O', 2: 'X'}

    def __init__(self, index: int) -> None:
        self.index = index
        self.__state = 0

    def state_info(self) -> str:
        if self.__state == 0:
            return f'{self.index}'
        return f'{Cell.STATES[self.__state]}'

    @property
    def state(self) -> int:
        return self.__state

    @state.setter
    def state(self, num: int) -> None:
        self.__state = num


class Board:
    """ Класс, описывающий игровое поле и логику игры """

    WIN_COORD = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def __init__(self) -> None:
        self.board = [Cell(index=i) for i in range(1, 10)]

    def __str__(self) -> List[Cell]:
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
        if self.board[num_cell - 1].state == 0:
            self.board[num_cell - 1].state = num_state
        else:
            print('Клетка уже занята')
            player = int(input('Выберите другую Клетку! '))
            self.board_check(num_state=num_state, num_cell=player)

    def check_win(self, pl_1, pl_2) -> bool:
        for each in Board.WIN_COORD:
            if self.board[each[0]].state_info() == self.board[each[1]].state_info() == self.board[each[2]].state_info():
                self.player_win(pl_1, pl_2, self.board[each[0]])
                return True
        return False

    @classmethod
    def player_win(cls, pl_1, pl_2, state) -> None:
        if state == pl_1.get_team():
            print(f'Победитель:\n{pl_1}')
        else:
            print(f'Победитель:\n{pl_2}')


class Player:

    def __init__(self, name: str, team: int) -> None:  # , board: Board
        self.name = name
        self.team = team
        # self.board = board

    def __str__(self) -> str:
        return f'Имя игрока: {self.name}, Команда: {Cell.STATES[self.team]}'

    def get_team(self):
        return self.team

    def get_name(self):
        return self.name

    @classmethod
    def create_first_player(cls):
        return cls(name='Rick', team=1)

    @classmethod
    def create_second_player(cls):
        return cls(name='Morty', team=2)


class Game:
    count = 0

    def __init__(self) -> None:
        self.pl_first: Optional[Player] = None
        self.pl_second: Optional[Player] = None
        self.board: Optional[Board] = None

    def setup(self) -> None:
        self.pl_first = Player.create_first_player()
        self.pl_second = Player.create_second_player()
        self.board = Board()

    def play(self) -> None:
        while True:
            self.board.draw_board()
            if self.board.check_win(pl_1=self.pl_first, pl_2=self.pl_second):
                break
            if Game.count == 9:
                print('Победила: Дружба!')
                break
            elif Game.count % 2 == 0:
                player = int(input(f'{self.pl_first.get_name()} твой ход! '))
                self.board.board_check(num_state=1, num_cell=player)
            else:
                player = int(input(f'{self.pl_second.get_name()} твой ход! '))
                self.board.board_check(num_state=2, num_cell=player)
            Game.count += 1

    def run(self):
        self.setup()
        self.play()


Game.run(Game())
