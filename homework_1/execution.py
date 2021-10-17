from tic_tac_toe import Board


def execution():
    board = Board()
    board.put((0, 0), 0)
    board.put((0, 1), 0)
    board.put((0, 2), 0)
    print(board)
    print(board.check_winner())

execution()
