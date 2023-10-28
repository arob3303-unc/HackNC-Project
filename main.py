"""The main game file (game loop)."""

import pygame
pygame.init()
import os
from func_names import *
from var_names import *

def main() -> None:
    """Main Game Loop Function."""
    tractor = pygame.Rect(50 - (TRACTOR_WIDTH // 2), (940 - (TRACTOR_HEIGHT // 2)), TRACTOR_WIDTH, TRACTOR_HEIGHT)
    camera_x, camera_y = 0, 0

    run: bool = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            

        keys_pressed = pygame.key.get_pressed()
        print(tractor)
        handle_tractor(keys_pressed, tractor)
        draw_w(tractor, camera_x, camera_y)
    
    pygame.quit()


if __name__ == "__main__":
    main()
