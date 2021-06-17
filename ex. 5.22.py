class MineralWater:
    def __init__(self, sodium, calcium):
        self.sodium = sodium
        self.calcium = calcium

    def __eq__(self, other):
        if self.sodium == other.sodium and self.calcium == other.calcium:
            return True
        else:
            return False


staropolanka = MineralWater(32.50, 124)
staropolanka2 = MineralWater(32.50, 124)

print(staropolanka.__eq__(staropolanka2))
