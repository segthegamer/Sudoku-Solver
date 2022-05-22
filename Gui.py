import pygame

# pygame start
pygame.font.init()

pygame.display.set_caption("Sudoku Solver")
screen = pygame.display.set_mode((500, 600))
icon = pygame.image.load('sudoku_icon.png')
pygame.display.set_icon(icon)
display_x = 0
display_y = 0
display_diff = 500 / 9
display_val = 0

# fonts
font1 = pygame.font.SysFont("", 40)
font2 = pygame.font.SysFont("", 18)


# Raise error when sudoku is unsolvable
def print_msg_1():
    text1 = font1.render("Sudoku is unsolvable", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


# Raise message when sudoku is solvable
def print_msg_2():
    text1 = font1.render("Sudoku is solvable", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


# Raise error when invalid value entered
def print_msg_3():
    text1 = font1.render("Invalid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


# Convert screen coordinates to square coordinates
def get_cord(pos):
    x = pos[0] // display_diff
    y = pos[1] // display_diff
    return x, y


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


# Cell highlighting
def draw_box(display_x, display_y):
    if (0 <= display_x < 9) and (0 <= display_y < 9):
        for i in range(2):
            pygame.draw.line(screen, (255, 0, 0), (display_x * display_diff - 3, (display_y + i) * display_diff),
                             (display_x * display_diff + display_diff + 3, (display_y + i) * display_diff), 7)
            pygame.draw.line(screen, (255, 0, 0), ((display_x + i) * display_diff, display_y * display_diff),
                             ((display_x + i) * display_diff, display_y * display_diff + display_diff), 7)


# Fill value entered in cell
def draw_val(display_x, display_y, display_val):
    text1 = font1.render(str(display_val), 1, (0, 0, 0))
    screen.blit(text1, (display_x * display_diff + 15, display_y * display_diff + 15))


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
    text1 = font2.render("Press R to empty board, H J K L difficulty, I check, S - CP solve, D - VO solve, F - B solve",
                         1,
                         (0, 0, 0))
    text2 = font2.render("Use the left mouse button and arrow keys, enter a value, C to clear placement", 1, (0, 0, 0))
    screen.blit(text1, (1, 520))
    screen.blit(text2, (1, 540))


# Display finished when solved
def result():
    text1 = font1.render("Game is finished", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))
