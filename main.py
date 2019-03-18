import math

from src.classes.Board import Board
from src.classes.LogicChecker import LogicChecker
from src.classes.InputHandler import InputHandler

from src.classes.utilities import Logger as log



logger = log.Logger()
board = Board() #This is the game board itself
logic = LogicChecker(board)

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
while 1:
    print("------------------------------------------------")
    print("\t\tRound ", math.ceil(logic.turn/2), ":\n\n\tPlayer ", current_player, " - it is your turn.\n")

    board.draw()

    player_choice = in_handler.get_player_choice(current_player)

    if player_choice == 'surrender':
        break
    else:
        board.insert(current_player, *player_choice) 

    if logic.is_this_move_a_victory(current_player, *player_choice):
        board.draw()
        print("\n-------------------------------------------------")
        print("\nPlayer", current_player, "has won after", math.ceil(logic.turn/2), "rounds!!\nAll hail the victor!\n")
        print("-------------------------------------------------\n\n")
        break
    
    if logic.turn >= 7:
        if logic.would_this_be_a_draw(current_player, board.empty_tile_coordinates()):
            board.draw()
            print("\n-------------------------------------------------")
            print("\nA draw after", math.ceil(logic.turn/2), "rounds!!\nGood work both!\n")
            print("-------------------------------------------------\n\n\n")
            break

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

    logic.turn += 1