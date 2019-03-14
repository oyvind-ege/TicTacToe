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

<<<<<<< Updated upstream
    """empty_tile_coordinates()"""
    def test_tr_empty(self, board):
        assert board.empty_tile_coordinates() == [ (0,0),(2,0),(4,0), 
                                            (0,2),(2,2),(4,2),
                                            (0,4),(2,4),(4,4)]
    
    def test_tr_full(self, board):
=======
    """how_many_open_tiles_remain()"""
    def test_hmotr_empty(self, board):
        assert board.how_many_open_tiles_remain() == 9
    
    def test_hmotr_full(self, board):
>>>>>>> Stashed changes
        board.game_board = [['X', '|', 'X', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['X', '|', 'O', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', 'X', '|', 'X']]
<<<<<<< Updated upstream
        assert board.empty_tile_coordinates() == []

    def test_tr_first(self, board):
=======
        assert board.how_many_open_tiles_remain() == 0

    def test_hmotr_1(self, board):
>>>>>>> Stashed changes
        board.game_board = [[' ', '|', 'O', '|', 'X'],
                            ['--', '+', '--', '+', '--'],
                            ['X', '|', 'O', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', 'X', '|', 'X']]
<<<<<<< Updated upstream
        assert board.empty_tile_coordinates() == [(0,0)]

    def test_tr_middle(self, board):
        board.game_board = [['X', '|', 'O', '|', 'X'],
                            ['--', '+', '--', '+', '--'],
                            ['X', '|', ' ', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', 'X', '|', 'X']]
        assert board.empty_tile_coordinates() == [(2,2)]
    
    def test_tr_topmid(self, board):
        board.game_board = [['X', '|', 'O', '|', 'X'],
                            ['--', '+', '--', '+', '--'],
                            ['X', '|', 'X', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            ['O', '|', ' ', '|', 'X']]
        assert board.empty_tile_coordinates() == [(2,4)]

    def test_tr_toprow(self, board):
        board.game_board = [['X', '|', 'O', '|', 'X'],
                            ['--', '+', '--', '+', '--'],
                            ['X', '|', 'X', '|', 'O'],
                            ['--', '+', '--', '+', '--'],
                            [' ', '|', ' ', '|', ' ']]
        assert board.empty_tile_coordinates() == [(0,4),(2,4), (4,4)]

    def test_tr_no_data(self, board):
        board.game_board = None
        with pytest.raises(IndexError):
            board.empty_tile_coordinates()
=======
        assert board.how_many_open_tiles_remain() == 1

    def test_hmotr_no_data(self, board):
        board.game_board = None
        with pytest.raises(IndexError):
            board.how_many_open_tiles_remain()
>>>>>>> Stashed changes
