import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS


class GameEngine:
    def __init__(self, event_handler):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Visual Novel")
        self.clock = pygame.time.Clock()
        self.running = True
        self.event_handler = event_handler

    def run(self):
        while self.running:
            self.event_handler.handle()
            if self.event_handler.quit_requested:
                self.running = False

            self.clock.tick(FPS)
            pygame.display.flip()

        pygame.quit()