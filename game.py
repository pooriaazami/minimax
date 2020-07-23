import numpy as np

from node import Node


class Game:
    X_Win_SCORE = 1
    O_WIN_SCORE = -1
    EQUAL_SCORE = 0
    UNKNOWN_SCORE = None

    def __init__(self, board_size: int = 3):
        self.__board = Node(board_size)
        self.__board_size = board_size
        self.__counter = 0
        self.__count_of_cells = self.__board_size ** 2
        self.__result = Game.UNKNOWN_SCORE

        self.__row_sum = np.zeros(board_size)
        self.__column_sum = np.zeros(board_size)
        self.__main_diagonal = 0
        self.__anti_diagonal = 0

    def __move(self, x, y):
        self.__counter += 1
        self.__row_sum[x] += self.__board.turn
        self.__column_sum[y] += self.__board.turn

        if x == y:
            self.__main_diagonal += self.__board.turn
        if x + y + 1 == self.__board:
            self.__anti_diagonal += self.__board.turn

        self.__board = self.__board.move(x, y)

    def start(self):
        print(self.__board)

    def __check(self):
        if self.__count_of_cells - self.__board_size < self.__counter:
            self.__result = Game.EQUAL_SCORE
            return Game.EQUAL_SCORE

        x_win = self.__board_size
        o_win = x_win * -1

        if (x_win in self.__row_sum) or (x_win in self.__column_sum) or (self.__main_diagonal == x_win) or (
                self.__anti_diagonal == x_win):
            self.__result = Game.X_Win_SCORE
        elif (o_win in self.__row_sum) or (o_win in self.__column_sum) or (self.__main_diagonal == o_win) or (
                self.__anti_diagonal == o_win):
            self.__result = Game.O_WIN_SCORE
        else:
            self.__result = Game.UNKNOWN_SCORE

    def step(self, x, y):
        self.__move(x, y)
        print(self.__board)
        self.__check()
        return self.__result

    @property
    def current_state(self):
        return self.__board

    @property
    def result(self):
        return self.__result
