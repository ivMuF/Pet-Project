# В этом задании тебе нужно будет создать конструктор героев для RPG.
# Что-то вроде того, что реализован в играх а-ля NWN.
# Задание, в первую очередь, направлено на закрепление темы наследования и интерфейсов.
# За типизацию тоже буду ебать мозг, так что типизируй правильно, никаких Any.
# Основные требования:
# 1. У героя есть аттрибуты (возьми из DnD). Аттрибуты дают модификаторы, как в DnD.
# 2. Расы дают дополнительные модификаторы к аттрибутам и дополнительные способности (можно любые)
# 3. Классы персонажей делают то же самое - модификаторы аттрибутов и доп. способности
# 4. Реализовать этапы построения можно инпутами.
# 5. Постарайся не бояться ошибиться, делай как тебе это представляется правильным.
# 6. Проверять работоспособность буду сам, не парься над тем, как показать,
#    что условная доп. способность, полученная от класса персонажа, работает и реализована правильно

from race import Race, Human, Dwarf, Elf
from profession import Profession, Warrior, Archer, Mage


class Player:
    """ Класс. Описывающий игрока """

    def __init__(self, name: str, race: Race, profession: Profession) -> None:
        self.name = name
        self.power = 10
        self.agility = 10
        self.constitution = 10
        self.intellect = 10
        self.wisdom = 10
        self.charisma = 10
        self.race = race
        self.profession = profession

    def __str__(self) -> str:
        return f"name: {self.name},{self.power=},{self.agility=},{self.constitution=},{self.intellect=},{self.wisdom=}"

    @property
    def pwr(self) -> int:
        return self.power + self.race.pwr_race_modifier + self.profession.pwr_profession_modifier

    @property
    def agi(self) -> int:
        return self.agility + self.race.agi_race_modifier + self.profession.agi_profession_modifier

    @property
    def con(self) -> int:
        return self.constitution + self.race.con_race_modifier + self.profession.con_profession_modifier

    @property
    def int(self) -> int:
        return self.intellect + self.race.int_race_modifier + self.profession.int_profession_modifier

    @property
    def wis(self) -> int:
        return self.wisdom + self.race.wis_race_modifier + self.profession.wis_profession_modifier


player = Player('Rick', Human(), Warrior())
print(player.pwr, player.agi, player.con, player.int, player.wis)
