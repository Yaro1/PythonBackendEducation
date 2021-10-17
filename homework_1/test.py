import unittest
from homework_1.tic_tac_toe import Board
from homework_1.exceptions import BoardInitException, BoardPutExceptionCoordinates, BoardPutExceptionItem, BoardPutExceptionExists


class TicTacToeTest(unittest.TestCase):

    def test_creating_board_1(self):
        self.assertRaises(BoardInitException, Board, -1)

    def test_creating_board_2(self):
        self.assertRaises(BoardInitException, Board, 0)

    def test_creating_board_3(self):
        self.assertRaises(BoardInitException, Board, 1)

    def test_creating_board_4(self):
        self.assertRaises(BoardInitException, Board, 2)

    def test_put_1(self):
        self.assertRaises(BoardPutExceptionCoordinates, Board().put, (-1, -1), 1)

    def test_put_2(self):
        self.assertRaises(BoardPutExceptionItem, Board().put, (0, 0), 21312312312)

    def test_put_3(self):
        self.assertRaises(BoardPutExceptionCoordinates, Board().put, (100, 100), 0)

    def test_put_4(self):
        board = Board()
        board.put((0, 0), 0)
        self.assertRaises(BoardPutExceptionExists, board.put, (0, 0), 1)

    def test_put_5(self):
        board = Board()
        board.put((0, 0), 0)
        self.assertRaises(BoardPutExceptionExists, board.put, (0, 0), 0)

    def test_game_result_1(self):
        board = Board()
        board.put((0, 0), 0)
        board.put((0, 1), 0)
        board.put((0, 2), 0)
        self.assertEqual('x', board.check_winner())

    def test_game_result_2(self):
        board = Board()
        board.put((0, 0), 1)
        board.put((0, 1), 1)
        board.put((0, 2), 1)
        self.assertEqual('o', board.check_winner())

    def test_game_result_3(self):
        board = Board()
        board.put((0, 0), 1)
        board.put((0, 1), 0)
        board.put((0, 2), 1)
        self.assertEqual('nobody', board.check_winner())
