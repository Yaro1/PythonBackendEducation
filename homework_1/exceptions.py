"""
Module for manual exceptions.
"""


class BoardException(Exception):
    """
    Base exception.
    """
    def __init__(self, obj, msg=None):
        self.obj = obj
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.obj} -> {self.msg}'


class BoardInitException(BoardException):
    """
    Initialisation exception.
    """
    def __init__(self, size_board, msg="Size of the board should be odd and more than 2"):
        super().__init__(size_board, msg)


class BoardPutExceptionItem(BoardException):
    """
    Putting excetion in item.
    """
    def __init__(self, item, msg="Your value should be 0 or 1"):
        super().__init__(item, msg)


class BoardPutExceptionCoordinates(BoardException):
    """
    Putting exception in coordinates.
    """
    def __init__(self, coordinates, msg="Coordinates should be two digit inside [0 -> board.size]"):
        super().__init__(coordinates, msg)


class BoardPutExceptionExists(BoardException):
    """
    Putting exception (same coordinates was using).
    """
    def __init__(self, coordinates, msg="On this coordinates already exist element"):
        super().__init__(coordinates, msg)
