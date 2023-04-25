from abc import ABC, abstractmethod


class Profession(ABC):

    @property
    def pwr_profession_modifier(self) -> int:
        return 0

    @property
    def agi_profession_modifier(self) -> int:
        return 0

    @property
    def con_profession_modifier(self) -> int:
        return 0

    @property
    def int_profession_modifier(self) -> int:
        return 0

    @property
    def wis_profession_modifier(self) -> int:
        return 0

    @abstractmethod
    def profession_skill(self):
        return NotImplementedError('Пропиши особенность профессии')


class Warrior(Profession):

    @property
    def pwr_profession_modifier(self) -> int:
        return 2

    @property
    def con_profession_modifier(self) -> int:
        return 2

    @property
    def int_profession_modifier(self) -> int:
        return -1

    def profession_skill(self):
        return 'Персонаж умеет обращаться с одноручным оружием'


class Archer(Profession):

    @property
    def agi_profession_modifier(self) -> int:
        return 3

    def profession_skill(self):
        return 'Персонаж умеет обращаться с луком или арбалетом'


class Mage(Profession):

    @property
    def int_profession_modifier(self) -> int:
        return 2

    @property
    def wis_profession_modifier(self) -> int:
        return 2

    @property
    def pwr_profession_modifier(self) -> int:
        return -1

    def profession_skill(self):
        return 'Персонаж умеет пользоваться магией'
