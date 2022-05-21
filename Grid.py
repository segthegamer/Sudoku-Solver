import random
import time
import pygame
import Functions


class Square(object):
    def __init__(self, number, options):
        self.number = number
        self.options = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_options(self):
        return self.options

    def set_options(self, options):
        self.options = options


"""
        j, i = 0, 0
        while i < 9:
            j = 0
            while j < 9 and Functions.full_grid[i][j] != 0:
                if j == 8:
                    break
                else:
                    j += 1
            if Functions.full_grid[i][j] == 0:
                break
            else:
                i += 1
         if there are no blank squares, the grid is solved, return 1 else return 0
        if i == 9:
            set_options(self, 0)
"""