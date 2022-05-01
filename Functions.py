import random

global columns
global rows
global number
number = 0
columns = 9
rows = 9
full_grid = [[0 for x in range(columns)] for y in range(rows)]
puzzle_grid = [[0 for x in range(columns)] for y in range(rows)]


# checking if placement is valid
def is_valid(full_grid, row, col, candidate):
    if full_grid[row][col] != 0:
        return False

    # check column
    for i in range(9):
        if i != row:
            if full_grid[i][col] == candidate:
                return False

    # check row
    for i in range(9):
        if i != col:
            if full_grid[row][i] == candidate:
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
                if full_grid[temp_row + i][temp_col + j] == candidate:
                    return False

    return True


# make new full sudoku board
def make_full_sudoku(row, col):
    candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 0
    # shuffle the first row
    random.shuffle(candidate)

    if (row == 8) and (col == 8):
        while (i <= 8) and (not is_valid(full_grid, row, col, candidate[i])):
            i += 1

        if i == 9:
            return False

        full_grid[8][8] = candidate[i]
        return True

    i = 0
    while i <= 8:
        if is_valid(full_grid, row, col, candidate[i]):
            full_grid[row][col] = candidate[i]
            if col == 8:
                finished = make_full_sudoku(row + 1, 0)
            else:
                finished = make_full_sudoku(row, col + 1)
            if not finished:
                full_grid[row][col] = 0
            else:
                return True
        i += 1

    return False


def is_sudoku_solvable(temp_grid):
    # if solvable return 1, if not return 0. if more than 1 solution (bad) return 2
    # int  i, j, num, k

    # find first blank square
    j = 0
    for i in range(9):
        while j < 9 and temp_grid[i][j] != 0:
            if j == 8:
                break
            j += 1
        if temp_grid[i][j] == 0:
            break

    # if there are no blank squares, the grid is solved, return 1
    if i == 9:
        return 1

    k = 0
    for num in range(1, 10):
        if is_valid(temp_grid, i, j, num):
            temp_grid[i][j] = num
            k += is_sudoku_solvable(temp_grid)
            temp_grid[i][j] = 0
            if k == 2:
                return 2
    return k


def make_puzzle():
    # int i, j, temp
    candidate_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    candidate_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(candidate_1)
    random.shuffle(candidate_2)

    for i in range(9):
        for j in range(9):
            puzzle_grid[i][j] = full_grid[i][j]

    for i in range(9):
        for j in range(9):
            temp = puzzle_grid[candidate_1[i] - 1][candidate_2[j] - 1]
            puzzle_grid[candidate_1[i] - 1][candidate_2[j] - 1] = 0
            if is_sudoku_solvable(puzzle_grid) != 1:
                puzzle_grid[candidate_1[i] - 1][candidate_2[j] - 1] = temp


"""
def solve_sudoku():


def solve_sudoku_puzzle():
    # int i, j
    for i in range(9):
        for j in range(9):
            solgrid[i][j] = puzgrid[i][j]
    return solve_sudoku()
"""

make_full_sudoku(0, 0)
make_puzzle()

i = 0
while i <= 8:
    print(full_grid[i])
    i += 1

print(" ")
print(is_sudoku_solvable(full_grid))

print(" ")
i = 0
while i <= 8:
    print(puzzle_grid[i])
    i += 1

print(" ")
print(is_sudoku_solvable(puzzle_grid))
