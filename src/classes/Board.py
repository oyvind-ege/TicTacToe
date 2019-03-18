"""
A game board is a list of lists.

Each sublist represents a data row, and contains symbols.
    A whitespace represents an empty cell
    An 'X' or 'O' (Oh) means the cell is owned by that player
    The edges and intersections of the game board itself are represented by: | or -- or + 

The game board looks like this (with coordinates):

  0  1  2  3  4
0    |     |
1 -- +  -- + --
2    |     |   
3 -- +  -- + --
4    |     |

"""

class Board:
    def __init__(self, setup=None):
        """Setup is a dictionary. Each key represents a player(X, O), the values is a list of tuples representing coordinates where that player has his piece."""

        self.size = 3
        self.game_board = [[' ' for column in range(self.size + 2)] for rows in range(self.size + 2)] #This represents the board data

        if setup:
            for symbol in setup:
                for coords in setup[symbol]:
                    self.game_board[coords[1]][coords[0]] = symbol

        self._set_grid()

    def _set_grid(self):
        """Insert the edges and intersections into the game board."""
        
        def _insert_horizontal_dividing_line(arow):
            arow[0] = '--'
            arow[1] = '+'
            arow[2] = '--'
            arow[3] = '+'
            arow[4] = '--'
        
        def _insert_simple_line(arow):
            arow[1] = '|'
            arow[3] = '|'

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
        """Insert 'symbol' into self.game_board(y, x)."""
        self.game_board[y][x] = symbol
    
    def draw(self):
        """Print the game board to the terminal."""
        print("\n")
        for row in self.game_board:
            for item in row:
                if item == ' ' or item == 'X' or item == 'O' or item.isnumeric():
                    print(' ', end='')
                print(item, end=" ")
            print('\n')
        print("\n")

    def get_tiles_as_dict(self):
        """Return a dict. Each key represents a symbol, and their values are tuples representing coordinates. Format is X,Y"""
        
        return_dict = {'X':[], 'O':[], ' ':[]}

        for y, row in enumerate(self.game_board):
            for x, column in enumerate(row):
                if column != '|' and column != '|' and column != '+' and column !='--':
                    return_dict[column].append((x,y)) #Will return x and y coordinates in a tuple

        return return_dict

    def dict_to_tiles(self, dictionary):
        """Will transform dictionary into self.game_board."""
        for symbol in dictionary:
            coordinates = dictionary[symbol]
            for each in coordinates:
                self.game_board[each[0]][each[1]] = symbol

    def empty_tile_coordinates(self):
        """Returns the coordinates for all empty tiles in X,Y format."""
        if self.game_board == None:
            raise IndexError

        coordinate_list = []
        for rowid, row in enumerate(self.game_board):
            for colid, col in enumerate(row):
                if col == ' ':
                    coordinate_list.append((colid, rowid))
        
        return coordinate_list
