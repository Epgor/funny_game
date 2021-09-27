from random import randint
import os

class Hero:
    def __init__(self):
        self.hp = 100
        self.attack = 10
        self.defence = 10
        self.luck = 10
        self.gold = 20000
        self.exp = 1
        self.next_lvl_exp = 100
        self.lvl = 0

    def travel_event_fight(self, enemy_attack):

        if self.attack <= enemy_attack * 2:
            self.hp -= int((randint(1, 10) + (self.hp / 2) + enemy_attack - self.defence))
            self.gold -= int((randint(1, 10) + (self.gold / 2) + (enemy_attack * 2) - (self.defence * 3)))
            self.exp += (10 * self.luck)
        elif self.attack > enemy_attack * 2:
            self.hp -= (randint(1, 10) + int((self.hp / 5) + enemy_attack - (self.defence * 4) - (self.luck * 3)))
            self.exp += (5 * 10 * self.luck + self.attack)

        # # chujemuje
        #

    def travel_event_gold(self):
        random = randint(1, 100)
        if random < 40:
            self.gold -= randint(1, 40)
            self.exp += random
        else:
            self.gold += randint(40, 100)
            self.exp += (random * self.luck)

    def upgrade_attack(self):
        if self.gold >= self.attack * 100:
            self.gold -= self.attack * 100
            self.attack += 1

    def upgrade_defence(self):
        if self.gold >= self.defence * 100:
            self.gold -= self.defence * 100
            self.defence += 1

    def upgrade_luck(self):
        if self.gold >= self.luck * 100:
            self.gold -= self.luck * 100
            self.luck += 1

    def upgrade_hp(self):
        if self.gold >= self.hp * 100:
            self.gold -= self.hp * 100
            self.defence += 10

    def lvl_up(self):
        self.hp += 10
        self.attack += 1
        self.defence += 1
        self.luck += 1
        self.exp = 1
        self.next_lvl_exp = (((self.lvl + 1) ** 3) * 1000)
        self.lvl += 1
    #
    # def stats(self):
    #     return "HP: " + self.hp + "Attack: " + self.attack + "Defence: " + self.defence + "Luck: " + self.luck + "Gold: " + self.gold + "Level: " + self.lvl + "Experience: " + self.exp + "Next Level: " + self.next_lvl_exp

    def stats(self):
        return f"HP: {self.hp} \nAttack:{self.attack} \nDefence: {self.defence} \nLuck: {self.luck} \nGold: {self.gold}" \
            f" \nLevel: {self.lvl} \nExperience: {self.exp} \nNext Level: {self.next_lvl_exp} \n "

    def heal(self):
        if self.gold > 1000:
            self.hp += int(10 + self.lvl * (self.luck / 10))
            self.gold -= 100 + self.lvl ** 3 - self.luck * 3
            return "You heal"
        else:
            return "Not enough gold!"

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def is_lvl_up(self):
        if not self.is_dead():
            if self.exp >= self.next_lvl_exp:
                return 1
            else:
                return 0

    def exp_bar(self):
        if int(self.exp / (self.next_lvl_exp + 1) * 100) <= 1:
            return 10
        else:
            return int(self.exp / (self.next_lvl_exp + 1) * 100)

    def r_exp(self):
        return self.exp / self.exp + 1

    def Exit(self):
        os._exit(0)

    def r_exp_max(self):
        return self.next_lvl_exp / self.next_lvl_exp + 1 * 100 #sroga rozkmina xD
    # def upgrade_defence(self):ack
    #     if self.gold >= self.defence * 100:
    #         self.gold -= self.defence * 100
    #         self.defence += 1

    def cheat_upgrade(self):
        self.hp += 100
        self.attack += 10
        self.defence += 10
        self.luck += 10
        self.gold += 20000
        self.exp += 999999

    #
    # def degrade(self):
    #     case = randint(2, 4)
    #     if case == 0:
    #         pass
    #     if case == 1:
    #         self.hp += 10
    #     if case == 2:
    #         self.attack += 1
    #     if case == 3:
    #         self.attack += 1
    #     if case == 4:
    #         self.attack += 1
    #     else:
    #         pass


class Warrior(Hero):
    def __init__(self, name, hp, defence, attack, roll_v=0):
        self.hp = hp
        self.name = name
        self.roll_v = roll_v
        self.defence = 3
        self.attack = 2

    def roll(self):
        if self.roll_v > 0:
            return 1
        if self.roll_v == 0:
            return 0
        else:
            return -1

    def __str__(self):
        return "{}({},{},{},{},{})".format(self.__class__.__name__, self.name, self.hp, self.defence, self.attack,
                                           self.roll_v, )

# noinspection PyArgumentList
# my_hero = Warrior('Jon', 10, 0, 0, 1)
# # print(my_hero)
# # print(my_hero.roll())
