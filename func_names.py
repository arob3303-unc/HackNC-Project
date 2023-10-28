"""Functions."""

import pygame
from var_names import *

def draw_w(tractor, camera_x, camera_y, tractor_x, tractor_y) -> None:
    """Everything drawn onto the screen will be this."""
    WIN_SURFACE.fill((BROWN))
    WIN.blit(WIN_SURFACE, (0, 0))

    WIN.blit(TRACTOR_IMAGE_ONE_EDITED, (tractor_x - camera_y, tractor_y - camera_y, TRACTOR_WIDTH, TRACTOR_HEIGHT))

    pygame.display.update()

def handle_tractor(keys_pressed, tractor):
    if keys_pressed[pygame.K_a]:
        tractor.x -= TRACTOR_VEL
    if keys_pressed[pygame.K_d]:
        tractor.x += TRACTOR_VEL
    if keys_pressed[pygame.K_w]:
        tractor.y -= TRACTOR_VEL
    if keys_pressed[pygame.K_s]:
        tractor.y += TRACTOR_VEL
