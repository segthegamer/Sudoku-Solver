import random

global fullgrid
global columns
global rows
columns = 9
rows = 9
fullgrid = [[0 for x in range(columns)] for y in range(rows)]


# checking if placement is valid
def is_valid(row, col, candidate):
    # checking no copies in same row or column
    temp_row, temp_col = 0, 0
    while 8 >= temp_row >= 0:
        if fullgrid[temp_row][col] == candidate:
            return False
        temp_row += 1
    while 8 >= temp_col >= 0:
        if fullgrid[row][temp_col] == candidate:
            return False
        temp_col += 1

    # checking no copies in same square
    # 1 square
    if 2 >= row and col >= 0:
        temp_row, temp_col = 0, 0
        while 2 >= temp_row >= 0:
            while 2 >= temp_col >= 0:
                if fullgrid[temp_row][temp_col] == candidate:
                    return False
                temp_col += 1
            temp_row += 1
    # 2 square
    if (2 >= row >= 0) and (5 >= col >= 3):
        temp_row, temp_col = 0, 3
        while 2 >= temp_row >= 0:
            while 5 >= temp_col >= 3:
                if fullgrid[temp_row][temp_col] == candidate:
                    return False
                temp_col += 1
            temp_row += 1
    # 3 square
    if (2 >= row >= 0) and (8 >= col >= 6):
        temp_row, temp_col = 0, 6
        while 2 >= temp_row >= 0:
            while 8 >= temp_col >= 6:
                if fullgrid[temp_row][temp_col] == candidate:
                    return False
                temp_col += 1
            temp_row += 1
    # 4 square
    if (5 >= row >= 3) and (2 >= col >= 0):
        temp_row, temp_col = 3, 0
        while 5 >= temp_row >= 3:
            while 2 >= temp_col >= 0:
                if fullgrid[temp_row][temp_col] == candidate:
                    return False
                temp_col += 1
            temp_row += 1
    # 5 square
    if 5 >= row and col >= 3:
        temp_row, temp_col = 3, 3
        while 5 >= temp_row >= 3:
            while 5 >= temp_col >= 3:
                if fullgrid[temp_row][temp_col] == candidate:
                    return False
                temp_col += 1
            temp_row += 1
    # 6 square
    if (5 >= row >= 3) and (8 >= col >= 6):
        temp_row, temp_col = 3, 6
        while 5 >= temp_row >= 3:
            while 8 >= temp_col >= 6:
                if fullgrid[temp_row][temp_col] == candidate:
                    return False
                temp_col += 1
            temp_row += 1
    # 7 square
    if (8 >= row >= 6) and (2 >= col >= 0):
        temp_row, temp_col = 6, 0
        while 8 >= temp_row >= 6:
            while 2 >= temp_col >= 0:
                if fullgrid[temp_row][temp_col] == candidate:
                    return False
                temp_col += 1
            temp_row += 1
    # 8 square
    if (8 >= row >= 6) and (5 >= col >= 3):
        temp_row, temp_col = 6, 3
        while 8 >= temp_row >= 6:
            while 5 >= temp_col >= 3:
                if fullgrid[temp_row][temp_col] == candidate:
                    return False
                temp_col += 1
            temp_row += 1
    # 9 square
    if 8 >= row and col >= 6:
        temp_row, temp_col = 6, 6
        while 8 >= temp_row >= 6:
            while 8 >= temp_col >= 6:
                if fullgrid[temp_row][temp_col] == candidate:
                    return False
                temp_col += 1
            temp_row += 1
    return True


# shuffling first row
def shuffle_row(row):
    temp_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 0
    while i < 9:
        temp = random.randrange(1, 10)
        while temp not in temp_row:
            temp = random.randrange(1, 10)
        temp_row.remove(temp)
        row[i] = temp
        i += 1
    return row


# make brand new full sudoku board
def make_full_sudoku(row, col):
    candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 0
    candidate = shuffle_row(candidate)
    #    print(candidate)

    if row == 8 and col == 8:
        while (not is_valid(row, col, candidate[i])) and (i <= 8):
            i += 1

        if i == 9:
            return False

        fullgrid[8][8] = candidate[i]
        return True

    while i <= 8:
        if is_valid(row, col, candidate[i]):
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


make_full_sudoku(8, 0)
i = 0
while i <= 8:
    print(fullgrid[i])
    i += 1
