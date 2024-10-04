import pygame
from game.constants import WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class Paddle():
    def __init__(self, y, width, height, x_offset):
        self.y = y
        self.width = width
        self.height = height
        self.x_offset = x_offset
        
    def draw(self, screen):
        rect = pygame.Rect(SCREEN_WIDTH - self.x_offset, self.y, self.width, self.height)
        pygame.draw.rect(screen, WHITE, rect)
        
    def move_paddle(self, speed, direction):
        if direction == "UP":
            self.y -= speed
        elif direction == "DOWN":
            self.y += speed
    
    
            
        
        
        