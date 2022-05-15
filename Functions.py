import random

global columns
global rows
global number
number = 0
columns = 9
rows = 9
full_grid = [[0 for x in range(columns)] for y in range(rows)]
puzzle_grid = [[0 for x in range(columns)] for y in range(rows)]
solution_grid = [[0 for x in range(columns)] for y in range(rows)]


# checking if placement is valid
def is_valid(grid, row, col, candidate):
    # int i, j
    if grid[row][col] != 0:
        return False

    # check column
    for i in range(9):
        if i != row:
            if grid[i][col] == candidate:
                return False

    # check row
    for i in range(9):
        if i != col:
            if grid[row][i] == candidate:
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
                if grid[temp_row + i][temp_col + j] == candidate:
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


# check if the current grid is solvable
def is_sudoku_solvable(temp_grid):
    # if solvable return 1, if not return 0. if more than 1 solution (bad) return 2
    # int  i, j, num, k

    # find first blank square
    j, i = 0, 0
    while i < 9:
        j = 0
        while j < 9 and temp_grid[i][j] != 0:
            if j == 8:
                break
            else:
                j += 1
        if temp_grid[i][j] == 0:
            break
        else:
            i += 1
    # if there are no blank squares, the grid is solved, return 1
    if i == 9:
        return 1

    # Work in progress start
    """
    possible_numbers = []
    for i2 in range(9):
        for j2 in range(9):
            count = 0
            for num in range(1, 10):
                if is_valid(solution_grid, i2, j2, num):
                    count += 1
                if count == 1:
                    possible_numbers.append(num)
            for num in possible_numbers:
                if num 
            solution_grid[i2][j2] = num

    for row in range(9):
        for num in range(1, 10):
            for c1 in range(9):
                if solution_grid[row][c1] == 0:
                    while num not in solution_grid[row]:
                        count = 0
                        if is_valid(solution_grid, row, c1, num):
                            count += 1
            if count == 1:
                solution_grid[row][c1] = num
    """

    # Work in progress end

    k = 0
    for num in range(1, 10):
        if is_valid(temp_grid, i, j, num):
            temp_grid[i][j] = num
            k += is_sudoku_solvable(temp_grid)
            temp_grid[i][j] = 0
            if k == 2:
                return 2
    return k


# make a puzzle form the full grid
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


# solve solution grid
def solve_sudoku():
    # int i, j, num, k
    # find first blank square
    j, i = 0, 0
    while i < 9:
        j = 0
        while j < 9 and solution_grid[i][j] != 0:
            if j == 8:
                break
            else:
                j += 1
        if solution_grid[i][j] == 0:
            break
        else:
            i += 1

    # if there are no blank squares, the grid is solved, return 1
    if i == 9:
        return 1

    # Work in progress start
    """
    possible_numbers = []
    for i2 in range(9):
        for j2 in range(9):
            count = 0
            for num in range(1, 10):
                if is_valid(solution_grid, i2, j2, num):
                    count += 1
                if count == 1:
                    possible_numbers.append(num)
            for num in possible_numbers:
                if num 
            solution_grid[i2][j2] = num

    for row in range(9):
        for num in range(1, 10):
            for c1 in range(9):
                if solution_grid[row][c1] == 0:
                    while num not in solution_grid[row]:
                        count = 0
                        if is_valid(solution_grid, row, c1, num):
                            count += 1
            if count == 1:
                solution_grid[row][c1] = num
    """

    # Work in progress end

    k = 0
    for num in range(1, 10):
        if is_valid(solution_grid, i, j, num):
            solution_grid[i][j] = num
            k += solve_sudoku()
            if k == 0:
                solution_grid[i][j] = 0
    return k


# initialize solution grid
def solve_sudoku_puzzle():
    # int i, j
    for i in range(9):
        for j in range(9):
            solution_grid[i][j] = puzzle_grid[i][j]
    solve_sudoku()


def print_sudoku(print_grid):
    for i in range(9):
        for j in range(9):
            if print_grid[i][j] == 0:
                print('-', end=' ')
            else:
                print(print_grid[i][j], end=' ')
        print()


make_full_sudoku(0, 0)
make_puzzle()
solve_sudoku_puzzle()

print_sudoku(full_grid)
print(" ")
print(is_sudoku_solvable(full_grid))

print(" ")
print_sudoku(puzzle_grid)
print(" ")
print(is_sudoku_solvable(puzzle_grid))

print(" ")
print_sudoku(solution_grid)
print(" ")
print(is_sudoku_solvable(solution_grid))
