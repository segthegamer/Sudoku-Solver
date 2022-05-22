import random
import pygame
import Gui


def find_options(temp_grid):
    # Update known number's options
    for i in range(9):
        for j in range(9):
            if temp_grid[i][j].number != 0:
                temp_grid[i][j].options = {temp_grid[i][j].number}

    # Update unknown number's options
    for i in range(9):
        for j in range(9):
            if temp_grid[i][j].number == 0:
                for num in range(1, 10):
                    if not is_valid(temp_grid, i, j, num):
                        if num in temp_grid[i][j].options:
                            temp_grid[i][j].options.remove(num)


def reload_options(temp_grid):
    for i in range(9):
        for j in range(9):
            temp_grid[i][j].options = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    find_options(temp_grid)


def remove_options(temp_grid, row, col):
    # Update the current number
    if temp_grid[row][col].number != 0:
        temp_grid[row][col].options = {temp_grid[row][col].number}

        # Check column
        for i in range(9):
            if i != row:
                if temp_grid[i][col].number == 0:
                    if temp_grid[row][col].number in temp_grid[i][col].options:
                        temp_grid[i][col].options.remove(temp_grid[row][col].number)
                        if not temp_grid[i][col].options:
                            return False

        # Check row
        for i in range(9):
            if i != col:
                if temp_grid[row][i].number == 0:
                    if temp_grid[row][col].number in temp_grid[row][i].options:
                        temp_grid[row][i].options.remove(temp_grid[row][col].number)
                        if not temp_grid[row][i].options:
                            return False

        # Check squares
        temp_row = (row // 3) * 3
        temp_col = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                if (temp_row + i != row) or (temp_col + j != col):
                    if temp_grid[temp_row + i][temp_col + j].number == 0:
                        if temp_grid[row][col].number in temp_grid[temp_row + i][temp_col + j].options:
                            temp_grid[temp_row + i][temp_col + j].options.remove(temp_grid[row][col].number)
                            if not temp_grid[temp_row + i][temp_col + j].options:
                                return False
    return True


def add_options(temp_grid, row, col):
    # Update the current number
    if temp_grid[row][col].number != 0:
        temp_grid[row][col].options = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        temp_grid[row][col].options.remove(temp_grid[row][col].number)
        for num in range(1, 10):
            if not is_valid(temp_grid, row, col, num):
                if num in temp_grid[row][col].options:
                    temp_grid[row][col].options.remove(num)

        # Check column
        for i in range(9):
            if i != row:
                if temp_grid[i][col].number == 0:
                    if temp_grid[row][col].number not in temp_grid[i][col].options:
                        if is_valid(temp_grid, i, col, temp_grid[row][col].number):
                            temp_grid[i][col].options.append(temp_grid[row][col].number)

        # Check row
        for i in range(9):
            if i != col:
                if temp_grid[row][i].number == 0:
                    if temp_grid[row][col].number not in temp_grid[row][i].options:
                        if is_valid(temp_grid, row, i, temp_grid[row][col].number):
                            temp_grid[row][i].options.append(temp_grid[row][col].number)

        # Check squares
        temp_row = (row // 3) * 3
        temp_col = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                if (temp_row + i != row) or (temp_col + j != col):
                    if temp_grid[temp_row + i][temp_col + j].number == 0:
                        if temp_grid[row][col].number not in temp_grid[temp_row + i][temp_col + j].options:
                            if is_valid(temp_grid, temp_row + i, temp_col + j, temp_grid[row][col].number):
                                temp_grid[temp_row + i][temp_col + j].options.append(temp_grid[row][col].number)


# Graphics end

# Check if grid is full
def find_blank(temp_grid):
    # If there are no blank squares, the grid is solved, return True else return False
    j, i = 0, 0
    while temp_grid[i][j].number != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    return False


# Checking if placement is valid
def is_valid(temp_grid, row, col, candidate):
    # int i, j
    if temp_grid[row][col].number != 0:
        return False

    # Check column
    for i in range(9):
        if i != row:
            if temp_grid[i][col].number == candidate:
                return False

    # Check row
    for i in range(9):
        if i != col:
            if temp_grid[row][i].number == candidate:
                return False

    # Check squares
    temp_row = (row // 3) * 3
    temp_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if (temp_row + i != row) or (temp_col + j != col):
                if temp_grid[temp_row + i][temp_col + j].number == candidate:
                    return False

    return True


# Make new full sudoku board
def make_full_sudoku(temp_grid, row, col):
    candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 0

    # Shuffle the first row
    random.shuffle(candidate)

    if (row == 8) and (col == 8):
        while (i <= 8) and (not is_valid(temp_grid, row, col, candidate[i])):
            i += 1

        if i == 9:
            return False

        temp_grid[8][8].number = candidate[i]
        return True

    i = 0
    while i <= 8:
        if is_valid(temp_grid, row, col, candidate[i]):
            temp_grid[row][col].number = candidate[i]
            if col == 8:
                finished = make_full_sudoku(temp_grid, row + 1, 0)
            else:
                finished = make_full_sudoku(temp_grid, row, col + 1)
            if not finished:
                temp_grid[row][col].number = 0
            else:
                return True
        i += 1

    return False


# Check if the current grid is solvable
def is_sudoku_solvable(temp_grid):
    # if solvable return 1, if not return 0. if more than 1 solution (bad) return 2
    # int  i, j, num, k
    # find first blank square
    j, i = 0, 0
    while i < 9:
        j = 0
        while j < 9 and temp_grid[i][j].number != 0:
            if j == 8:
                break
            else:
                j += 1
        if temp_grid[i][j].number == 0:
            break
        else:
            i += 1
    # if there are no blank squares, the grid is solved, return 1
    if i == 9:
        return 1

    k = 0
    for num in temp_grid[i][j].options:
        if is_valid(temp_grid, i, j, num):
            temp_grid[i][j].number = num
            k += is_sudoku_solvable(temp_grid)
            temp_grid[i][j].number = 0
            if k == 2:
                return 2
    return k


# Make a puzzle from the full grid
def make_puzzle(temp_grid, difficulty):
    candidate_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    candidate_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(candidate_1)
    random.shuffle(candidate_2)
    if difficulty == 0:
        maximum = 41
    if difficulty == 1:
        maximum = 46
    if difficulty == 2:
        maximum = 51
    if difficulty == 3:
        maximum = 64

    counter = 0
    for i in range(9):
        for j in range(9):
            if counter >= maximum:
                break
            temp = temp_grid[candidate_1[i] - 1][candidate_2[j] - 1].number
            temp_grid[candidate_1[i] - 1][candidate_2[j] - 1].number = 0
            counter += 1
            if is_sudoku_solvable(temp_grid) != 1:
                temp_grid[candidate_1[i] - 1][candidate_2[j] - 1].number = temp
                counter -= 1


# Solve grid using backtracking with constraint propagation
def solve_sudoku_constraint_propagation(temp_grid):
    # Find first blank square
    j, i = 0, 0
    while i < 9:
        j = 0
        while j < 9 and temp_grid[i][j].number != 0:
            if j == 8:
                break
            else:
                j += 1
        if temp_grid[i][j].number == 0:
            break
        else:
            i += 1

    # if there are no blank squares, the grid is solved, return 1
    if i == 9:
        return 1
    pygame.event.pump()

    k = 0
    for num in temp_grid[i][j].options:
        if is_valid(temp_grid, i, j, num):
            temp_grid[i][j].number = num
            remove_options(temp_grid, i, j)
            Gui.screen.fill((255, 255, 255))
            Gui.draw_sudoku(temp_grid)
            Gui.draw_box(i, j)
            pygame.display.update()
            #            pygame.time.delay(1)
            k += solve_sudoku_constraint_propagation(temp_grid)
            if k == 0:
                temp_grid[i][j].number = 0
                reload_options(temp_grid)
    return k


def get_min_options(temp_grid, x, y):
    minimum = 0
    for i in range(9):
        for j in range(9):
            if temp_grid[i][j].number == 0:
                if len(temp_grid[i][j].options) > minimum:
                    minimum = len(temp_grid[i][j].options)
                    x = i
                    y = j
    return x, y


def solve_sudoku_variable_ordering(temp_grid):
    # Find first blank square
    j, i = 0, 0
    i, j = get_min_options(temp_grid, i, j)
    while i < 9:
        j = 0
        while j < 9 and temp_grid[i][j].number != 0:
            if j == 8:
                break
            else:
                j += 1
        if temp_grid[i][j].number == 0:
            break
        else:
            i += 1

    # If there are no blank squares, the grid is solved, return 1
    if i == 9:
        return 1
    pygame.event.pump()

    k = 0
    for num in range(1, 10):
        if is_valid(temp_grid, i, j, num):
            temp_grid[i][j].number = num
            Gui.screen.fill((255, 255, 255))
            Gui.draw_sudoku(temp_grid)
            Gui.draw_box(i, j)
            pygame.display.update()
            #            pygame.time.delay(1)
            k += solve_sudoku_variable_ordering(temp_grid)
            if k == 0:
                temp_grid[i][j].number = 0
    return k


# Solve grid using only backtracking
def solve_sudoku_backtracking(temp_grid):
    # Find first blank square
    j, i = 0, 0
    while i < 9:
        j = 0
        while j < 9 and temp_grid[i][j].number != 0:
            if j == 8:
                break
            else:
                j += 1
        if temp_grid[i][j].number == 0:
            break
        else:
            i += 1

    # If there are no blank squares, the grid is solved, return 1
    if i == 9:
        return 1
    pygame.event.pump()

    k = 0
    for num in range(1, 10):
        if is_valid(temp_grid, i, j, num):
            temp_grid[i][j].number = num
            Gui.screen.fill((255, 255, 255))
            Gui.draw_sudoku(temp_grid)
            Gui.draw_box(i, j)
            pygame.display.update()
            #            pygame.time.delay(1)
            k += solve_sudoku_backtracking(temp_grid)
            if k == 0:
                temp_grid[i][j].number = 0
    return k
