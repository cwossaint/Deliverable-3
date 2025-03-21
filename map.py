import pygame
from level_data import *
from constants import *
import copy

class Map():
    def __init__(self):
        self.array = copy.deepcopy(LEVEL1MAPARRAY)

    def draw_grid(self, screen):
        for x in range(0, GRID_SIZE + 1, TILE_SIZE):
            pygame.draw.line(screen, BROWN, (x, 0), (x, GRID_SIZE), 1)
        for y in range(0, GRID_SIZE + 1, TILE_SIZE):
            pygame.draw.line(screen, BROWN, (0, y), (GRID_SIZE, y), 1)

    def render(self, screen):
        for row in range(len(self.array)):
            for col in range(len(self.array[row])):
                grid_value = self.array[row][col]
                if grid_value == 1 or grid_value == 4:
                    colour = LIGHT_BROWN
                elif grid_value == 0:
                    colour = DARK_BROWN
                elif grid_value == 3:
                    colour = GRAY
                elif grid_value == 2:
                    colour = DARK_GREEN
                else:
                    colour = None
                if colour:
                    x, y = self.grid_to_screen(row, col)
                    pygame.draw.rect(screen, colour, (x, y, TILE_SIZE, TILE_SIZE))
    
    def grid_to_screen(self, row, col):
        y = row * TILE_SIZE
        x = col * TILE_SIZE
        return x, y