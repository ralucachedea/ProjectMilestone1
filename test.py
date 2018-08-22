# 1. write a function that print out the matrix 3x3
# 2. function that can take the player input and assign their marker as 'X' or '0'
# 3. function where the user can mark his choice: row, column, x or zero
# 4. check the win
# 5. what users starts first -> random
# 6. check if there are free spaces in matrix
# 7. check the matrix is full
# 8. ask the user his next position. check if the position is free in matrix

x_turn = True
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
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
#def win_validation()

if __name__ == "__main__":
    matrix_print(matrix)
    users_turn()
    #user_input()
    matrix_print(matrix)







