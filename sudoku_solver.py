puzzle = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
          [6, 0, 0, 0, 7, 5, 0, 0, 9],
          [0, 0, 0, 6, 0, 1, 0, 7, 8],
          [0, 0, 7, 0, 4, 0, 2, 6, 0],
          [0, 0, 1, 0, 5, 0, 9, 3, 0],
          [9, 0, 4, 0, 6, 0, 0, 0, 5],
          [0, 7, 0, 3, 0, 0, 0, 1, 2],
          [1, 2, 0, 0, 0, 7, 4, 0, 0],
          [0, 4, 9, 2, 0, 6, 0, 0, 7]]


def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("\n- - - - - - - - - - -", end=" ")
        for ii in range(len(sudoku[0])):
            if ii % 3 == 0 and ii != 0:
                print("|", end=" ")
            if ii == 0:
                print(f'\n{sudoku[i][ii]}', end=" ")
            else:
                print(sudoku[i][ii], end=" ")


def find_empty(sudoku):
    for i in range(len(sudoku)):
        for ii in range(len(sudoku[0])):
            if sudoku[i][ii] == 0:
                return i, ii


def valid(sudoku, number, position):
    for i in range(len(sudoku[0])):
        if sudoku[position[0]][i] == number and position[1] != i:
            return False

    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == number and position[0] != i:
            return False


print_sudoku(puzzle)
