from abc import ABC, abstractmethod


class Race(ABC):

    @property
    def str_race_modifier(self) -> int:
        return 0

    @property
    def agi_race_modifier(self) -> int:
        return 0

    @abstractmethod
    def super_attack(self):
        raise NotImplementedError("Чел пропиши чудо-скилл")

class Human(Race):

    @property
    def str_race_modifier(self) -> int:
        return 2

    # @property
    # def agi_race_modifier(self) -> int:
    #     return -1

    @property
    def super_attack(self):
        return


class Profession(ABC):

    @property
    def str_profession_modifier(self) -> int:
        return 0

    @property
    def agi_profession_modifier(self) -> int:
        return 0

    # Добавь доп. способность


class Archer(Profession):

    @property
    def str_profession_modifier(self) -> int:
        return 6


class Player:
    def __init__(self, strength: int, agility: int, race: Race, profession: Profession):
        self.race = race
        self.profession = profession
        self.init_str = strength
        self.init_agility = agility

    @property
    def strength(self) -> int:
        return self.init_str + self.race.str_race_modifier + self.profession.str_profession_modifier

    @property
    def agility(self) -> int:
        return self.init_agility + self.race.agi_race_modifier + self.profession.agi_profession_modifier


human = Player(100, 100, Human(), Archer())
print(human.strength, human.agility)

