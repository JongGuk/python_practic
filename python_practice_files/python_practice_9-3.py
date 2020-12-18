class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # member parameter
        self.hp = hp
        self.damage = damage
        print("{0} unit is created.".format(self.name))
        print("hp {0}, damage {1}".format(self.hp, self.damage))

# 객체 (Unit 클래스의 인스턴스)
marine1 = Unit("marine", 40, 5)
marine2 = Unit("marine", 40, 5)
tank = Unit("tank", 40, 5)
marine3 = Unit("marine", 40, 5)

wraith1 = Unit("wraith", 80, 5)

print("Unit name : {0}, damage: {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("control wraith", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} is clocking state.".format(wraith2.name))