"""Functions."""

import pygame, sys
from var_names import *


def draw_w(tractor, camera_x, camera_y, score) -> None:
    """Everything drawn onto the screen will be this."""
    # bg color
    WIN.fill(BLUE)

    # grass bg / image
    WIN.blit(GRASS_IMAGE, (0, 75))

    # black border on top
    pygame.draw.rect(WIN, BLACK, BORDER)

    # tractor image
    WIN.blit(TRACTOR_IMAGE_ONE_EDITED, (tractor.x - camera_x, tractor.y - camera_y, TRACTOR_WIDTH, TRACTOR_HEIGHT))
    
    # score on top left
    score_text = SCORE_FONT.render("" + str(score), 1, BLACK)
    # displays text
    WIN.blit(score_text, (10, 0))

    # health text (if needed) - dont need cause of heart system
    #health_text = HEALTH_FONT.render("Health: " + str(health), 1, BLACK)
    #WIN.blit(health_text, (100, 0))

    # john deere image
    WIN.blit(JOHN_DEER, (WIDTH / 2 - (JOHN_WIDTH / 2), 5))




def handle_tractor(keys_pressed, tractor):
    """Handles the movement on tractor with WSAD."""
    if keys_pressed[pygame.K_a] and tractor.x - TRACTOR_VEL > 0:  # left
        tractor.x -= TRACTOR_VEL
    if keys_pressed[pygame.K_d] and tractor.x - TRACTOR_VEL < 890:  # right
        tractor.x += TRACTOR_VEL
    if keys_pressed[pygame.K_w] and tractor.y - TRACTOR_VEL > 50:   # up
        tractor.y -= TRACTOR_VEL
    if keys_pressed[pygame.K_s] and tractor.y - TRACTOR_VEL < 910:  # down
        tractor.y += TRACTOR_VEL
    

    pygame.display.update()  # updates pygame everytime a key is hit

def draw_winner(text):
    """Displays the winner."""
    # renders text
    draw_text = WINNER_FONT.render(text, 1, BLACK)

    # draws text on screen
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    
    # updates game screen for text
    pygame.display.update()
    
    # ending sound noise (herd of cows)
    COWS_SOUND.play()
    
    # delay to read final score msg
    pygame.time.delay(3000)


