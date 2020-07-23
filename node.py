from itertools import product

import numpy as np


class Node:

    def __init__(self, board_size: int = 3, board: np.ndarray = None, turn: int = 1, parent=None):
        self.__size = board_size
        self.__turn = turn
        self.__optimum_value = self.__turn * -1
        self.__board_size = board_size
        self.__count_of_cells = self.__board_size ** 2
        self.__mark = True
        self.__parent = parent
        self.__result = None

        if board is not None:
            self.__board = board
            self.__board_size = self.__board.shape[0]
        else:
            self.__board = np.zeros((self.__size, self.__size))

    def __len__(self):
        return len(self.__board)

    def children(self):
        for i, j in product(range(self.__board_size), range(self.__board_size)):
            if not self.__board[i, j]:
                child_board = self.__board.copy()
                child_board[i, j] = self.turn
                child = Node(self.__board_size, child_board, self.__turn * -1, self)
                yield child

    @property
    def turn(self):
        return self.__turn

    @property
    def optimum(self):
        return self.__optimum_value

    @optimum.setter
    def optimum(self, val):
        self.__optimum_value = val

    @property
    def marked(self):
        return self.__mark

    @property
    def board(self):
        return self.__board

    @property
    def board_size(self):
        return self.__board_size

    @property
    def result(self):
        return self.__result

    def check(self):
        if self.__result is not None:
            return self.__result

        row_sum = self.__board.sum(axis=1)
        column_sum = self.__board.sum(axis=0)
        main_diagonal = np.trace(self.__board)
        anti_diagonal = np.trace(np.fliplr(self.__board))

        win_score = self.__turn * self.__board_size
        loss_score = win_score * -1

        if (win_score in row_sum) or (win_score in column_sum) or (main_diagonal == win_score) or (anti_diagonal ==
                                                                                                   win_score):
            self.__result = self.__turn
        elif (loss_score in row_sum) or (loss_score in column_sum) or (main_diagonal == loss_score) or (anti_diagonal ==
                                                                                                        loss_score):
            self.__result = self.__turn * -1
        elif np.count_nonzero(self.__board) > self.__count_of_cells - self.__board_size:
            self.__result = 0
        else:
            self.__result = None

        return self.__result

    @property
    def parent(self):
        return self.__parent

    def mark(self):
        self.__mark = False

    def __repr__(self):
        me = ""

        for i in range(self.__board_size):
            for j in range(self.__board_size):
                if self.__board[i, j] == 1:
                    me += "X "
                elif self.__board[i, j] == -1:
                    me += "O "
                else:
                    me += "_ "
            me += "\n"

        return me

    def move(self, x, y):
        child_board = self.__board.copy()
        child_board[x, y] = self.__turn
        return Node(self.__board_size, child_board, self.__turn * -1, self)

    def difference_with_parent(self):
        if self.parent is not None:
            for i, j in product(range(self.__board_size), range(self.__board_size)):
                if self.parent.board[i, j] != self.board[i, j]:
                    return i, j
        else:
            for i, j in product(range(self.__board_size), range(self.__board_size)):
                if self.board[i, j]:
                    return i, j
