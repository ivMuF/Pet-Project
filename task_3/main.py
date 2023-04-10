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


class Race:
    """ Класс. Описывает бонусы от расы """
    @staticmethod
    def elf() -> int:
        """ Раса эльф добавляет +2 к ловкости """
        return 2

    @staticmethod
    def human() -> int:
        """ Раса человек добавляет +2 к силе """
        return 2


class Profession:
    """ Класс. Описывает бонусы от профессий """

    @staticmethod
    def mag() -> int:
        """ Профессия маг добавляет +3 к интеллекту """
        return 3

    @staticmethod
    def archer() -> int:
        """ Профессия маг добавляет +3 к ловкости """
        return 3

    @staticmethod
    def warrior() -> int:
        """ Профессия маг добавляет +3 к телосложению """
        return 3


class Player(Race):
    """ Класс. Описывающий игрока """

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.power: int = 10
        self.agility: int = 10
        self.constitution: int = 10
        self.intellect: int = 10
        self.wisdom: int = 10
        self.charisma: int = 10
        self.race: str = ''
        self.profession: str = ''

    def __str__(self) -> str:
        return '\n{}: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}'.format(
            'Имя', self.name,
            'Сила', self.power,
            'Ловкость', self.agility,
            'Телосложение', self.constitution,
            'Интеллект', self.intellect,
            'Мудрость', self.wisdom,
            'Харизма', self.charisma,
            'Раса', self.race,
            'Класс', self.profession
        )

    def change_race(self, race: str) -> None:
        if race == 'elf':
            self.race = 'Эльф'
            self.agility += Race.elf()
        elif race == 'human':
            self.race = 'Человек'
            self.power += Race.human()

    def change_profession(self, profession: str) -> None:
        if profession == 'mag':
            self.profession = 'Маг'
            self.intellect += Profession.mag()
        elif profession == 'archer':
            self.profession = 'Лучник'
            self.agility += Profession.archer()
        elif profession == 'warrior':
            self.profession = 'Воин'
            self.constitution += Profession.warrior()


def create_player() -> Player:
    name = input('Введите Имя персонажа: ')
    race = input('Введите Расу персонажа(elf, human): ')
    profession = input('Введите Класс персонажа(mag, archer, warrior): ')
    user = Player(name=name)
    user.change_race(race=race)
    user.change_profession(profession=profession)

    return user


if __name__ == '__main__':
    print(create_player())
