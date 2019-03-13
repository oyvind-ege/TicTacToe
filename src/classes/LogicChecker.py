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
            or self._check_diagonal(symbol, x, y) 
            or self._check_vertical(symbol, x, y))


