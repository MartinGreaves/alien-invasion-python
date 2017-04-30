import sys

import pygame

import game_functions as gf

from settings import Settings
from ship import Ship

from pygame.sprite import  Group

def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")

    settings = Settings()

    screen_size = (settings.screen_width, settings.screen_height)
    screen = pygame.display.set_mode(screen_size)

    ship = Ship(settings, screen)

    bullets = Group()

    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(settings, screen, ship, bullets)


run_game()
