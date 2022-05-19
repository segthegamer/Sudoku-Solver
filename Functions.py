import random
import pygame

global columns
global rows
global number
number = 0
columns = 9
rows = 9
full_grid = [[0 for x in range(columns)] for y in range(rows)]
puzzle_grid = [[0 for x in range(columns)] for y in range(rows)]
solution_grid = [[0 for x in range(columns)] for y in range(rows)]

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
font2 = pygame.font.SysFont("comicsans", 20)


def get_cord(pos):
    global display_x
    display_x = pos[0] // display_diff
    global display_y
    display_y = pos[1] // display_diff


# make recive temporary grid
# draw sudoku grid
def draw_sudoku(temp_grid):
    # Draw the lines

    for i in range(9):
        for j in range(9):
            if temp_grid[j][i] != 0:
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (0, 153, 153),
                                 (i * display_diff, j * display_diff, display_diff + 1, display_diff + 1))

                # Fill grid with default numbers specified
                text1 = font1.render(str(temp_grid[j][i]), 1, (0, 0, 0))
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


# cell highlight
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (display_x * display_diff - 3, (display_y + i) * display_diff),
                         (display_x * display_diff + display_diff + 3, (display_y + i) * display_diff), 7)
        pygame.draw.line(screen, (255, 0, 0), ((display_x + i) * display_diff, display_y * display_diff),
                         ((display_x + i) * display_diff, display_y * display_diff + display_diff), 7)


# Raise error when wrong value entered
def raise_error1():
    text1 = font1.render("Wrong number", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


def raise_error2():
    text1 = font1.render("Invalid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


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



def print_sudoku(print_grid):
    for i in range(9):
        for j in range(9):
            if print_grid[i][j] == 0:
                print('-', end=' ')
            else:
                print(print_grid[i][j], end=' ')
        print()


def main():
    make_full_sudoku(0, 0)
    make_puzzle()
#    solve_sudoku_puzzle()
#    solve_sudoku()

    print_sudoku(full_grid)
    print(" ")
    print(is_sudoku_solvable(full_grid))

    print(" ")
    print_sudoku(puzzle_grid)
    print(" ")
    print(is_sudoku_solvable(puzzle_grid))

#    print(" ")
#    print_sudoku(solution_grid)
#    print(" ")
#    print(is_sudoku_solvable(solution_grid))


main()


# Display instruction for the game
def instruction():
    text1 = font2.render("Press R to empty board, Press D to make new puzzle", 1, (0, 0, 0))
    text2 = font2.render("Enter a value, then press ENTER to visualize placement", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))


# Display options when solved
def result():
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

# game loop

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
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        # Get the number to be inserted if key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                display_x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                display_x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                display_y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                display_y += 1
                flag1 = 1
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
            if event.key == pygame.K_RETURN:
                flag2 = 1
            # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                full_grid = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            # If D is pressed reset the board to default
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                full_grid = [
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]
        if flag2 == 1:
            if not solve_sudoku_puzzle():
                error = 1
            else:
                rs = 1
            flag2 = 0

        if display_val != 0:
            draw_val(display_val)
            if is_valid(full_grid, int(display_x), int(display_y), display_val):
                full_grid[int(display_x)][int(display_x)] = display_val
                flag1 = 0
            else:
                full_grid[int(display_x)][int(display_y)] = 0
                raise_error2()
            display_val = 0

        if error == 1:
            raise_error1()
        if rs == 1:
            result()
        draw_sudoku(full_grid)
        if flag1 == 1:
            draw_box()
        instruction()

        # Update window
        pygame.display.update()

# Quit pygame window
pygame.quit()
