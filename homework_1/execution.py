"""
Execution module for homework_1.
"""
from homework_1.exceptions import BoardPutExceptionExists
from homework_1.tic_tac_toe import Board


def execution():
    """
    Function for playing on tic-tac-toe
    :return:
    """
    help_info = "If you want to print board please press p.\nIf you want to quit please press q."
    print("Start game.")
    print(help_info)
    hello = "Please enter the name {number} player.\n"
    first_player, second_player = input(hello.format(number="first")), input(hello.format(number="second"))
    map_players = {'x': first_player, 'o': second_player}
    size_board = input("Please enter the size board.\n")
    while not size_board.isdigit() or int(size_board) % 2 == 0:
        size_board = input("Boardsize should be greater than 2 and odd\nTry again\nPlease enter the size board.\n")
    size_board = int(size_board)
    board = Board(size_board)
    max_steps = size_board ** 2
    steps = 0
    while steps < max_steps:
        turn_to_walk = steps % 2 == 0
        step = input(f"Now goes player {first_player if turn_to_walk else second_player}\n").split()
        while step[0] != 'p' or step[0] != 'q' or not step[0].isdigit() or not step[1].isdigit() or\
            int(step[0]) < 0 or int(step[1]) < 0 or int(step[0]) >= board.size or int(step[1]) >= board.size:
            step = input(f"Try again\nNow goes player {first_player if turn_to_walk else second_player}\n").split()
        if step[0] == 'p' or step[0] == 'q':
            if step[0] == 'p':
                print(board)
            else:
                return 0
            continue
        coordinates = (int(step[0]), int(step[1]))
        try:
            board.put(coordinates, 0 if turn_to_walk else 1)
        except BoardPutExceptionExists:
            print("This coordinates already employed.")
            continue
        result = board.check_winner()
        if result != "nobody":
            print(f"The winner is {map_players[result]}.")
            print(board)
            return 0
        steps += 1
    print("This is a draw!")

execution()

# тесты захуячить получше
# пользовательский ввод проверить на валидацию
