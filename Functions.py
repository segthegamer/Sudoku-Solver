import random
import pygame

global columns
global rows
global grid

columns = 9
rows = 9


class Square:
    def __init__(self):
        self.number = 0
        self.options = {1, 2, 3, 4, 5, 6, 7, 8, 9}


grid = [[Square() for x in range(columns)] for y in range(rows)]

# pygame start
pygame.font.init()

# change values
# screen
pygame.display.set_caption("Sudoku Solver")
screen = pygame.display.set_mode((500, 600))
icon = pygame.image.load('sudoku_icon.png')
pygame.display.set_icon(icon)
display_x = 0
display_y = 0
display_diff = 500 / 9
display_val = 0

# fonts
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 18)


def find_options():
    # Update known number's options
    for i in range(9):
        for j in range(9):
            if grid[i][j].number != 0:
                grid[i][j].options = {grid[i][j].number}

    # Update unknown number's options
    for i in range(9):
        for j in range(9):
            if grid[i][j].number == 0:
                for num in range(1, 10):
                    if not is_valid(grid, i, j, num):
                        if num in grid[i][j].options:
                            grid[i][j].options.remove(num)


def reload_options():
    for i in range(9):
        for j in range(9):
            grid[i][j].options = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    find_options()


def remove_options(row, col):
    # Update the current number
    if grid[row][col].number != 0:
        grid[row][col].options = {grid[row][col].number}

        # Check column
        for i in range(9):
            if i != row:
                if grid[i][col].number == 0:
                    if grid[row][col].number in grid[i][col].options:
                        grid[i][col].options.remove(grid[row][col].number)
                        if not grid[i][col].options:
                            return False

        # Check row
        for i in range(9):
            if i != col:
                if grid[row][i].number == 0:
                    if grid[row][col].number in grid[row][i].options:
                        grid[row][i].options.remove(grid[row][col].number)
                        if not grid[row][i].options:
                            return False

        # Check squares
        temp_row = (row // 3) * 3
        temp_col = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                if (temp_row + i != row) or (temp_col + j != col):
                    if grid[temp_row + i][temp_col + j].number == 0:
                        if grid[row][col].number in grid[temp_row + i][temp_col + j].options:
                            grid[temp_row + i][temp_col + j].options.remove(grid[row][col].number)
                            if not grid[temp_row + i][temp_col + j].options:
                                return False
    return True


def add_options(row, col):
    # Update the current number
    if grid[row][col].number != 0:
        grid[row][col].options = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        grid[row][col].options.remove(grid[row][col].number)
        for num in range(1, 10):
            if not is_valid(grid, row, col, num):
                if num in grid[row][col].options:
                    grid[row][col].options.remove(num)

        # Check column
        for i in range(9):
            if i != row:
                if grid[i][col].number == 0:
                    if grid[row][col].number not in grid[i][col].options:
                        if is_valid(grid, i, col, grid[row][col].number):
                            grid[i][col].options.append(grid[row][col].number)

        # Check row
        for i in range(9):
            if i != col:
                if grid[row][i].number == 0:
                    if grid[row][col].number not in grid[row][i].options:
                        if is_valid(grid, row, i, grid[row][col].number):
                            grid[row][i].options.append(grid[row][col].number)

        # Check squares
        temp_row = (row // 3) * 3
        temp_col = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                if (temp_row + i != row) or (temp_col + j != col):
                    if grid[temp_row + i][temp_col + j].number == 0:
                        if grid[row][col].number not in grid[temp_row + i][temp_col + j].options:
                            if is_valid(grid, temp_row + i, temp_col + j, grid[row][col].number):
                                grid[temp_row + i][temp_col + j].options.append(grid[row][col].number)


# Graphics
def get_cord(pos):
    global display_x
    display_x = pos[0] // display_diff
    global display_y
    display_y = pos[1] // display_diff


# Draw sudoku grid
def draw_sudoku(temp_grid):
    # Draw the lines

    for i in range(9):
        for j in range(9):
            if temp_grid[i][j].number != 0:
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (0, 153, 153),
                                 (i * display_diff, j * display_diff, display_diff + 1, display_diff + 1))

                # Fill grid with default numbers specified
                text1 = font1.render(str(temp_grid[i][j].number), 1, (0, 0, 0))
                screen.blit(text1, (i * display_diff + 15, j * display_diff + 15))

    # Draw lines horizontally and vertically to form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * display_diff), (500, i * display_diff), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * display_diff, 0), (i * display_diff, 500), thick)

    # Fill value entered in cell


def draw_val(display_val):
    text1 = font1.render(str(display_val), 1, (0, 0, 0))
    screen.blit(text1, (display_x * display_diff + 15, display_y * display_diff + 15))


# Cell highlighting
def draw_box(display_x, display_y):
    if (0 <= display_x < 9) and (0 <= display_y < 9):
        for i in range(2):
            pygame.draw.line(screen, (255, 0, 0), (display_x * display_diff - 3, (display_y + i) * display_diff),
                             (display_x * display_diff + display_diff + 3, (display_y + i) * display_diff), 7)
            pygame.draw.line(screen, (255, 0, 0), ((display_x + i) * display_diff, display_y * display_diff),
                             ((display_x + i) * display_diff, display_y * display_diff + display_diff), 7)


# Raise error when wrong value entered
def raise_error1():
    text1 = font1.render("Sudoku is unsolvable", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


def raise_error2():
    text1 = font1.render("Invalid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


def raise_error3():
    text1 = font1.render("Sudoku is solvable", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


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
def make_full_sudoku(row, col):
    candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 0

    # Shuffle the first row
    random.shuffle(candidate)

    if (row == 8) and (col == 8):
        while (i <= 8) and (not is_valid(grid, row, col, candidate[i])):
            i += 1

        if i == 9:
            return False

        grid[8][8].number = candidate[i]
        return True

    i = 0
    while i <= 8:
        if is_valid(grid, row, col, candidate[i]):
            grid[row][col].number = candidate[i]
            if col == 8:
                finished = make_full_sudoku(row + 1, 0)
            else:
                finished = make_full_sudoku(row, col + 1)
            if not finished:
                grid[row][col].number = 0
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
    for num in grid[i][j].options:
        if is_valid(temp_grid, i, j, num):
            temp_grid[i][j].number = num
            k += is_sudoku_solvable(temp_grid)
            temp_grid[i][j].number = 0
            if k == 2:
                return 2
    return k


# Make a puzzle from the full grid
def make_puzzle(difficulty):
    candidate_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    candidate_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(candidate_1)
    random.shuffle(candidate_2)
    if difficulty == 0:
        max = 41
    if difficulty == 1:
        max = 46
    if difficulty == 2:
        max = 51
    if difficulty == 3:
        max = 64

    counter = 0
    for i in range(9):
        for j in range(9):
            if counter >= max:
                break
            temp = grid[candidate_1[i] - 1][candidate_2[j] - 1].number
            grid[candidate_1[i] - 1][candidate_2[j] - 1].number = 0
            counter += 1
            if is_sudoku_solvable(grid) != 1:
                grid[candidate_1[i] - 1][candidate_2[j] - 1].number = temp
                counter -= 1


# Solve grid using backtracking with constraint propagation
def solve_sudoku_constraint_propagation():
    # Find first blank square
    j, i = 0, 0
    while i < 9:
        j = 0
        while j < 9 and grid[i][j].number != 0:
            if j == 8:
                break
            else:
                j += 1
        if grid[i][j].number == 0:
            break
        else:
            i += 1

    # if there are no blank squares, the grid is solved, return 1
    if i == 9:
        return 1
    pygame.event.pump()

    k = 0
    for num in grid[i][j].options:
        if is_valid(grid, i, j, num):
            grid[i][j].number = num
            remove_options(i, j)
            screen.fill((255, 255, 255))
            draw_sudoku(grid)
            draw_box(i, j)
            pygame.display.update()
            #            pygame.time.delay(1)
            k += solve_sudoku_constraint_propagation()
            if k == 0:
                grid[i][j].number = 0
                reload_options()
    return k


def get_min_options(x, y):
    minimum = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j].number == 0:
                if len(grid[i][j].options) > minimum:
                    minimum = len(grid[i][j].options)
                    x = i
                    y = j
    return x, y


def solve_sudoku_variable_ordering():
    # Find first blank square
    j, i = 0, 0
    i, j = get_min_options(i, j)
    while i < 9:
        j = 0
        while j < 9 and grid[i][j].number != 0:
            if j == 8:
                break
            else:
                j += 1
        if grid[i][j].number == 0:
            break
        else:
            i += 1

    # If there are no blank squares, the grid is solved, return 1
    if i == 9:
        return 1
    pygame.event.pump()

    k = 0
    for num in range(1, 10):
        if is_valid(grid, i, j, num):
            grid[i][j].number = num
            screen.fill((255, 255, 255))
            draw_sudoku(grid)
            draw_box(i, j)
            pygame.display.update()
            #            pygame.time.delay(1)
            k += solve_sudoku_variable_ordering()
            if k == 0:
                grid[i][j].number = 0
    return k


# Solve grid using only backtracking
def solve_sudoku_backtracking():
    # Find first blank square
    j, i = 0, 0
    while i < 9:
        j = 0
        while j < 9 and grid[i][j].number != 0:
            if j == 8:
                break
            else:
                j += 1
        if grid[i][j].number == 0:
            break
        else:
            i += 1

    # If there are no blank squares, the grid is solved, return 1
    if i == 9:
        return 1
    pygame.event.pump()

    k = 0
    for num in range(1, 10):
        if is_valid(grid, i, j, num):
            grid[i][j].number = num
            screen.fill((255, 255, 255))
            draw_sudoku(grid)
            draw_box(i, j)
            pygame.display.update()
            #            pygame.time.delay(1)
            k += solve_sudoku_backtracking()
            if k == 0:
                grid[i][j].number = 0
    return k


# Print puzzle on screen
def print_sudoku(print_grid):
    for i in range(9):
        for j in range(9):
            if print_grid[i][j].number == 0:
                print('-', end=' ')
            else:
                print(print_grid[i][j].number, end=' ')
        print()


# Print all square options on screen
def print_sudoku_options(print_grid):
    for i in range(9):
        for j in range(9):
            print(print_grid[i][j].options, end=' ')
        print()


# Display instruction for the game
def instruction():
    text1 = font2.render("Press R to empty board, H J K L difficulty, I to check if solvable, S to solve, B backtrack",
                         1,
                         (0, 0, 0))
    text2 = font2.render("Use the left mouse button and arrow keys, enter a value, C to clear placement", 1, (0, 0, 0))
    screen.blit(text1, (1, 520))
    screen.blit(text2, (1, 540))


# Display finished when solved
def result():
    text1 = font1.render("Game is finished", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


# Starting values for gui
run = True
move = 0
solvable = 1
print_solvable = 0
full_board = 0

# Game loop
while run:
    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False
        # Get the mouse position to insert number
        if event.type == pygame.MOUSEBUTTONDOWN:
            display_val = 0
            move = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        # Get the number to be inserted if key pressed
        if event.type == pygame.KEYDOWN:
            solvable = 1
            print_solvable = 0
            display_val = 0
            if event.key == pygame.K_LEFT:
                display_x -= 1
                move = 1
            if event.key == pygame.K_RIGHT:
                display_x += 1
                move = 1
            if event.key == pygame.K_UP:
                display_y -= 1
                move = 1
            if event.key == pygame.K_DOWN:
                display_y += 1
                move = 1
            if event.key == pygame.K_1:
                display_val = 1
            if event.key == pygame.K_2:
                display_val = 2
            if event.key == pygame.K_3:
                display_val = 3
            if event.key == pygame.K_4:
                display_val = 4
            if event.key == pygame.K_5:
                display_val = 5
            if event.key == pygame.K_6:
                display_val = 6
            if event.key == pygame.K_7:
                display_val = 7
            if event.key == pygame.K_8:
                display_val = 8
            if event.key == pygame.K_9:
                display_val = 9

            # If I pressed show if sudoku is solvable
            if (event.key == pygame.K_i) and (full_board == 0):
                if is_sudoku_solvable(grid) != 1:
                    solvable = 0
                else:
                    print_solvable = 1

            # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                full_board = 0
                grid = [[Square() for x in range(columns)] for y in range(rows)]

            # If H is pressed start new easy game
            if event.key == pygame.K_h:
                full_board = 0
                grid = [[Square() for x in range(columns)] for y in range(rows)]
                make_full_sudoku(0, 0)
                make_puzzle(0)
                find_options()

            # If J is pressed start new normal game
            if event.key == pygame.K_j:
                full_board = 0
                grid = [[Square() for x in range(columns)] for y in range(rows)]
                make_full_sudoku(0, 0)
                make_puzzle(1)
                find_options()

            # If K is pressed start hard new game
            if event.key == pygame.K_k:
                full_board = 0
                grid = [[Square() for x in range(columns)] for y in range(rows)]
                make_full_sudoku(0, 0)
                make_puzzle(2)
                find_options()

            # If L is pressed start new impossible game
            if event.key == pygame.K_l:
                full_board = 0
                grid = [[Square() for x in range(columns)] for y in range(rows)]
                make_full_sudoku(0, 0)
                make_puzzle(3)
                find_options()

            # If pressed C clear the current highlighted square
            if (event.key == pygame.K_c) and (0 <= display_x < 9) and (0 <= display_y < 9) and (
                    grid[int(display_x)][int(display_y)].number != 0):
                full_board = 0
                grid[int(display_x)][int(display_y)].number = 0

            # If pressed S solve the board with constraint propagation
            if event.key == pygame.K_s:
                if is_sudoku_solvable(grid) != 1:
                    solvable = 0
                else:
                    solve_sudoku_constraint_propagation()
                    full_board = 1

            # If pressed D solve with variable ordering
            if event.key == pygame.K_d:
                if is_sudoku_solvable(grid) != 1:
                    solvable = 0
                else:
                    solve_sudoku_variable_ordering()
                    full_board = 1

            # If pressed F solve with only backtracking
            if event.key == pygame.K_f:
                if is_sudoku_solvable(grid) != 1:
                    solvable = 0
                else:
                    solve_sudoku_backtracking()
                    full_board = 1

        if solvable == 0:
            raise_error1()

        if print_solvable == 1:
            raise_error3()

        if (display_val != 0) and (0 <= display_x < 9) and (0 <= display_y < 9):
            if is_valid(grid, int(display_x), int(display_y), display_val):
                grid[int(display_x)][int(display_y)].number = display_val
                move = 0
                draw_val(display_val)
                display_val = 0
            else:
                grid[int(display_x)][int(display_y)].number = 0
                raise_error2()

        if find_blank(grid):
            result()
            full_board = 1
        else:
            full_board = 0

        draw_sudoku(grid)
        if move == 1:
            draw_box(display_x, display_y)
        instruction()

        # Update window
        pygame.display.update()

# Quit pygame window
pygame.quit()
