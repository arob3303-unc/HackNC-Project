"""Functions."""

import pygame, sys
from var_names import *

def draw_w(tractor, camera_x, camera_y, score) -> None:
    """Everything drawn onto the screen will be this."""
    WIN.fill(BLUE)
    WIN.blit(GRASS_IMAGE, (0, 75))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(TRACTOR_IMAGE_ONE_EDITED, (tractor.x - camera_x, tractor.y - camera_y, TRACTOR_WIDTH, TRACTOR_HEIGHT))
    score_text = SCORE_FONT.render("" + str(score), 1, BLACK)
    WIN.blit(score_text, (10, 0))
    #health_text = HEALTH_FONT.render("Health: " + str(health), 1, BLACK)
    #WIN.blit(health_text, (100, 0))
    WIN.blit(JOHN_DEER, (WIDTH / 2 - (JOHN_WIDTH / 2), 5))




def handle_tractor(keys_pressed, tractor):
    if keys_pressed[pygame.K_a] and tractor.x - TRACTOR_VEL > 0:  # left
        tractor.x -= TRACTOR_VEL
    if keys_pressed[pygame.K_d] and tractor.x - TRACTOR_VEL < 890:  # right
        tractor.x += TRACTOR_VEL
    if keys_pressed[pygame.K_w] and tractor.y - TRACTOR_VEL > 50:   # up
        tractor.y -= TRACTOR_VEL
    if keys_pressed[pygame.K_s] and tractor.y - TRACTOR_VEL < 910:  # down
        tractor.y += TRACTOR_VEL
    

    pygame.display.update()

def draw_winner(text):
    """Displays the winner."""
    draw_text = WINNER_FONT.render(text, 1, BLACK)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    COWS_SOUND.play()
    pygame.time.delay(3000)


