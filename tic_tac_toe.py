field = [[' ' for _ in range(3)] for _ in range(3)]


def print_field():  # Prints all content of the field`s current state
    for i in field:
        print(i)


def field_replace(axis_y_x: list, chosen_name_for_element: str):  # Replaces 1 field`s slot by income coordinates` list
    for i in range(len(field)):
        for j in range(len(field[i])):
            if i == axis_y_x[0] and j == axis_y_x[1]:
                field[i][j] = chosen_name_for_element


def moves_splitter(global_moves_order):  # Splits global list of moves into 2 lists of A and B player`s moves
    moves_a = []  # coordinates
    moves_b = []
    for i in range(len(global_moves_order)):
        if (i + 2) % 2 == 0:
            moves_a.append(global_moves_order[i])
        else:
            moves_b.append(global_moves_order[i])
    return moves_a, moves_b


def data_to_replace_by_player(lst: list, chosen_name_for_element: str):  # Receives list of moves, symbol and gives data
    for i in range(len(lst)):  # to field replacer
        field_replace(lst[i], chosen_name_for_element)
    return


def game_status(current_field):
    for i in range(len(current_field)):
        if len(current_field) == current_field[i].count('X'):
            print('Player A has won')
            print()
            return 1
        elif len(current_field) == current_field[i].count('O'):
            print('Player B has won')
            print()
            return 1
        else:
            if current_field[0][0] == current_field[1][1] == current_field[2][2]:
                if current_field[0][0] == 'X':
                    print('Player A has won')
                    return 1
                elif current_field[0][0] == 'O':
                    print('Player B has won')
                    return 1
            elif current_field[0][2] == current_field[1][1] == current_field[2][0]:
                if current_field[0][2] == 'X':
                    print('Player A has won')
                    return 1
                elif current_field[0][2] == 'O':
                    print('Player B has won')
                    return 1
            elif current_field[0][0] == current_field[1][0] == current_field[2][0]:
                if current_field[0][0] == 'X':
                    print('Player A has won')
                    return 1
                elif current_field[0][0] == 'O':
                    print('Player B has won')
                    return 1
            elif current_field[0][1] == current_field[1][1] == current_field[2][1]:
                if current_field[0][1] == 'X':
                    print('Player A has won')
                    return 1
                elif current_field[0][1] == 'O':
                    print('Player B has won')
                    return 1
            elif current_field[0][2] == current_field[1][2] == current_field[2][2]:
                if current_field[0][2] == 'X':
                    print('Player A has won')
                    return 1
                elif current_field[0][2] == 'O':
                    print('Player B has won')
                    return 1


def play():
    print(f'Coordinates(X.Y): \n[0.0][0.1][0.2]\n[1.0][1.1][1.2]\n[2.0][2.1][2.2]')
    moves = []
    while len(moves) < 9:
        if game_status(field) != 1:
            if len(moves) % 2 == 0:
                coordinates = input('Player A, input coordinates in format X.Y:').split('.')
            else:
                coordinates = input('Player B, input coordinates in format X.Y:').split('.')
            for i in range(len(coordinates)):
                coordinates[i] = int(coordinates[i])
            moves.append(coordinates)
            moves_aa, moves_bb = moves_splitter(moves)
            moves_splitter(moves)
            data_to_replace_by_player(moves_aa, 'X')
            data_to_replace_by_player(moves_bb, 'O')
            print_field()
            game_status(field)
        else:
            break
        print('Pending')
    if len(moves) == 9:
        print('Draw')


play()
