from typing import Callable

from node import Node


class Tree:
    first_player = 1
    second_player = -1
    empty_cell = 0

    opponent_turn: Callable[[int], int] = lambda x: x * -1

    def __init__(self, board_size: int = 3):
        self.__board_size = board_size

    def __minimax_step(self, node: Node, root: Node):
        win = node.result if node.result is not None else node.optimum
        if node.parent is not None:
            if node.parent.turn == 1:
                node.parent.optimum = max(win, node.parent.optimum)
            else:
                node.parent.optimum = min(win, node.parent.optimum)
            if node.parent is root and win == root.optimum:
                return node.difference_with_parent()
            return None, None

    def minimax(self, initial_node: Node):
        stack = [initial_node]
        x, y = -1, -1
        while stack:
            top = stack[-1]
            top.check()
            if top.result is None and top.marked:
                for child in top.children():
                    stack.append(child)
                top.mark()
            else:
                x_temp, y_temp = self.__minimax_step(top, initial_node)
                x, y = (x_temp, y_temp) if x_temp is not None else (x, y)
                stack.pop()

        return x, y
