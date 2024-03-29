# Задание состоит в том, чтобы создать генератор стандартной настольной игры (бросаем кубик,
# двигаемся на выброшенное количество клеток). Условия задания:
# 1. Карта генерируется случайным образом. Длина (кол-во клеток) - варируется от min_cell_count до max_cell_count
# 2. Клетки должны содержать события (на этапе генерирования карты игры, в ячейку помещается событие, которое
# будет одинаково работать для всех игроков). Тут как фантазия позволит.
# Для примера (необходимый минимум), сделать события
# бонусного передвижения на сколько клеток вперед. Ну и наоборот штраф с уходом назад.
# 3. Побеждает тот, кто первый доберется. Количество игроков произвольное.
# 4. Сделать имитацию кубика.
# 5. Логгировать передвижения игроков. (тут можешь заморочиться и сделать разными цветами, но не обязательно)
# 6. Частота событий на игровом поле тоже должна выноситься в отдельную переменную.
import random
from typing import Optional, List, Any
from abc import ABC, abstractmethod


class Event(ABC):

    @abstractmethod
    def return_num(self, num):
        pass


class PositiveEvent(Event):

    def return_num(self, num: int) -> int:
        return num


class NegativeEvent(Event):

    def return_num(self, num: int) -> int:
        return -1 * num


class Cell:
    """ Класс, описывающий клетку """

    def __init__(self, index: int) -> None:
        self.__index: int = index
        self.__event: Any = self.set_event()

    def __str__(self) -> str:
        return f'{self.__index}'

    def get(self) -> int:
        return self.__index

    def get_event(self) -> Any:
        return self.__event

    @staticmethod
    def set_event() -> Any:
        if random.randint(1, 100) < 65:
            num = random.randint(1, 5)
            events = [PositiveEvent(), NegativeEvent()]
            return random.choice(events).return_num(num)


class Field:
    """ Класс, описывающий игровое поле """

    def __init__(self, min_cell_count, max_cell_count) -> None:
        self.__cells: List[Cell] = [Cell(index=j) for j in range(1, random.randint(min_cell_count, max_cell_count))]

    def __str__(self) -> str:
        return f'Длина игрового поля: {len(self.__cells)}'

    def __len__(self):
        return len(self.__cells)

    def get_cells(self) -> List[Cell]:
        return self.__cells


class Player:
    """ Класс, описывающий игрока """

    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__num_cell: int = 0

    def __str__(self) -> str:
        return self.__name

    def get_cell(self) -> int:
        return self.__num_cell

    def set_cell(self, num: int) -> None:
        self.__num_cell = num

    def game_cube(self) -> None:
        num_cube = random.randint(1, 6)
        print('На кубике выпало', num_cube)
        self.__num_cell += num_cube


class Game:
    """ Класс, описывающий логику игры """

    def __init__(self) -> None:
        self.players: Optional[List[Player]] = None
        self.game_field: Optional[Field] = None
        self.win = False
        self.finish_list = []

    def setup(self, num_player: int, min_cell: int, max_cell: int) -> None:
        self.players: List[Player] = [Player(name=input('Введите имя игрока: ')) for _ in range(num_player)]
        self.game_field: Field = Field(min_cell_count=min_cell, max_cell_count=max_cell)

    def field_check(self, num: int) -> bool:
        if num >= len(self.game_field):
            return True
        else:
            return False

    def move(self, gamer: Player) -> None:
        if self.field_check(gamer.get_cell()):
            print(gamer, 'дошёл до конца!')
            self.finish_list.append(gamer)
            self.win = True
        else:
            print(gamer, 'передвигается на клетку', gamer.get_cell())

    def events(self, cell_num: int, gamer: Player) -> None:
        event_list = self.game_field.get_cells()
        if cell_num < len(event_list):
            event = event_list[cell_num - 1].get_event()
            if event:
                if event > 0:
                    gamer.set_cell(cell_num + event)
                    print('Случилось что-то хорошее, '
                          f'передвигайтесь на {event} клеток вперед')
                elif event < 0:
                    gamer.set_cell(cell_num + event)
                    print('Случилось что-то плохое '
                          f'передвигайтесь на {abs(event)} клеток назад')

                print(gamer, 'передвигается на клетку', gamer.get_cell())

    def play(self) -> None:
        print('\nНачинается игра')
        print(self.game_field)

        while True:
            for player in self.players:
                print('\nХодит игрок:', player)
                player.game_cube()
                self.move(gamer=player)
                self.events(cell_num=player.get_cell(), gamer=player)

            if self.win:
                print('\nПобедители:')
                for player in self.finish_list:
                    print(player)
                break

    def run(self):
        self.setup(num_player=2, min_cell=15, max_cell=30)
        self.play()


Game().run()
