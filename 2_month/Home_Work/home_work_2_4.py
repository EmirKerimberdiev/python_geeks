from random import randint, choice, random

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if type(hero) == Berserk and self.defence != hero.ability:
                    blocked = choice([5, 10])
                    hero.blocked_damage = blocked
                    hero.health -= (self.damage - blocked)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes):
        pass

    def attack(self, boss):
        boss.health -= self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes):
        coefficient = randint(2, 5)
        boss.health -= self.damage * coefficient
        print(f'Warrior {self.name} hit critically {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage, boosting_point):
        super().__init__(name, health, damage, 'BOOST')
        self._boosting_point = boosting_point

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self and hero.name != 'Kitagava':
                hero.damage += self._boosting_point


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_AND_REVERT')
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} damage.')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points

class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'SUPER_HEAL')

    def apply_super_power(self, boss, heroes):
        life_points = 0
        for hero in heroes:
            if hero.health == 0 and life_points == 0:
                hero.health = self.health
                self.health = 0
                life_points = 1

class Hacker(Hero):
    def __init__(self, name, health, damage, hack_points):
        super().__init__(name, health, damage, 'HACK')
        self.__hack_points = hack_points

    def apply_super_power(self, boss, heroes):
        hero = choice(heroes)
        global round_number
        if round_number % 2 == 0:
            boss.health -= self.__hack_points
            hero.health += self.__hack_points
            print(f'Hacker {self.name} heal {hero.name} for {self.__hack_points} damage.')

class Samurai(Hero):
    def __init__(self, name, health, damage, surikens):
        super().__init__(name, health, damage, 'SURIKEN')
        self.__surikens = surikens

    def apply_super_power(self, boss, heroes):
        suriken = randint(1, 2)
        if suriken == 1:
            boss.health -= self.__surikens
            print(f'Samurai {self.name} hit {boss.name} with {self.__surikens} surikens.')
        else:
            boss.health += self.__surikens
            print(f'Samurai {self.name} heal {boss.name} for {self.__surikens} health points.')

class King(Hero):
    def __init__(self, name, health, damage, one_hit):
        super().__init__(name, health, damage, 'SURIKEN')
        self.__one_hit = one_hit

    def apply_super_power(self, boss, heroes):
        list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        hit = choice(list_num)
        if hit == 1:
            boss.health -= self.__one_hit
            print(f'King {self.name} called Saitama and hit {boss.name} with {self.__one_hit} damage.')

round_number = 0


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and hero.ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def show_statistics(boss, heroes):
    print(f'\n---------- ROUND {round_number} ----------')
    print(boss)
    for hero in heroes:
        print(hero)
    print("\n")


def start_game():
    boss = Boss(name='Elena', health=1500, damage=50)

    warrior_1 = Warrior(name='Ahiles', health=280, damage=10)
    warrior_2 = Warrior(name='Helios', health=290, damage=15)
    magic = Magic(name='Potter', health=260, damage=10, boosting_point=2)
    berserk = Berserk(name='Guts', health=240, damage=5)
    doc = Medic(name='Merlin', health=200, damage=5, heal_points=15)
    assistant = Medic(name='Marin', health=300, damage=5, heal_points=5)
    witcher = Witcher(name='Kitagava', health=300, damage=0)
    hacker = Hacker(name='Tanjiro', health=250, damage=15, hack_points=20)
    samurai = Samurai(name='Inoske', health=240, damage=10, surikens=10)
    king = King(name='Goku', health=300, damage=0, one_hit=1000000)

    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant, witcher, hacker, samurai, king]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()