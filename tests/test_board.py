import pytest

from src.classes.Board import Board


@pytest.fixture(scope="function")
def board():
    board = Board()
    return board

class TestBoardClass(object):
    def test_set_board(self, board):
        assert board.game_board == [[' ', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', ' ', '|', ' ']]
    
    def test_get_list_data(self, board):
        assert board.game_board == [[' ', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', ' ', '|', ' ']]

    def test_insert(self, board):
        board.insert('X', 0, 0)
        assert board.game_board == [['X', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', ' ', '|', ' ']]
    
    def test_insert_44(self, board):
        board.insert('X', 4, 4)
        assert board.game_board == [[' ', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', ' ', '|', 'X']]
    
    def test_insert_42(self, board):
        board.insert('O', 2, 4)
        assert board.game_board == [[' ', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', 'O', '|', ' ']]

    """how_many_open_tiles_remain()"""
    def test_hmotr_empty(self, board):
        assert board.how_many_open_tiles_remain() == 9
    
    def test_hmotr_full(self, board):
        board.game_board = [['X', '|', 'X', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['X', '|', 'O', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', 'X', '|', 'X']]
        assert board.how_many_open_tiles_remain() == 0

    def test_hmotr_1(self, board):
        board.game_board = [[' ', '|', 'O', '|', 'X'],
                            ['--', '+', '--', '+', '--'],
                            ['X', '|', 'O', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', 'X', '|', 'X']]
        assert board.how_many_open_tiles_remain() == 1

    def test_hmotr_no_data(self, board):
        board.game_board = None
        with pytest.raises(IndexError):
            board.how_many_open_tiles_remain()
