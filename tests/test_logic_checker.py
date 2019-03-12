import pytest

from src.LogicChecker import LogicChecker
from src.Board import Board


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
        board._set_grid()
        checker = LogicChecker(board)
        print(board.game_board)
        assert checker.is_this_move_a_victory('X', 2, 3) == False
    
    def test_is_this_move_a_victory_true(self):
        board = Board()
        board._set_grid()
        board.insert('X', 0, 0)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)
        assert checker.is_this_move_a_victory('X', 4, 4) == True
    

    """Testing _check_horizontal()"""

    def test_check_horizontal_first_row(self):
        board = Board()
        board._set_grid()
        board.insert('X', 0, 0)
        board.insert('X', 2, 0)
        checker = LogicChecker(board)
        assert checker._check_horizontal('X', 4, 0) == True
      
    def test_check_horizontal_second_row(self):
        board = Board()
        board._set_grid()
        board.insert('X', 0, 2)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)
        assert checker._check_horizontal('X', 4, 2) == True

    def test_check_horizontal_second_row_false(self):
        board = Board()
        board._set_grid()
        board.insert('X', 0, 2)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)
        assert checker._check_horizontal('X', 2, 4) == False
    
    """Testint _check_vertical()"""
    def test_check_vertical_first_column(self):
        board = Board()
        board._set_grid()
        board.insert('X', 0, 0)
        board.insert('X', 0, 2)
        checker = LogicChecker(board)

        assert checker._check_vertical('X', 0, 4) == True
      
    def test_check_vertical_second_column(self):
        board = Board()
        board._set_grid()
        board.insert('X', 2, 0)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)

        assert checker._check_vertical('X', 2, 4) == True
    
    def test_check_vertical_first_column_false(self):
        board = Board()
        board._set_grid()
        board.insert('X', 0, 0)
        board.insert('X', 0, 2)
        checker = LogicChecker(board)

        assert checker._check_vertical('X', 2, 4) == False
      
    """Testint _check_diagonals()"""
    def test_check_diagonal_first_row(self):
        board = Board()
        board._set_grid()
        board.insert('X', 4, 4)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)
        
        assert checker._check_diagonal('X', 0) == True

    def test_check_diagonal_last_row(self):
        board = Board()
        board._set_grid()
        board.insert('X', 0, 0)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)
        
        assert checker._check_diagonal('X', 4) == True
    
    def test_check_diagonal_last_row_false(self):
        board = Board()
        board._set_grid()
        board.insert('X', 0, 2)
        board.insert('X', 2, 2)
        checker = LogicChecker(board)
        
        assert checker._check_diagonal('X', 4) == False
    
    def test_check_diagonal_middle_row(self):
        board = Board()
        board._set_grid()
        board.insert('X', 0, 0)
        board.insert('X', 4, 4)
        checker = LogicChecker(board)
        
        assert checker._check_diagonal('X', 2) == True
    
    def test_check_diagonal_middle_row_false(self):
        board = Board()
        board._set_grid()
        board.insert('X', 0, 0)
        board.insert('X', 0, 4)
        checker = LogicChecker(board)
        
        assert checker._check_diagonal('X', 2) == False
    
    def test_check_diagonal_symbol_mismatch(self):
        board = Board()
        board._set_grid()
        board.insert('O', 0, 0)
        board.insert('X', 4, 4)
        checker = LogicChecker(board)
        
        assert checker._check_diagonal('O', 2) == False

    def test_check_diagonal_other_symbol(self):
        board = Board()
        board._set_grid()
        board.insert('O', 0, 0)
        board.insert('O', 4, 4)
        checker = LogicChecker(board)
        
        assert checker._check_diagonal('O', 2) == True
      