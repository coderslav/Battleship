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
        self.field = [['O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O'],
                      ['O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O'],
                      ['O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O']]
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
                ship.hp -= 1
                self.field[z.x][z.y] = Cell.destroyed_ship
                if ship.hp == 0:
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

    def __str__(self):
        field_str = ""
        field_str += "    1   2   3   4   5   6  "
        for i, row in enumerate(self.field):
            field_str += f"\n{i + 1} | " + " | ".join(row) + " |"
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
        self.pos = position
        self.orientation = orientation
        self.busy = []
        self.ships = []

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.size):
            coord_x = self.pos.x
            coord_y = self.pos.y

            if self.orientation == 0:
                coord_x += i

            elif self.orientation == 1:
                coord_y += i

            ship_dots.append(Cell(coord_x, coord_y))

        return ship_dots

    def shot_reg(self, shot):
        return shot in self.dots


class Player:
    def __init__(self, battlefield, enemy_battlefield):
        self.battlefield = battlefield
        self.enemy_battlefield = enemy_battlefield

    def turn(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy_battlefield.shot(target)
                return repeat
            except GameException as x:
                print(x)

    def ask(self):
        raise NotImplementedError()


class AI(Player):
    def ask(self):
        z = Cell(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {z.x + 1} {z.y + 1}")
        return z


class HomoSapiens(Player):
    def ask(self):
        while True:
            coords = input("Ваш ход: ").split()

            if len(coords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = coords

            if not (x.isdigit()) or not (y.isdigit()):
                print("Введите числа!")
                continue

            x, y = int(x), int(y)

            return Cell(x - 1, y - 1)


class Game:
    def __init__(self):
        player = self.random_battlefield()
        computer = self.random_battlefield()
        computer.hid = True

        self.ai = AI(computer, player)
        self.hs = HomoSapiens(player, computer)

    def random_battlefield(self):
        field = None
        while field is None:
            field = self.random_place()
        return field

    def random_place(self):
        ship_lens = [3, 2, 2, 1, 1, 1, 1]
        battlefield = BattleField()
        attempts = 0
        for i in ship_lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ships(Cell(randint(0, 6), randint(0, 6)), i, randint(0, 1))
                try:
                    battlefield.add_ship(ship)
                    break
                except WrongShipException:
                    pass
        battlefield.reset()
        return battlefield

    @staticmethod
    def greetings():
        print("-------------------")

    def loop(self):
        num = 0
        while True:
            print("-" * 20)
            print("Море пользователя:")
            print(self.hs.battlefield)
            print("-" * 20)
            print("Море компьютера:")
            print(self.ai.battlefield)
            if num % 2 == 0:
                print("-" * 20)
                print("Пользователь ходит!")
                repeat = self.hs.turn()
            else:
                print("-" * 20)
                print("Компьютер ходит!")
                repeat = self.ai.turn()
            if repeat:
                num -= 1

            if self.ai.battlefield.count == 7:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.hs.battlefield.count == 7:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greetings()
        self.loop()


g = Game()
g.start()
