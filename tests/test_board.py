import pytest

from src.Board import Board


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
        assert board.get_list_of_data() == [[' ', '|', ' ', '|', ' '],
                                            ['--', '+', '--', '+', '--'],
                                            [' ', '|', ' ', '|', ' '],
                                            ['--', '+', '--', '+', '--'],
                                            [' ', '|', ' ', '|', ' ']]

    def test_insert(self, board):
        board.insert('X', 0, 0)
        assert board.get_list_of_data() == [['X', '|', ' ', '|', ' '],
                                            ['--', '+', '--', '+', '--'],
                                            [' ', '|', ' ', '|', ' '],
                                            ['--', '+', '--', '+', '--'],
                                            [' ', '|', ' ', '|', ' ']]
    
    def test_insert_44(self, board):
        board.insert('X', 4, 4)
        assert board.get_list_of_data() == [[' ', '|', ' ', '|', ' '],
                                            ['--', '+', '--', '+', '--'],
                                            [' ', '|', ' ', '|', ' '],
                                            ['--', '+', '--', '+', '--'],
                                            [' ', '|', ' ', '|', 'X']]
    
    def test_insert_42(self, board):
        board.insert('O', 2, 4)
        assert board.get_list_of_data() == [[' ', '|', ' ', '|', ' '],
                                            ['--', '+', '--', '+', '--'],
                                            [' ', '|', ' ', '|', ' '],
                                            ['--', '+', '--', '+', '--'],
                                            [' ', '|', 'O', '|', ' ']]