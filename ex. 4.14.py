class Ship:
    def __init__(self, damage):
        self.damage = damage

    def deal_damage(self):
        print("Object {} inflict {} damage.".format(self.__class__.__name__, self.damage))


class BattleShip(Ship):
    def __init__(self, damage, special_damage):
        super().__init__(damage)
        self.special_damage = special_damage

    def deal_special_damage(self):
        print("Object {} inflict {} damage.".format(self.__class__.__name__, self.special_damage))


class BigBattleShip(BattleShip):
    def __init__(self, damage, special_damage, bomb_damage):
        super().__init__(damage, special_damage)
        self.bomb_damage = bomb_damage

    def deal_special_damage_twice(self):
        self.deal_special_damage()
        self.deal_special_damage()

    def use_bomb(self):
        print("Object {} inflict {} damage.".format(self.__class__.__name__, self.bomb_damage))


class CargoShip(Ship):
    def __init__(self, damage, capacity):
        super().__init__(damage)
        self.capacity = capacity

    def transport(self):
        print("Object {} transport {} cargo.".format(self.__class__.__name__, self.capacity))


a = Ship(10)
a.deal_damage()

print(" ")

b = BattleShip(12, 14)
b.deal_damage()
b.deal_special_damage()

print(" ")

c = BigBattleShip(13, 16, 50)
c.deal_damage()
c.deal_special_damage_twice()
c.use_bomb()

print(" ")

d = CargoShip(8, 10)
d.deal_damage()
d.transport()
