# name = "Marine"
# hp = 40
# damage = 5

# print("{0} unit is created.".format(name))
# print("HP {0}, Damage {1}\n".format(hp, damage))

# tank_name = "Tank"
# tank_hp = 150
# tank_damage = 35

# print("{0} unit is created.".format(tank_name))
# print("HP {0}, Damage {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : attack {1} direction enemy. [damage {2}]".format(\
#         name, location, damage))

# attack(name, "north", damage)
# attack(tank_name, "north", tank_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} unit is created.".format(self.name))
        print("hp {0}, damage {1}".format(self.hp, self.damage))

marine1 = Unit("marine", 40, 5)
marine2 = Unit("marine", 40, 5)
tank = Unit("tank", 40, 5)