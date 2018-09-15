# 1. write a function that print out the matrix 3x3
# 2. function that can take the player input and assign their marker as 'X' or '0'
# 3. function where the user can mark his choice: row, column, x or zero
# 4. check the win
# 5. what users starts first -> random
# 6. check if there are free spaces in matrix
# 7. check the matrix is full
# 8. ask the user his next position. check if the position is free in matrix

'''
ai nevoie de o funcție pentru început
dev check_win(matrix, player):
care returnează un rezultat boolean
o parcurgi cu 2 foruri
for în for
unul pentru linii și unul pentru coloane
care determină dacă o matrice bidimensională are aceleași valori pe una dintre linii, coloane sau diagonală

ce valori trebuie să aibă indecșii elementelor de pe diagonala principală a unei matrici? dar de pe cea secundară?
indecșii elementelor de pe diagonala principală trebuie să fie egali
suna indecșilor de pe diagonala secundară trebuie să fie tot timpul egală cu min(nr_linii, nr_coloane)

'''
x_turn = True
matrix = [['x', '2', 'x'], ['x', '5', '6'], ['x', '0', '9']]
game_on = True

def matrix_print(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()


def users_turn():
    global x_turn
    global game_on

    while game_on:
        if x_turn:
            print("It's X's turn: ")
        else:
            print("It's 0's turn: ")
        validation_result = False
        while not validation_result:
            user_row = input('Add the row number: ')
            user_column = input('Add the column number: ')
            validation_result = input_validation(user_row,user_column,matrix)

        if x_turn:
            matrix[int(user_row)][int(user_column)] = 'X'
        else:
            matrix[int(user_row)][int(user_column)] = '0'
        x_turn = not x_turn
        matrix_print(matrix)


def input_validation(user_row,user_column,matrix):
    """
    the function checks the user's inputs
    :param user_row:
    :param user_column:
    :param matrix:
    :return: return True if the input is valid or False if the input is invalid
    """
    try:
        int_row = int(user_row)
    except NameError:
        print("value added for the row: {} is not in range (0,2)".format(user_row))
        return False
    except TypeError:
        print("value added for the row: {} is not in range (0,2)".format(user_row))
        return False
    except SyntaxError:
        print("value added for the row: {} is not in range (0,2)".format(user_row))
        return False
    except ValueError:
        print("value added for the row: {} is not in range (0,2)".format(user_row))
        return False

    try:
        int_column = int(user_column)
    except NameError:
        print("value added for the column: {} is not in range (0,2)".format(user_column))
        return False
    except TypeError:
        print("value added for the column: {} is not in range (0,2)".format(user_column))
        return False
    except SyntaxError:
        print("value added for the column: {} is not in range (0,2)".format(user_column))
        return False
    except ValueError:
        print("value added for the column: {} is not in range (0,2)".format(user_column))
        return False
    if int_row not in range(0,3):
        print("value added for the row: {} is not in range (0,2)".format(user_row))
        return False
    elif int_column not in range(0,3):
        print("value added for the column: {} is not in range (0,2)".format(user_column))
        return False

    if matrix[int_row][int_column] == 'X' or matrix[int_row][int_column] == '0':
        print("The position is already taken!! Please add another number")
        return False
    return True


def win_validation(matrix, player):
    """
    The function checks if the user wins the game
    The function checks if all positions were occuped and the game is over
    :param matrix:
    :param player:
    :return: True if all position are occuped with the same mark
    """
    diagonal_counter = 0
    diagonal_sec_counter = 0
    column_counter = [0, 0, 0]
    for row_index in range(len(matrix)):
        line_counter = 0
        # main diagonal check
        if matrix[row_index][row_index] == player:
            diagonal_counter += 1
        if diagonal_counter == 3:
            print("User {} has won, see diagonal".format(player))
            return True
        for column_index in range(len(matrix)):
            if matrix[row_index][column_index] == player:
                line_counter += 1
                # secondary diagonal check
                if (row_index + column_index) == 2:
                    diagonal_sec_counter += 1
                    if diagonal_sec_counter == 3:
                        print(f"User {player} has won, see secondary diagonal")
                        return True
                # column check
                column_counter[column_index] += 1
                if column_counter[column_index] == 3:
                    print(f"User {player} has won, see column {column_index}")
                    return True
            else:
                line_counter = 0
        # line check
        if line_counter == 3:
            print("User {} has won, see line {}".format(player, row_index))
            return True

    return False
def check_available_positions(matrix):
    for row_index in range(len(matrix)):
        for column_index in range(len(matrix)):
            if matrix[row_index][column_index]!='x' and matrix[row_index][column_index]!='0':
                return False
    return True

if __name__ == "__main__":
    matrix_print(matrix)
    # users_turn()
    #user_input()
    # matrix_print(matrix)
    win_evaluation_result = win_validation(matrix, 'x')
    print(win_evaluation_result)
    # win_validation_res = check_available_positions(matrix)
    # print(win_validation_res)






