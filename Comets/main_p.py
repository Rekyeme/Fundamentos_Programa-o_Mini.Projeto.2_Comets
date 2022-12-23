import pygame

class Comets:
    def __init__(self):
        self.__init__pygame()
        self.screen = pygame.display.set_mode((800, 600))

    def main_loop(self):
        while True:
            self._input()
            self._game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def _input(self):
        pass

    def _game_logic(self):
        pass

    def _draw(self):
        self.screen.fill((0, 0, 255))
        pygame.display.flip()
        
