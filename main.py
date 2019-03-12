import pprint

from src.classes.Board import Board
from src.classes.LogicChecker import LogicChecker
from src.classes.InputHandler import InputHandler

board = Board() #This is the game board itself
checker = LogicChecker(board)

help_board = Board() #This is a board that helps the user pick where to place their X or O.

help_board.insert('1', 0, 0)
help_board.insert('2', 2, 0)
help_board.insert('3', 4, 0)

help_board.insert('4', 0, 2)
help_board.insert('5', 2, 2)
help_board.insert('6', 4, 2)

help_board.insert('7', 0, 4)
help_board.insert('8', 2, 4)
help_board.insert('9', 4, 4)


in_handler = InputHandler(help_board, board)


"""Main Loop"""

current_player = 'X'
i = 1
while 1:

    print("------------------------------------------------")
    print("\t\tRound ", i, ":")
    board.draw()
    player_choice = in_handler.get_player_choice(current_player)

    if player_choice != -1: #player_choice will be false if one of the players surrenders
        board.insert(current_player, *player_choice)
    else:
        break

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

    i += 1