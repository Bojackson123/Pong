import pygame
import os

pygame.init()

# Game settings
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

FONT_TITLE_SIZE = 200
FONT_SIZE = 40
FONT_PATH = os.path.join(os.path.dirname(__file__), "../assets/fonts/8bit.ttf")
TITLE_FONT = pygame.font.Font(FONT_PATH, FONT_TITLE_SIZE)
FONT = pygame.font.Font(FONT_PATH, FONT_SIZE)

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Rects (x, y, width, height)
STAGE = pygame.Rect(10, 10, SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)

# Player settings

