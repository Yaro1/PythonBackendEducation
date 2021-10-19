"""
Tests for homework1
"""
import unittest
from homework_1.tic_tac_toe import Board
from homework_1.exceptions import BoardInitException, BoardPutExceptionCoordinates, \
    BoardPutExceptionItem, BoardPutExceptionExists


class TicTacToeTest(unittest.TestCase):
    """
    Testing class.
    """

    def test_creating_board(self):
        """
        :return:
        """
        self.assertRaises(BoardInitException, Board, -1)
        self.assertRaises(BoardInitException, Board, 0)
        self.assertRaises(BoardInitException, Board, 1)
        self.assertRaises(BoardInitException, Board, 2)
        board = Board(3)
        self.assertEqual(board.board, Board(3).board)
        board = Board(5)
        self.assertEqual(board.board, Board(5).board)
        board = Board(7)
        self.assertEqual(board.board, Board(7).board)

    def test_put(self):
        """
        Check puting item by coordinates to the board.
        """
        self.assertRaises(BoardPutExceptionCoordinates, Board().put, (-1, -1), 1)
        self.assertRaises(BoardPutExceptionItem, Board().put, (0, 0), 21312312312)
        self.assertRaises(BoardPutExceptionCoordinates, Board().put, (100, 100), 0)
        matrix_test = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        board = Board()
        board.put((0, 0), 0)
        matrix_test[0][0] = 0
        self.assertEqual(matrix_test, board.board)
        board.put((1, 1), 0)
        matrix_test[1][1] = 0
        self.assertEqual(matrix_test, board.board)
        board.put((2, 2), 0)
        matrix_test[2][2] = 0
        self.assertEqual(matrix_test, board.board)
        board.put((0, 2), 1)
        matrix_test[0][2] = 1
        self.assertEqual(matrix_test, board.board)
        self.assertRaises(BoardPutExceptionExists, board.put, (0, 0), 1)
        self.assertRaises(BoardPutExceptionExists, board.put, (0, 0), 0)

    def test_game_results(self):
        """
        :return:
        """
        board = Board()
        board.put((0, 0), 0)
        board.put((0, 1), 0)
        board.put((0, 2), 0)
        self.assertEqual('x', board.check_winner())

        board = Board()
        board.put((0, 0), 1)
        board.put((0, 1), 1)
        board.put((0, 2), 1)
        self.assertEqual('o', board.check_winner())

        board = Board()
        board.put((0, 0), 1)
        board.put((0, 1), 0)
        board.put((0, 2), 1)
        self.assertEqual('nobody', board.check_winner())
