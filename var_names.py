"""Holds the variable values for game."""
import pygame
import os


# Window Display
WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Harvest the Hay Bales!")

# IMAGES
GRASS_IMAGE = pygame.image.load(os.path.join('Assets', 'grass.png'))
HAY_BALE_IMAGE = pygame.image.load(os.path.join('Assets', 'hay_bale.png'))
TRACTOR_IMAGE_ONE = pygame.image.load(os.path.join('Assets', 'tractor.png'))
COW_IMAGE = pygame.image.load(os.path.join('Assets', 'cow.png'))
FULL_HEART_IMAGE = pygame.image.load(os.path.join('Assets', 'full_heart.png'))
EMPTY_HEART_IMAGE = pygame.image.load(os.path.join('Assets', 'empty_heart.png'))
JOHN_DEER_IMAGE = pygame.image.load(os.path.join('Assets', 'john_deer.png'))

# JOHN DEER IMAGE
JOHN_WIDTH, JOHN_HEIGHT = 80, 55
JOHN_DEER = pygame.transform.scale(JOHN_DEER_IMAGE, (JOHN_WIDTH, JOHN_HEIGHT))

# HAY BALES
HAY_WIDTH, HAY_HEIGHT = 45, 45
HAY_BALE = pygame.transform.scale(HAY_BALE_IMAGE, (HAY_WIDTH, HAY_HEIGHT))
HAY_BALE_ICON = pygame.transform.scale(HAY_BALE_IMAGE, (35, 35))
pygame.display.set_icon(HAY_BALE_ICON)
# MAX HAYS ON SCREEN FOR PLAYER TO GRAB
MAX_HAY: int = 5

# COW VALUES
COW_WIDTH, COW_HEIGHT = 60, 45
COW = pygame.transform.scale(COW_IMAGE, (COW_WIDTH, COW_HEIGHT))

# SOUNDS
TRACTOR_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'tractor.wav'))
HAY_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'harvest.wav'))
COW_SOUND =pygame.mixer.Sound(os.path.join('Assets', 'cow_moo.wav'))
COWS_SOUND =pygame.mixer.Sound(os.path.join('Assets', 'cows.wav'))


# SCORE
SCORE_FONT = pygame.font.SysFont('Cambria', 50)

# WINNER FONT
WINNER_FONT = pygame.font.SysFont('Cambria', 65)

# HEALTH
#HEALTH_FONT = pygame.font.SysFont('Cambria', 25)

# HEARTS
HEART_WIDTH, HEART_HEIGHT = 45, 45
FULL_HEART = pygame.transform.scale(FULL_HEART_IMAGE, (HEART_WIDTH, HEART_HEIGHT))
EMPTY_HEART = pygame.transform.scale(EMPTY_HEART_IMAGE, (HEART_WIDTH, HEART_HEIGHT))



# BLACK BORDER
BORDER = pygame.Rect(0, 60, 1000, 20)

# Color
BROWN: tuple[int] = (131, 92, 28)
BLACK: tuple[int] = (0, 0, 0)
BLUE: tuple[int] = (138, 236, 223)

# FPS
FPS: int = 60

# TRACTOR VALUES
TRACTOR_VEL: int = 10
TRACTOR_WIDTH, TRACTOR_HEIGHT = 90, 65
TRACTOR_X, TRACTOR_Y = WIDTH // 2 - TRACTOR_WIDTH // 2, HEIGHT // 2 - TRACTOR_HEIGHT // 2
TRACTOR_IMAGE_ONE_EDITED = pygame.transform.scale(TRACTOR_IMAGE_ONE, (TRACTOR_WIDTH, TRACTOR_HEIGHT))
