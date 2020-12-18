from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name # member parameter
        self.hp = hp
        self.speed = speed
        print("{0} Unit is created.".format(name))

    def damaged(self, damage):
        print("{0} : {1} damaged.".format(self.name, damage))
        self.hp -= damage
        print("{0} : current hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : is destoyed.".format(self.name))

    def move(self, location):
        print("[ground unit move]")
        print("{0} : move to {1} direction. [speed {2}]"\
            .format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : attack enemy to {1} direction. [damage {2}]"\
            .format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : Stimpack using. (hp 10 decrease)".format(self.name))
        else:
            print("{0} : Not enough hp.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False
    
    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0} : changing seize mode.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : changing normal mode.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : fly to {1} direction. [speed {2}]"\
            .format(name, location, self.flying_speed))
            
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # ground speed = 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[sky unit move]")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "wraith", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : diable clocking mode.".format(self.name))
            self.clocked = False
        else:
            print("{0} : enable clocking mode.".format(self.name))
            self.clocked = True

def game_start():
    print("[Note] New Game Start.")

def game_over():
    print("Player: gg")
    print("[Player] quit the game.")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 =Tank()
t2 =Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("north")

Tank.seize_developed = True
print("[Note] Tank seize mode has been developed.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("north")

for unit in attack_units:
    unit.damaged(randint(5, 21))

game_over()