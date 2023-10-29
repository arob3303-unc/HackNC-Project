"""The main game file (game loop)."""

import pygame
pygame.init()
from func_names import *
from var_names import *
from random import randint


def main() -> None:
    """Main Game Loop Function."""
    # variables
    tractor = pygame.Rect((TRACTOR_WIDTH // 2) - 35, (940 - (TRACTOR_HEIGHT // 2)), TRACTOR_WIDTH, TRACTOR_HEIGHT)
    camera_x, camera_y = 0, 0
    score: int = 0
    health: int = 3
    time: int = 0
    x: int = 0
    y: int = 0

    # Holds how many cows are on screen/game
    hay_bales = [
        pygame.Rect(200, 750, HAY_WIDTH, HAY_HEIGHT),
    ]

    cows = [
        pygame.Rect(500, 500, COW_WIDTH, COW_HEIGHT),
    ]

    run: bool = True  # run variable

    clock = pygame.time.Clock()

    # while loop to allow game to run (game loop)
    while run:

        clock.tick(FPS)  # 60 FRAMES PER SECOND

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        # COWS
        for cow in cows:

            WIN.blit(COW, (cow[0], cow[1]))
        
        for cow in cows:
            
            # random placement for cows
            cow_x = randint(10, 950) + x
            cow_y = randint(100, 950) + y

            # if cow get hits by tractor, it is removed
            if cow.colliderect(tractor):
                cows.remove(cow)
                health -= 1  # health is substracted
                # allows cow noise to not exist on last cow
                if health > 0:
                    COW_SOUND.play()
        
        # see if hay bales have been collected    
        for hay in hay_bales:
             
             WIN.blit(HAY_BALE, (hay[0], hay[1]))

        for hay in hay_bales:
            hay_x = randint(10, 950)
            hay_y = randint(100, 950)

            if hay.colliderect(tractor):
                hay_bales.remove(hay)
                cows.append(pygame.Rect(cow_x, cow_y, COW_WIDTH, COW_HEIGHT))
                score += 1
                time += 1
                HAY_SOUND.play()
            
            if len(hay_bales) < MAX_HAY:
                hay_bales.append(pygame.Rect(hay_x, hay_y, HAY_WIDTH, HAY_HEIGHT))

        # different score msg depending on score value
        if score < 15:
            winner_text = (f"SCORE: {score}   ->    ONLY {score}???")
        elif score < 30:
            winner_text = (f"YOUR SCORE IS {score}! GOOD JOB!")
        elif score >= 30:
            winner_text = (f"YOUR SCORE IS {score}! WOW!!!")


        # heart system top right
        if health == 3:
            WIN.blit(FULL_HEART, (925, 10))
            WIN.blit(FULL_HEART, (875, 10))  # 3 hearts
            WIN.blit(FULL_HEART, (825, 10))
        if health == 2:
            WIN.blit(FULL_HEART, (925, 10))
            WIN.blit(FULL_HEART, (875, 10))  # 2 hearts
            WIN.blit(EMPTY_HEART, (825, 10))
        if health == 1:
            WIN.blit(FULL_HEART, (925, 10))
            WIN.blit(EMPTY_HEART, (875, 10))  # 1 heart
            WIN.blit(EMPTY_HEART, (825, 10))
        if health == 0:
            WIN.blit(EMPTY_HEART, (925, 10))
            WIN.blit(EMPTY_HEART, (875, 10))  # 0 hearts
            WIN.blit(EMPTY_HEART, (825, 10))




        # key system
        keys_pressed = pygame.key.get_pressed()
        handle_tractor(keys_pressed, tractor)

        # draw function
        draw_w(tractor, camera_x, camera_y, score)

        # ends game when health equals 0
        if health == 0:
            draw_winner(winner_text)
            break

    main()  # restarts game after health equals 0 after delay time


if __name__ == "__main__":
    main()
