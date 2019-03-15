from src.classes.Board import Board
from src.classes.LogicChecker import LogicChecker
from src.classes.InputHandler import InputHandler

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
    print("\n\n")
    print("------------------------------------------------")
    print("\t\tRound ", logic.turn, ":")


    board.draw()

    player_choice = in_handler.get_player_choice(current_player)

    if player_choice == 'surrender':
        break
    else:
        board.insert(current_player, *player_choice) 

    if logic.is_this_move_a_victory(current_player, *player_choice):
        print("\n-------------------------------------------------")
        print("\nPlayer", current_player, "has won after", logic.turn, "rounds!!\nAll hail the victor!\n")
        print("-------------------------------------------------\n\n\n")
        board.draw()
        break
    
        #Would this be a draw?

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

    logic.turn += 1