import pygame


class EventHandler:
    def __init__(self):
        self.quit_requested = False

    def handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_requested = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_click(event.pos)
            elif event.type == pygame.KEYDOWN:
                self.handle_key(event.key)

    def handle_click(self, pos):
        pass

    def handle_key(self, key):
        if key == pygame.K_ESCAPE:
            self.quit_requested = True