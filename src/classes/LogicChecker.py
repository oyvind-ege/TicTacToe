from src.classes.Board import Board

class LogicChecker:
    def __init__(self, board):
        self.board = board
        self.turn = 1
        self.symbol_opposites = {'O': 'X', 'X': 'O'}

    def _check_horizontal(self, next_symbol, x, y):
        if x == 0:
            return (self.board.game_board[y][2] == next_symbol and self.board.game_board[y][4] == next_symbol)
        
        elif x == 2:
            return (self.board.game_board[y][0] == next_symbol and self.board.game_board[y][4] == next_symbol)

        elif x == 4:
            return (self.board.game_board[y][0] == next_symbol and self.board.game_board[y][2] == next_symbol)
        else:
            return False

    def _check_vertical(self, next_symbol, x, y):
        if y == 0:
            return (self.board.game_board[2][x] == next_symbol and self.board.game_board[4][x] == next_symbol)
        
        elif y == 2:
            return (self.board.game_board[0][x] == next_symbol and self.board.game_board[4][x] == next_symbol)

        elif y == 4:
            return (self.board.game_board[0][x] == next_symbol and self.board.game_board[2][x] == next_symbol)
        else:
            return False
    
    def _check_diagonal(self, next_symbol, x, y):
        """Check if adding a next_symbol to either (0,0), (4,0), (2,2), (0,4), (4,4) will lead to a complete diagonal."""

        top_left = self.board.game_board[0][0]
        top_right = self.board.game_board[0][4]
        mid = self.board.game_board[2][2]
        bot_left = self.board.game_board[4][0]
        bot_right = self.board.game_board[4][4]
        
        if y == 0:

            if x != 0 and x != 4:
                return False
            elif x == 0:
                return (mid == next_symbol and bot_right == next_symbol)
            elif x == 4:
                return (mid == next_symbol and bot_left == next_symbol)

        elif y == 2:

            if x != 2:
                return False
            
            return ((top_left == next_symbol and bot_right == next_symbol) or
                    (top_right == next_symbol and bot_left == next_symbol))

        elif y == 4:

            if x != 0 and x != 4:
                return False
            elif x == 4:
                return (top_left == next_symbol and mid == next_symbol)
            elif x == 0:
                return (top_right == next_symbol and mid == next_symbol)

        else:

            return False

    def is_this_move_a_victory(self, next_symbol, x, y):
        """Determine whether adding next_symbol to x,y of the game board would lead to victory. Return boolean."""


        horizontal_win = self._check_horizontal(next_symbol, x, y)
        diagonal_win = self._check_diagonal(next_symbol, x, y)
        vertical_win = self._check_vertical(next_symbol, x, y)


        return (horizontal_win 
            or diagonal_win 
            or vertical_win)

    def would_this_be_a_draw(self, next_symbol, empty_tiles_coordinates):
        """Checks whether the current gameboard setting results in a draw.

        Accepts a string next_symbol 'X' or 'Y', and a list of tuples. 
            The string represents the player with the current move.
            The tuples contain coordinates for all empty tiles.
        
        """
            
        next_symbol = self.symbol_opposites[next_symbol] #The code here makes predictions about next round

        if self.turn >= 7 and self.turn < 8: #There are two open tiles left, next_symbol == 'O'
            current_positions_as_dict = self.board.get_tiles_as_dict()

            """There are two scenarios. One takes place if player 'O' chooses one tile; the other if he chooses the other tile."""

            scenario1_future_positions = current_positions_as_dict
            scenario2_future_positions = current_positions_as_dict

            #Scenario 1
            scenario1_future_positions[next_symbol].append(empty_tiles_coordinates[0])

            scenario1_board = Board(setup=scenario1_future_positions)
            scenario1_logic = LogicChecker(scenario1_board)

            scenario1_boolean = (   not self.is_this_move_a_victory(next_symbol, *empty_tiles_coordinates[0]) 
                                and not scenario1_logic.is_this_move_a_victory(self.symbol_opposites[next_symbol], *empty_tiles_coordinates[1]))
 
            #Scenario 2
            scenario2_future_positions[next_symbol].append(empty_tiles_coordinates[1])

            scenario2_board = Board(setup=scenario2_future_positions)
            scenario2_logic = LogicChecker(scenario2_board)

            scenario2_boolean = (   not self.is_this_move_a_victory(next_symbol, *empty_tiles_coordinates[1])
                                and not scenario2_logic.is_this_move_a_victory(self.symbol_opposites[next_symbol], *empty_tiles_coordinates[0]))

            return ( scenario1_boolean and scenario2_boolean )

        elif self.turn == 8:
            will_there_be_a_victory = self.is_this_move_a_victory(next_symbol, *empty_tiles_coordinates[0])
            return (not will_there_be_a_victory)
        
        else:
            return False #We cannot guarantee that there will be a draw
