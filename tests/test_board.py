from src.cBoard import Board

class TestBoardClass(object):
    def test_set_board(self):
        board = Board()
        board._set_grid()
        assert board.game_board == [[' ', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', ' ', '|', ' ']]
    
    def test_draw(self):
        board = Board()
        board._set_grid()
        assert board.draw() ==      [[' ', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', ' ', '|', ' '],
                                    ['--', '+', '--', '+', '--'],
                                    [' ', '|', ' ', '|', ' ']]

    def test_insert(self):
        board = Board()
        board._set_grid()
        board.insert('X', 0, 0)
        assert board.draw() == [['X', '|', ' ', '|', ' '],
                                ['--', '+', '--', '+', '--'],
                                [' ', '|', ' ', '|', ' '],
                                ['--', '+', '--', '+', '--'],
                                [' ', '|', ' ', '|', ' ']]
    
    def test_insert_44(self):
        board = Board()
        board._set_grid()
        board.insert('X', 4, 4)
        assert board.draw() == [[' ', '|', ' ', '|', ' '],
                                ['--', '+', '--', '+', '--'],
                                [' ', '|', ' ', '|', ' '],
                                ['--', '+', '--', '+', '--'],
                                [' ', '|', ' ', '|', 'X']]
    
    def test_insert_42(self):
        board = Board()
        board._set_grid()
        board.insert('O', 2, 4)
        assert board.draw() == [[' ', '|', ' ', '|', ' '],
                                ['--', '+', '--', '+', '--'],
                                [' ', '|', ' ', '|', ' '],
                                ['--', '+', '--', '+', '--'],
                                [' ', '|', 'O', '|', ' ']]