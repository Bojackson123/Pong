import pygame
from game import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, WHITE, BLACK, STAGE

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Render game
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, STAGE, 2, border_radius=20)
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 10), (SCREEN_WIDTH // 2, 589), 2)
    
    pygame.display.flip()
    
    clock.tick(FPS)

pygame.quit()