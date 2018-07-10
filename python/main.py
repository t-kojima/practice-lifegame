import random
import sys
import time
from lifegame import LifeGame


def init():
    base_x = 25
    base_y = 25
    game = LifeGame(base_x, base_y)
    for x in range(base_x):
        for y in range(base_y):
            game.set_alive(y, x, random.randint(0, 1))
    return game


def console_out(game):
    sys.stdout.write("\r")
    for y in range(game.y):
        for x in range(game.x):
            sys.stdout.write("■ " if game.board[y][x] else "□ ")
        sys.stdout.write("\n")
    sys.stdout.flush()
    print()
    time.sleep(1)


def main():
    game = init()
    while(True):
        console_out(game)
        game.next_generation()


if __name__ == "__main__":
    main()
