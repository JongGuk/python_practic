class Unit:
    def __init__(self, name, hp, speed):
        self.name = name # member parameter
        self.hp = hp
        self.speed = speed

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

    def damaged(self, damage):
        print("{0} : {1} damaged.".format(self.name, damage))
        self.hp -= damage
        print("{0} : current hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : is destoyed.".format(self.name))

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

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location