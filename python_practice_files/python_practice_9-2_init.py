class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} unit is created.".format(self.name))
        print("hp {0}, damage {1}".format(self.hp, self.damage))

# 객체 (Unit 클래스의 인스턴스)
marine1 = Unit("marine", 40, 5)
marine2 = Unit("marine", 40, 5)
tank = Unit("tank", 40, 5)
marine3 = Unit("marine", 40, 5)