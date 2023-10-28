"""The main game file (game loop)."""

import pygame
pygame.init()
import os
from func_names import *
from var_names import *

def main() -> None:
    """Main Game Loop Function."""
    tractor = pygame.Rect(450, 250, TRACTOR_WIDTH, TRACTOR_HEIGHT)
    camera_x, camera_y = 0, 0
    tractor_x, tractor_y = WIDTH // 2 - 50 - TRACTOR_WIDTH // 2, HEIGHT - 50 // 2 - TRACTOR_HEIGHT // 2
    screen_center_x, screen_center_y = WIDTH // 2, HEIGHT // 2


    run: bool = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        camera_x, camera_y = tractor_x - screen_center_x, tractor_y - screen_center_y

        keys_pressed = pygame.key.get_pressed()
        handle_tractor(keys_pressed, tractor)
        draw_w(tractor, camera_x, camera_y, tractor_x, tractor_y)
    
    pygame.quit()


if __name__ == "__main__":
    main()
