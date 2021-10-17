"""
Tic tac toe class.
"""

from homework_1.exceptions import BoardInitException, BoardPutExceptionItem,\
    BoardPutExceptionCoordinates, BoardPutExceptionExists

MAPPING = {0: 'x', 1: 'o', -1: '_'}


class Board:
    """
    Class board for playing in tic-tac-toe.
    """

    def __init__(self, size=3):
        if size % 2 == 0 or size < 3:
            raise BoardInitException(size)
        self.size = size
        self.board = [[-1 for _ in range(self.size)] for _ in range(self.size)]

    def __str__(self):
        return '\n'.join([''.join([MAPPING[symbol] for symbol in str_]) for str_ in self.board])

    def put(self, coordinates, item):
        """
        :param coordinates:
        :param item:
        :return:
        """
        if item not in [0, 1]:
            raise BoardPutExceptionItem(item=item)
        isistance_expr = not isinstance(coordinates[0], int) or not isinstance(coordinates[1], int)
        crdnt_expr_less = coordinates[0] < 0 or coordinates[1] < 0
        crdnt_expr_greater = coordinates[0] > self.size - 1 or coordinates[1] > self.size - 1
        if len(coordinates) != 2 or isistance_expr or crdnt_expr_less or crdnt_expr_greater:
            raise BoardPutExceptionCoordinates(coordinates=coordinates)
        if self.board[coordinates[0]][coordinates[1]] != -1:
            raise BoardPutExceptionExists(coordinates)
        self.board[coordinates[0]][coordinates[1]] = item

    @staticmethod
    def check(checked_set):
        """
        :param checked_set:
        :return:
        """
        if len(checked_set) == 1:
            item = checked_set.pop()
            if MAPPING[item] in ['x', 'o']:
                return 'x' if MAPPING[item] == 'x' else 'o'
        return 'nobody'

    def check_winner_str_col(self, str_col):
        """
        :param str_col:
        :return:
        """
        return self.check(set(str_col))

    def check_diagonal(self, list_coordinates):
        """
        :param list_coordinates:
        :return:
        """
        checking = set()
        for i, j in list_coordinates:
            checking.add(self.board[i][j])
        return self.check(checking)

    def check_winner(self):
        """
        :return:
        """
        results = set()
        for str_col in self.board + [*zip(*self.board)]:
            results.add(self.check_winner_str_col(str_col))
        diagonal = [(i, i) for i in range(self.size)]
        reverse_diagonal = [(i, self.size - i - 1) for i in range(self.size)]
        results.add(self.check_diagonal(diagonal))
        results.add(self.check_diagonal(reverse_diagonal))
        if 'x' in results or 'o' in results:
            return 'x' if 'x' in results else 'o'
        return 'nobody'
