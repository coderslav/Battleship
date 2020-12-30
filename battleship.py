from random import randrange
from random import choice
class BattleField:
    def __init__(self, hide=False):
        self.hide = hide
        self.field = [[' ', '1', '2', '3', '4', '5', '6'], ['1', 'O', 'O', 'O', 'O', 'O', 'O'],
                      ['2', 'O', 'O', 'O', 'O', 'O', 'O'], ['3', 'O', 'O', 'O', 'O', 'O', 'O'],
                      ['4', 'O', 'O', 'O', 'O', 'O', 'O'], ['5', 'O', 'O', 'O', 'O', 'O', 'O'],
                      ['6', 'O', 'O', 'O', 'O', 'O', 'O']]
        self.radar = [[' ', '1', '2', '3', '4', '5', '6'], ['1', 'O', 'O', 'O', 'O', 'O', 'O'],
                      ['2', 'O', 'O', 'O', 'O', 'O', 'O'], ['3', 'O', 'O', 'O', 'O', 'O', 'O'],
                      ['4', 'O', 'O', 'O', 'O', 'O', 'O'], ['5', 'O', 'O', 'O', 'O', 'O', 'O'],
                      ['6', 'O', 'O', 'O', 'O', 'O', 'O']]

    def get_field(self):
        return self.field

    def get_radar(self):
        return self.radar

    def draw_field(self):
        field_str = ""
        for row in self.field:
            field_str += f"\n "+" | ".join(row)+" |"
        if self.hide:
            field_str = field_str.replace("■", "O")
        return field_str

    def draw_radar(self):
        field_str = ""
        for row in self.radar:
            field_str += f"\n "+" | ".join(row)+" |"
        if self.hide:
            field_str = field_str.replace("■", "O")
        return field_str

    def shoot(self, x, y):
        pass

    def busy(self):
        pass


class Ships:
    def __init__(self, position, hp, orientation):
        self.position = position
        self.hp = hp
        self.orientation = orientation

    def ship_init(self, ):
        pass


b = BattleField()
print(b.draw_field())


