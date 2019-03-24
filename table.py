import itertools
from ui import draw_table_once


class Table(object):
    def __init__(self, size=15, checkers_in_row_to_win=5, dsimagin_style_row=None):
        self.size = size
        self.checkers_in_row_to_win = checkers_in_row_to_win

        # NxN
        self.table = [[0 for _ in range(size)] for _ in range(size)]
        if dsimagin_style_row:
            self.from_dsimagin_style(dsimagin_style_row)

    def is_free(self, x, y):
        return self.table[x][y] == 0

    def go(self, x, y, color):
        if not (0 <= x < self.size and 0 <= y <= self.size):
            raise IndexError('cell ({},{}) is not in {}x{}'.format(x, y, self.size, self.size))
        if not self.is_free(x, y):
            raise IndexError('cell ({},{}) is not free, table:\n{}\n'.format(x, y, self.table))
        self.table[x][y] = color

    def get_winner(self):
        directions = ((1, 0), (0, 1), (1, 1), (-1, 1))
        for i, j in itertools.product(range(self.size), repeat=2):
            if self.get(i, j) == 0:
                continue
            for dir_i, dir_j in directions:
                equals = True
                for t in range(self.checkers_in_row_to_win):
                    if self.get(i + t * dir_i, j + t * dir_j) != self.get(i, j):
                        equals = False
                if equals:
                    return self.get(i, j)

        return 0  # draw

    def get(self, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.table[x][y]
        return 0

    def from_dsimagin_style(self, game):
        game = game.split()[1:]
        color = 1
        for cell in game:
            self.go(*self.translate_chess_coordinates(cell), color)
            color *= -1

    @staticmethod
    def translate_chess_coordinates(coord):
        x = ord(coord[0]) - ord('a')
        if x > ord('i') - ord('a'):
            x -= 1
        y = int(coord[1:]) - 1
        return x, y


with open('../data/prepared_data.renju') as f:
    content = f.readlines()
content = [x.strip() for x in content]

t = Table()
t.from_dsimagin_style(content[56])
draw_table_once(t.table)
