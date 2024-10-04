import pygame
from game.constants import WHITE, BLACK, STAGE, SCREEN_WIDTH, SCREEN_HEIGHT

class Game():
    def __init__(self):
        self.score = [2, 3]
        self.winner = None
        self.game_over = False
        self.winning_score = 5
        
    def draw_stage(self, screen):
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, STAGE, 2, border_radius=20)
        pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 10), (SCREEN_WIDTH // 2, 589), 2)
    
    def draw_score(self, screen, font):
        score_text = font.render(f"{self.score[0]}        {self.score[1]}", True, WHITE)
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))