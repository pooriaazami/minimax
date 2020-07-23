from game import Game
from node import Node
from tree import Tree

board_size = 3

node = Node(board_size=board_size)
tree = Tree(board_size=board_size)
game = Game(board_size=board_size)


def read_move_from_keyboard():
    movement = input().split(" ")
    return int(movement[0]), int(movement[1])


def ai_move(state: Node = None):
    return tree.minimax(state)


turn = True

game.start()

while game.result is Game.UNKNOWN_SCORE:
    if turn:
        x, y = read_move_from_keyboard()
    else:
        x, y = ai_move(game.current_state)

    game.step(x, y)
    turn = not turn

if game.result == Game.X_Win_SCORE:
    print("X wins the game")
elif game.result == Game.O_WIN_SCORE:
    print("O wins the game")
else:
    print("Equal")
