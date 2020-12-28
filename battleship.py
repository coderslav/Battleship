class BattleField:
    def __init__(self, size=7, hide=False):
        self.size = size
        self.hide = hide
        self.field = [["O"] * size for _ in range(size)]
        self.field[0][0] = " "
        self.field[0][1] = "1"
        self.field[0][2] = "2"
        self.field[0][3] = "3"
        self.field[0][4] = "4"
        self.field[0][5] = "5"
        self.field[0][6] = "6"
        self.field[1][0] = "1"
        self.field[2][0] = "2"
        self.field[3][0] = "3"
        self.field[4][0] = "4"
        self.field[5][0] = "5"
        self.field[6][0] = "6"

    def test_print(self, x, y):
        self.field[x][y] = "X"
        return self.field


class Ships:
    def __init__(self, position, hp, orientation):
        self.position = position
        self.hp = hp
        self.orientation = orientation


b = BattleField()
b.test_print(1, 1)
for i in b.field:
    print(i)

