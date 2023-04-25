from abc import ABC, abstractmethod


class Race(ABC):

    @property
    def pwr_race_modifier(self) -> int:
        return 0

    @property
    def agi_race_modifier(self) -> int:
        return 0

    @property
    def con_race_modifier(self) -> int:
        return 0

    @property
    def int_race_modifier(self) -> int:
        return 0

    @property
    def wis_race_modifier(self) -> int:
        return 0

    @abstractmethod
    def race_skill(self):
        return NotImplementedError('Пропиши особенность расы')


class Human(Race):

    @property
    def pwr_race_modifier(self) -> int:
        return 1

    @property
    def agi_race_modifier(self) -> int:
        return 1

    @property
    def con_race_modifier(self) -> int:
        return 1

    @property
    def int_race_modifier(self) -> int:
        return 1

    @property
    def wis_race_modifier(self) -> int:
        return 1

    def race_skill(self):
        return 'Адоптация: опыт +1%'


class Dwarf(Race):

    @property
    def pwr_race_modifier(self) -> int:
        return 3

    @property
    def con_race_modifier(self) -> int:
        return 2

    @property
    def wis_race_modifier(self) -> int:
        return 1

    @property
    def agi_race_modifier(self) -> int:
        return -1

    def race_skill(self):
        return 'Жадность: цена продажи +10%'


class Elf(Race):

    @property
    def pwr_race_modifier(self) -> int:
        return -3

    @property
    def agi_race_modifier(self) -> int:
        return 4

    @property
    def int_race_modifier(self) -> int:
        return 3

    @property
    def wis_race_modifier(self) -> int:
        return 1

    def race_skill(self):
        return 'Красота: быстро располагает к себе'
