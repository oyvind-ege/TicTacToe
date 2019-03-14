class LogicChecker:
    def __init__(self, board):
        self.board = board

    def _check_horizontal(self, symbol, x, y):
        if x == 0:
            return (self.board.game_board[y][2] == symbol and self.board.game_board[y][4] == symbol)
        
        elif x == 2:
            return (self.board.game_board[y][0] == symbol and self.board.game_board[y][4] == symbol)

        elif x == 4:
            return (self.board.game_board[y][0] == symbol and self.board.game_board[y][2] == symbol)
        else:
            return False

    def _check_vertical(self, symbol, x, y):
        if y == 0:
            return (self.board.game_board[2][x] == symbol and self.board.game_board[4][x] == symbol)
        
        elif y == 2:
            return (self.board.game_board[0][x] == symbol and self.board.game_board[4][x] == symbol)

        elif y == 4:
            return (self.board.game_board[0][x] == symbol and self.board.game_board[2][x] == symbol)
        else:
            return False
    
    def _check_diagonal(self, symbol, x, y):
        
        if y != x:
            return False

        if y == 0:
            return (self.board.game_board[2][2] == symbol and self.board.game_board[4][4] == symbol)
        elif y == 2:
            return (self.board.game_board[0][0] == symbol and self.board.game_board[4][4] == symbol)
        elif y == 4:
            return (self.board.game_board[0][0] == symbol and self.board.game_board[2][2] == symbol)
        else:
            return False

    def is_this_move_a_victory(self, symbol, x, y):
        """Determine whether adding symbol to x,y of the game board would lead to victory. Return boolean."""
        return (self._check_horizontal(symbol, x, y) 
<<<<<<< HEAD
            or self._check_diagonal(symbol, y) 
            or self._check_vertical(symbol, x, y))

<<<<<<< Updated upstream
    def would_this_be_a_draw(self, symbol, empty_tiles_coordinates):
        """Checks whether the current gameboard setting results in a draw. Accepts a list of tuples. Each tuple contains coordinates for all empty tiles."""
        #If len(empty_tiles_coordinates) == 1:
            #Main logic
        #Else
            #Return False
        pass

    def would_this_move_be_a_draw(self, symbol, x, y):
        """Determine whether adding symbol to x,y of the game board would lead to victory. Return boolean."""
        pass
=======
    def would_this_move_be_a_draw(self, symbol, x, y):
        """Determine whether adding symbol to x,y of the game board would lead to victory. Return boolean."""
>>>>>>> Stashed changes
=======
            or self._check_diagonal(symbol, x, y) 
            or self._check_vertical(symbol, x, y))


>>>>>>> origin/master
