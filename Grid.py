import random
import time
import pygame


class Square:
    def __init__(self):
        self.number = 0
        self.options = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_options(self):
        return self.options

    def set_options(self, options):
        self.options = options
