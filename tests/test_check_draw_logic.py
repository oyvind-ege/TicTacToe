"""import pytest

from src.classes.Board import Board
from src.classes.LogicChecker import LogicChecker


@pytest.fixture(scope="function")
def board():
    board = Board()
    return board


class TestCheckForDrawLogic(object):

    def test_empty_board(self, board):
        checker = LogicChecker(board)
        assert checker.would_this_be_a_draw('X', board.empty_tile_coordinates()) == False

    def test_draw_on_first_row(self, board):
        checker = LogicChecker(board)
        board.game_board = [[' ', '|', 'O', '|', 'X'],
                            ['--', '+', '--', '+', '--'],
                            ['X', '|', 'O', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', 'X', '|', 'X']]
        assert checker.would_this_be_a_draw('X', board.empty_tile_coordinates()) == True
        
    def test_victory_on_second_row(self, board):
        checker = LogicChecker(board)
        board.game_board = [['X', '|', 'O', '|', 'X'],
                            ['--', '+', '--', '+', '--'],
                            ['X', '|', ' ', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', 'X', '|', 'X']]
        assert checker.would_this_be_a_draw('X', board.empty_tile_coordinates()) == False"""