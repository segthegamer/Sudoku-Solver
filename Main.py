import pygame
import Functions
import Gui
from Grid import Square
from Gui import display_x
from Gui import display_y
from Gui import display_val
# Starting values for gui
rows, columns = 9, 9
grid = [[Square() for x in range(columns)] for y in range(rows)]
run = True
move = 0
solvable = 1
print_solvable = 0
full_board = 0

# Game loop
while run:
    # White color background
    Gui.screen.fill((255, 255, 255))
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
            display_x, display_y = Gui.get_cord(pos)
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
                if Functions.is_sudoku_solvable(grid) != 1:
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
                Functions.make_full_sudoku(grid, 0, 0)
                Functions.make_puzzle(grid, 0)
                Functions.find_options(grid)

            # If J is pressed start new normal game
            if event.key == pygame.K_j:
                full_board = 0
                grid = [[Square() for x in range(columns)] for y in range(rows)]
                Functions.make_full_sudoku(grid, 0, 0)
                Functions.make_puzzle(grid, 1)
                Functions.find_options(grid)

            # If K is pressed start hard new game
            if event.key == pygame.K_k:
                full_board = 0
                grid = [[Square() for x in range(columns)] for y in range(rows)]
                Functions.make_full_sudoku(grid, 0, 0)
                Functions.make_puzzle(grid, 2)
                Functions.find_options(grid)

            # If L is pressed start new impossible game
            if event.key == pygame.K_l:
                full_board = 0
                grid = [[Square() for x in range(columns)] for y in range(rows)]
                Functions.make_full_sudoku(grid, 0, 0)
                Functions.make_puzzle(grid, 3)
                Functions.find_options(grid)

            # If pressed C clear the current highlighted square
            if (event.key == pygame.K_c) and (0 <= display_x < 9) and (0 <= display_y < 9) and (
                    grid[int(display_x)][int(display_y)].number != 0):
                full_board = 0
                grid[int(display_x)][int(display_y)].number = 0

            # If pressed S solve the board with constraint propagation
            if event.key == pygame.K_s:
                if Functions.is_sudoku_solvable(grid) != 1:
                    solvable = 0
                else:
                    Functions.solve_sudoku_constraint_propagation(grid)
                    full_board = 1

            # If pressed D solve with variable ordering
            if event.key == pygame.K_d:
                if Functions.is_sudoku_solvable(grid) != 1:
                    solvable = 0
                else:
                    Functions.solve_sudoku_variable_ordering(grid)
                    full_board = 1

            # If pressed F solve with only backtracking
            if event.key == pygame.K_f:
                if Functions.is_sudoku_solvable(grid) != 1:
                    solvable = 0
                else:
                    Functions.solve_sudoku_backtracking(grid)
                    full_board = 1

            # If pressed G solve with only simple elimination
            if event.key == pygame.K_g:
                if Functions.is_sudoku_solvable(grid) != 1:
                    solvable = 0
                else:
                    Functions.solve_sudoku_simple_elimination(grid)
                    full_board = 1

        if solvable == 0:
            Gui.print_msg_1()

        if print_solvable == 1:
            Gui.print_msg_2()

        if (display_val != 0) and (0 <= display_x < 9) and (0 <= display_y < 9):
            if Functions.is_valid(grid, int(display_x), int(display_y), display_val):
                grid[int(display_x)][int(display_y)].number = display_val
                move = 0
                Gui.draw_val(display_x, display_y, display_val)
                display_val = 0
            else:
                grid[int(display_x)][int(display_y)].number = 0
                Gui.print_msg_3()

        if Functions.find_blank(grid):
            Gui.result()
            full_board = 1
        else:
            full_board = 0

        Gui.draw_sudoku(grid)
        if move == 1:
            Gui.draw_box(display_x, display_y)
        Gui.instruction()

        # Update window
        pygame.display.update()

# Quit pygame window
pygame.quit()
