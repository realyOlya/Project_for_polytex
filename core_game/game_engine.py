import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS


class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Visual Novel")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            pygame.display.flip()
        pygame.quit()