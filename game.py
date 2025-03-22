import pygame
from map import *
from entities.tower import *
from entities.enemy import *

class Game():


    def __init__(self):
        self.clock = pygame.time.Clock() 

    def run(self, screen):

        game_map = Map()
        create_towers()

        running = True
        while running:

            game_map.render(screen)
            game_map.draw_grid(screen)

            for tower in Tower.all_towers:
                 tower.render(screen)

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

def create_towers():
    tower1 = Dart(0,0)
    tower2 = Cannon(375, 75)
    tower3 = Boomerang(300, 375) 

