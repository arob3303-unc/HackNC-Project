"""Functions."""

import pygame, sys
from var_names import *

def draw_w(tractor, camera_x, camera_y) -> None:
    """Everything drawn onto the screen will be this."""

    WIN.blit(GRASS_IMAGE, (0, 0))

    WIN.blit(TRACTOR_IMAGE_ONE_EDITED, (tractor.x - camera_x, tractor.y - camera_y, TRACTOR_WIDTH, TRACTOR_HEIGHT))

    pygame.display.update()

def handle_tractor(keys_pressed, tractor):
    if keys_pressed[pygame.K_a] and tractor.x - TRACTOR_VEL > -25:
        tractor.x -= TRACTOR_VEL
    if keys_pressed[pygame.K_d] and tractor.x - TRACTOR_VEL < 873:
        tractor.x += TRACTOR_VEL
    if keys_pressed[pygame.K_w] and tractor.y - TRACTOR_VEL > -50:
        tractor.y -= TRACTOR_VEL
    if keys_pressed[pygame.K_s] and tractor.y - TRACTOR_VEL < 875:
        tractor.y += TRACTOR_VEL
