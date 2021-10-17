from homework_1.tic_tac_toe import Board


def execution():
    help = "If you want to print board please press p.\nIf you want to quit please press q."
    print("Start game.")
    print(help)
    first_player, second_player = input("Please enter the name first player.\n"), input("Please enter the name second player.\n")
    map_players = {'x': first_player, 'o': second_player}
    size_board = int(input("Please enter the size board.\n"))
    board = Board(size_board)
    max_steps = size_board ** 2
    steps = 0
    while steps < max_steps:
        turn_to_walk = steps % 2 == 0
        step = input(f"Now goes player {first_player if turn_to_walk else second_player}\n").split()
        if step[0] == 'p' or step[0] == 'q':
            if step[0] == 'p':
                print(board)
            else:
                return 0
            continue
        coordinates = (int(step[0]), int(step[1]))
        board.put(coordinates, 0 if turn_to_walk else 1)
        result = board.check_winner()
        if result != "nobody":
            print(f"The winner is {map_players[result]}.")
            print(board)
            return 0
        steps += 1
    print("This is a draw!")
