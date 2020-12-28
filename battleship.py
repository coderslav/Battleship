class BattleField:
    def __init__(self,  hide=False):
        self.hide = hide
        self.field = [[' ', '1', '2', '3', '4', '5', '6'], ['1', 'O', 'O', 'O', 'O', 'O', 'O'],
                      ['2', 'O', 'O', 'O', 'O', 'O', 'O'], ['3', 'O', 'O', 'O', 'O', 'O', 'O'],
                      ['4', 'O', 'O', 'O', 'O', 'O', 'O'], ['5', 'O', 'O', 'O', 'O', 'O', 'O'],
                      ['6', 'O', 'O', 'O', 'O', 'O', 'O']]

    def test_print(self, x, y):
        self.field[x][y] = "X"
        return self.field


class Ships:
    def __init__(self, position, hp, orientation):
        self.position = position
        self.hp = hp
        self.orientation = orientation


b = BattleField()
b.test_print(2, 2)
for i in b.field:
    print(i)

