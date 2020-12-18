class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # member parameter
        self.hp = hp
        self.damage = damage
        print("{0} unit is created.".format(self.name))
        print("hp {0}, damage {1}".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name # member parameter
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : attack enemy to {1} direction. [damage {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} damaged.".format(self.name, damage))
        self.hp -= damage
        print("{0} : current hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : is destoyed.".format(self.name))

firebat1 = AttackUnit("firebat", 50, 16)
firebat1.attack("north")
firebat1.damaged(25)
firebat1.damaged(25)