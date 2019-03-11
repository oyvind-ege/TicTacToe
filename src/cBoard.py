"""
A game board is a list of lists.

Each sublist represents a data row, and contains symbols.
    A whitespace represents an empty cell
    An 'X' or 'O' (Oh) means the cell is owned by that player
    The edges and intersections of the game board itself: | or -- or + 

The game board looks like this (with coordinates):

  0  1  2  3  4
0    |     |
1 -- +  -- + --
2    |     |   
3 -- +  -- + --
4    |     |

"""

class Board:
    def __init__(self):
        self.size = 3
        self.game_board = [[' ' for column in range(self.size + 2)] for rows in range(self.size + 2)] #This represents the board data
    
    def _set_grid(self):
        """
        Purpose: Inserts the edges and intersections into the game board.
        Example:

          |  | 
        --+--+--
          |  | 
        """
        def _insert_horizontal_dividing_line(arow):
            arow[0] = '--'
            arow[1] = '+'
            arow[2] = '--'
            arow[3] = '+'
            arow[4] = '--'
        
        def _insert_simple_line(arow):
            row[1] = '|'
            row[3] = '|'

        for index, row in enumerate(self.game_board):
            #Insert horizontal dividing lines in all odd rows
            #Insert simple lines in all other rows
            if index == 0:
                _insert_simple_line(row)
            if index % 2 == 0:
                _insert_simple_line(row)
            else:
                _insert_horizontal_dividing_line(row)

    def insert(self, symbol, x, y):
        """
        Inserts 'symbol' into self.game_board(y, x)
        """
        self.game_board[y][x] = symbol
    
    def draw(self):
        """Draws the current board on the screen."""
        return [row for row in self.game_board]