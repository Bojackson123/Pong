import pygame
from game import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, WHITE, BLACK, STAGE

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

playerOneYPos = SCREEN_HEIGHT // 2 - 50
playerTwoYPos = SCREEN_HEIGHT // 2 - 50


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Render game
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, STAGE, 2, border_radius=20)
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 10), (SCREEN_WIDTH // 2, 589), 2)
    
    PLAYERONE = pygame.Rect(SCREEN_WIDTH - (SCREEN_WIDTH - 30), playerOneYPos, 10, 90)
    PLAYERTWO = pygame.Rect(SCREEN_WIDTH - 40, playerTwoYPos, 10, 90)
    pygame.draw.rect(screen, WHITE, PLAYERTWO)
    pygame.draw.rect(screen, WHITE, PLAYERONE)
    
    keys = pygame.key.get_pressed()
    # Player One movement
    if keys[pygame.K_LEFT] and playerOneYPos > 10:
        playerOneYPos -= 5
    if keys[pygame.K_RIGHT] and playerOneYPos < SCREEN_HEIGHT - 100:
        playerOneYPos += 5
        
    # Player Two movement
    if keys[pygame.K_UP] and playerTwoYPos > 10:
        playerTwoYPos -= 5
    if keys[pygame.K_DOWN] and playerTwoYPos < SCREEN_HEIGHT - 100:
        playerTwoYPos += 5
    
    pygame.display.flip()
    
    clock.tick(FPS)

pygame.quit()