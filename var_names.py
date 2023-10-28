"""Holds the variable values for game."""
import pygame
import os


# Window Display
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tractor Race!")

WIN_CENTER_x, WIN_CENTER_y = WIDTH // 2, HEIGHT // 2
WIN_SURFACE = pygame.Surface((WIDTH, HEIGHT))

# Color
BROWN: tuple[int] = (131, 92, 28)

FPS: int = 60

TRACTOR_VEL: int = 5
TRACTOR_WIDTH, TRACTOR_HEIGHT = 125, 100
TRACTOR_X, TRACTOR_Y = WIDTH // 2 - TRACTOR_WIDTH // 2, HEIGHT // 2 - TRACTOR_HEIGHT // 2
TRACTOR_IMAGE_ONE = pygame.image.load(os.path.join('Assets', 'tractor.png'))
TRACTOR_IMAGE_ONE_EDITED = pygame.transform.scale(TRACTOR_IMAGE_ONE, (TRACTOR_WIDTH, TRACTOR_HEIGHT))
