import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT

pygame.init()


class Game:
    def __init__(self):
        self.running = True

    def create_screen(self, width: int, height: int):
        self.screen = pygame.display.set_mode((width, height))
        return self.screen

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        pygame.quit()


game = Game()
game.create_screen(800, 600)
game.main_loop()
