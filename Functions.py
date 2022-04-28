import random

global fullgrid
global columns
global rows
global num
num = 0
columns = 9
rows = 9
fullgrid = [[0 for x in range(columns)] for y in range(rows)]


# checking if placement is valid
def is_valid(fullgrid, row, col, candidate):
    if fullgrid[row][col] != 0:
        return False

    # check column
    for i in range(9):
        if i != row:
            if fullgrid[i][col] == candidate:
                return False

    # check row
    for i in range(9):
        if i != col:
            if fullgrid[row][i] == candidate:
                return False

    # check squares
    temp_row = row / 3
    temp_row = int(temp_row)
    temp_row = temp_row * 3

    temp_col = col / 3
    temp_col = int(temp_col)
    temp_col = temp_col * 3

    for i in range(3):
        for j in range(3):
            if (temp_row + i != row) or (temp_col + j != col):
                if fullgrid[temp_row + i][temp_col + j] == candidate:
                    return False

    return True


# make new full sudoku board
def make_full_sudoku(row, col):
    candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 0
    # shuffle the first row
    random.shuffle(candidate)

    if (row == 8) and (col == 8):
        while (i <= 8) and (not is_valid(fullgrid, row, col, candidate[i])):
            i += 1

        if i == 9:
            return False

        fullgrid[8][8] = candidate[i]
        return True

    i = 0
    while i <= 8:
        if is_valid(fullgrid, row, col, candidate[i]):
            fullgrid[row][col] = candidate[i]
            if col == 8:
                finished = make_full_sudoku(row + 1, 0)
            else:
                finished = make_full_sudoku(row, col + 1)
            if not finished:
                fullgrid[row][col] = 0
            else:
                return True
        i += 1

    return False


def is_sudoku_solvable():
    # if solvable return 1, if not return 0. if more than 1 solution (bad) return 2
    # int  i, j, num, k
    tempgrid = fullgrid

    # find first blank square
    i = j = 0
    for i in range(9):
        for j in range(9) and tempgrid[i][j] != 0:
            if j == 8:
                break
        if tempgrid[i][j] == 0:
            break

    # if there ar eno blank squares, the grid is solved, return 1
    if i == 9:
        return 1

    k = 0
    num = 1
    for num in range(10):
        if (is_valid())

make_full_sudoku(0, 0)

i = 0
while i <= 8:
    print(fullgrid[i])
    i += 1
