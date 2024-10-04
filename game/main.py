import pygame, os
from game import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, WHITE, BLACK, FONT, TITLE_FONT
from game.button import Button
from game.paddle import Paddle
from game.game import Game

pygame.init()
pygame.display.set_caption("Pong")
icon_path = os.path.join(os.path.dirname(__file__), "../assets/misc/icon.png")
icon_image = pygame.image.load(icon_path)
pygame.display.set_icon(icon_image)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def mainMenu():
    title = TITLE_FONT.render("Pong", True, WHITE)
    play_button = Button(SCREEN_WIDTH // 2 - 75, 350, 150, 50, "PLAY", WHITE, WHITE, FONT, BLACK)
    quit_button = Button(SCREEN_WIDTH // 2 - 75, 440, 150, 50, "QUIT", WHITE, WHITE, FONT, BLACK)
    
    while True:
        screen.fill(BLACK)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 160))
        
        mouse_pos = pygame.mouse.get_pos()
        
         # Check hover state for both buttons
        is_play_hovering = play_button.update(mouse_pos)
        play_button.draw(screen)
        
        is_quit_hovering = quit_button.update(mouse_pos)
        quit_button.draw(screen)
        
        # Change cursor based on hover state
        if is_play_hovering or is_quit_hovering:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Pointer cursor
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Default cursor
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                
            is_play_clicked = play_button.is_clicked(event)
            is_quit_clicked = quit_button.is_clicked(event)
            
            if is_play_clicked:
                play()
            elif is_quit_clicked:
                pygame.QUIT()
                return
        
        pygame.display.flip()
        
        clock.tick(FPS)
    

def play():

    playerOne = Paddle(SCREEN_HEIGHT // 2 - 50, 10, 90, SCREEN_WIDTH - 30)
    playerTwo = Paddle(SCREEN_HEIGHT // 2 - 50, 10, 90, 40)
    game = Game()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
            
        # Render game
        game.draw_stage(screen)
        game.draw_score(screen, FONT)
        
        playerOne.draw(screen)
        playerTwo.draw(screen)
        
        # Player movement
        keys = pygame.key.get_pressed()
        
        # Player One movement
        if keys[pygame.K_LEFT] and playerOne.y > 10:
            playerOne.move_paddle(10, "UP")
        if keys[pygame.K_RIGHT] and playerOne.y < SCREEN_HEIGHT - 100:
            playerOne.move_paddle(10, "DOWN")
            
        # Player Two movement
        if keys[pygame.K_UP] and playerTwo.y > 10:
            playerTwo.move_paddle(10, "UP")
        if keys[pygame.K_DOWN] and playerTwo.y < SCREEN_HEIGHT - 100:
            playerTwo.move_paddle(10, "DOWN")
        
        pygame.display.flip()
        
        clock.tick(FPS)

mainMenu()