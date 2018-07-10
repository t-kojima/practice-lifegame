import copy


class LifeGame():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = [[0 for i in range(x)] for n in range(y)]

    def set_alive(self, y, x, value=1):
        self.board[y][x] = value

    def board(self):
        return self.board

    def next_generation(self):
        clone = copy.deepcopy(self.board)

        def around_alive_cells(y, x):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx != 0 or dy != 0:
                        yield clone[(y + dy) % self.y][(x + dx) % self.x]

        def count_alive(y, x):
            return sum(list(around_alive_cells(y, x)))

        for x in range(self.x):
            for y in range(self.y):
                count = count_alive(y, x)
                if clone[y][x] and (count <= 1 or count >= 4):
                    self.board[y][x] = 0
                if not clone[y][x] and count == 3:
                    self.board[y][x] = 1
