from random import randint


class GameException(Exception):
    pass


class OutException(GameException):
    @staticmethod
    def message():
        return "Не стреляйте за поле!"


class UsedException(GameException):
    @staticmethod
    def message():
        return "Вы уже стреляли в эту клетку!"


class WrongShipException(GameException):
    pass


class BattleField:
    def __init__(self, hide=False):
        self.hide = hide
        self.field = [[' ', '1', '2', '3', '4', '5', '6'], ['1', 'O', 'O', 'O', 'O', 'O', 'O'],
                      ['2', 'O', 'O', 'O', 'O', 'O', 'O'], ['3', 'O', 'O', 'O', 'O', 'O', 'O'],
                      ['4', 'O', 'O', 'O', 'O', 'O', 'O'], ['5', 'O', 'O', 'O', 'O', 'O', 'O'],
                      ['6', 'O', 'O', 'O', 'O', 'O', 'O']]
        self.busy = []
        self.ships = []
        self.count = 0

    @staticmethod
    def out_of_field(z):
        return not ((0 <= z.x < 6) and (0 <= z.y < 6))

    def add_ship(self, ship):

        for i in ship.dots:
            if self.out_of_field(i) or i in self.busy:
                raise WrongShipException()
        for i in ship.dots:
            self.field[i.x][i.y] = Cell.ship_cell
            self.busy.append(i)

        self.ships.append(ship)
        self.non_ships_zone(ship)

    def non_ships_zone(self, ship, z=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                coord = Cell(d.x + dx, d.y + dy)
                if not (self.out_of_field(coord)) and coord not in self.busy:
                    if z:
                        self.field[coord.x][coord.y] = Cell.miss_cell
                    self.busy.append(coord)

    def shot(self, z):
        if self.out_of_field(z):
            raise OutException()

        if z in self.busy:
            raise UsedException()

        self.busy.append(z)

        for ship in self.ships:
            if z in ship.dots:
                ship.lives -= 1
                self.field[z.x][z.y] = Cell.destroyed_ship
                if ship.lives == 0:
                    self.count += 1
                    self.non_ships_zone(ship, z=True)
                    print("Корабль потоплен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[z.x][z.y] = Cell.miss_cell
        print("Мимо!")
        return False

    def reset(self):
        self.busy = []

    def draw_field(self):
        field_str = ""
        for row in self.field:
            field_str += f"\n "+" | ".join(row)+" |"
        if self.hide:
            field_str = field_str.replace("■", "O")
        return field_str


class Cell:
    empty_cell = 'O'
    ship_cell = '■'
    destroyed_ship = 'X'
    miss_cell = '•'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Ships:
    def __init__(self, position, size, orientation):
        self.size = size
        self.hp = size
        self.x, self.y = position
        self.orientation = orientation
        self.busy = []
        self.ships = []

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.size):
            coord_x = self.x
            coord_y = self.y

            if self.orientation == 0:
                coord_x += i

            elif self.orientation == 1:
                coord_y += i

            ship_dots.append(Cell(coord_x, coord_y))

        return ship_dots

    def shot_reg(self, shot):
        return shot in self.dots


