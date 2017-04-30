import sys

import pygame
from bullet import Bullet

def check_events(settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        check_keydown_event(settings, screen, event, ship, bullets)
        check_keyup_event(event, ship)

def check_keydown_event(settings, screen, event, ship, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            fire_bullet(settings, screen, ship, bullets)

def check_keyup_event(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False

def update_screen(settings, screen, ship, bullets):
    """update images on screen and flip to the new screen"""
    screen.fill(settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw()

    pygame.display.flip()

def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

