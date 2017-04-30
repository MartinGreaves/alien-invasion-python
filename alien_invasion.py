import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    pygame.init()
    sett = Settings()
    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode((sett.screen_width, sett.screen_height))

    ship = Ship(screen)

    while True:
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(sett.bg_color)
        ship.blitme()

        pygame.display.flip()

run_game()
