class BoardException(Exception):
    def __init__(self, obj, message=None):
        self.obj = obj
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.obj} -> {self.message}'


class BoardInitException(BoardException):

    def __init__(self, size_board, message="Size of the board should be odd and more than 2"):
        super().__init__(size_board, message)


class BoardPutExceptionItem(BoardException):

    def __init__(self, item, message="Your value should be 0 or 1"):
        super().__init__(item, message)


class BoardPutExceptionCoordinates(BoardException):

    def __init__(self, coordinates, message="Coordinates should be two digit inside [0 -> board.size]"):
        super().__init__(coordinates, message)
