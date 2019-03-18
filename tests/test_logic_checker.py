from src.classes.LogicChecker import LogicChecker
from src.classes.Board import Board

from src.classes.utilities import Logger as log

logger = log.Logger()

"""
The game board looks like this (with coordinates):

  0  1  2  3  4
0    |     |
1 -- +  -- + --
2    |     |   
3 -- +  -- + --
4    |     |

"""

class TestLogicChecker(object):
    def test_is_this_move_a_victory(self):
        board = Board()
        checker = LogicChecker(board)
        assert checker.is_this_move_a_victory('X', 2, 3) == False
    
    def test_is_this_move_a_victory_true(self):
        board = Board()
        board.insert('X', 0, 0)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)
        assert checker.is_this_move_a_victory('X', 4, 4) == True
    

    """Testing _check_horizontal()"""

    def test_check_horizontal_first_row(self):
        board = Board()
        board.insert('X', 0, 0)
        board.insert('X', 2, 0)
        checker = LogicChecker(board)
        assert checker._check_horizontal('X', 4, 0) == True
      
    def test_check_horizontal_second_row(self):
        board = Board()
        board.insert('X', 0, 2)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)
        assert checker._check_horizontal('X', 4, 2) == True

    def test_check_horizontal_second_row_false(self):
        board = Board()
        board.insert('X', 0, 2)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)
        assert checker._check_horizontal('X', 2, 4) == False
    
    """Testint _check_vertical()"""
    def test_check_vertical_first_column(self):
        board = Board()
        board.insert('X', 0, 0)
        board.insert('X', 0, 2)
        checker = LogicChecker(board)

        assert checker._check_vertical('X', 0, 4) == True
      
    def test_check_vertical_second_column(self):
        board = Board()
        board.insert('X', 2, 0)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)

        assert checker._check_vertical('X', 2, 4) == True
    
    def test_check_vertical_first_column_false(self):
        board = Board()
        board.insert('X', 0, 0)
        board.insert('X', 0, 2)
        checker = LogicChecker(board)

        assert checker._check_vertical('X', 2, 4) == False
      
    """Testint _check_diagonals()"""
    def test_check_diagonal_first_row(self):
        board = Board()
        board.insert('X', 4, 4)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)
        
        assert checker._check_diagonal('X', 0, 0) == True

    def test_check_diagonal_last_row(self):
        board = Board()
        board.insert('X', 0, 0)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)
        
        assert checker._check_diagonal('X', 4, 4) == True
    
    def test_check_diagonal_last_row_false(self):
        board = Board()
        board.insert('X', 0, 2)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)
        
        assert checker._check_diagonal('X', 4, 4) == False
    
    def test_check_diagonal_middle_row(self):
        board = Board()
        board.insert('X', 0, 0)
        board.insert('X', 4, 4)
        checker = LogicChecker(board)
        
        assert checker._check_diagonal('X', 2, 2) == True
    
    def test_check_diagonal_topright_to_bottom_left(self):
        board = Board()
        board.insert('X', 4, 0)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)

        board.draw()
        
        assert checker._check_diagonal('X', 0, 4) == True
    
    def test_check_diagonal_middle_row_false(self):
        board = Board()
        board.insert('X', 0, 0)
        board.insert('X', 4, 0)
        checker = LogicChecker(board)

        board.draw()
        
        assert checker._check_diagonal('X', 2, 2) == False
    
    def test_check_diagonal_symbol_mismatch(self):
        board = Board()
        board.insert('O', 0, 0)
        board.insert('X', 4, 4)
        checker = LogicChecker(board)
        
        assert checker._check_diagonal('O', 2, 2) == False

    def test_check_diagonal_other_symbol(self):
        board = Board()
        board.insert('O', 0, 0)
        board.insert('O', 4, 4)
        checker = LogicChecker(board)
        
        assert checker._check_diagonal('O', 2, 2) == True


class TestDrawChecker(object):
    """Test whether the check draw logic works."""


    """Test true conditions."""
    def test_two_remaining(self):
        board = Board()
        checker = LogicChecker(board)
        checker.turn = 8
        board.game_board = [['X', '|', 'O', '|', 'X'],
                            ['--', '+', '--', '+', '--'],
                            ['X', '|', 'O', '|', ' '],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', 'X', '|', ' ']]
        assert checker.would_this_be_a_draw('O', [(4,2), (4,4)]) == True

    def test_two_remaining_2(self):
        board = Board()
        checker = LogicChecker(board)
        checker.turn = 8
        board.game_board = [['X', '|', 'X', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', 'O', '|', 'X'],
                            ['--', '+', '--', '+', '--'],
                            ['X', '|', ' ', '|', ' ']]
        assert checker.would_this_be_a_draw('O', [(2,4), (4,4)]) == True
    
    def test_one_remaining(self):
        board = Board()
        checker = LogicChecker(board)
        checker.turn = 9
        board.game_board = [['X', '|', 'O', '|', 'X'],
                            ['--', '+', '--', '+', '--'],
                            [' ', '|', 'X', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', 'X', '|', 'O']]
        assert checker.would_this_be_a_draw('X', [(0,2)]) == True
    
    def test_one_remaining_2(self):
        board = Board()
        checker = LogicChecker(board)
        checker.turn = 9
        board.game_board = [['X', '|', 'X', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', ' ', '|', 'X'],
                            ['--', '+', '--', '+', '--'],
                            ['X', '|', 'O', '|', 'O']]
        assert checker.would_this_be_a_draw('X', [(2,2)]) == True
    
    """Victory scenarios"""

    
    def test_diagonal_victory_in_1(self):
        board = Board()
        checker = LogicChecker(board)
        checker.turn = 9
        board.game_board = [[' ', '|', 'X', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', 'X', '|', 'X'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', 'O', '|', 'X']]
        assert checker.would_this_be_a_draw('X', [(0,0)]) == False
    
    def test_empty_board(self):
        board = Board()
        checker = LogicChecker(board)
        board.game_board = [[' ', '|', ' ', '|', ' '],
                            ['--', '+', '--', '+', '--'],
                            [' ', '|', ' ', '|', ' '],
                            ['--', '+', '--', '+', '--'],
                            [' ', '|', ' ', '|', ' ']]
        assert checker.would_this_be_a_draw('X', [(0,0),(2,0),(4,0),
                                                  (0,2),(2,2),(4,2),
                                                  (0,4),(2,4),(4,4)]) == False
    
    """
    Mistake possible!
    One player can commit a grievous mistake! This is not a draw condition.
    """

    def test_mistake_possible_2(self):
        board = Board()
        checker = LogicChecker(board)
        checker.turn = 8

        board.game_board = [['X', '|', ' ', '|', 'X'],
                            ['--', '+', '--', '+', '--'],
                            ['X', '|', 'X', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', 'O', '|', ' ']]

        checker.board.draw()

        assert checker.would_this_be_a_draw('O', [(2,0), (4,4)]) == False
    

