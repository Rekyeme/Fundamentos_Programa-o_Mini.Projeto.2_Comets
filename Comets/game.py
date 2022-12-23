import pygame


class Comets:
    def __init__(self):
        self.win = pygame.display.set_mode((800, 600))

    def main_loop(self):
        while True:
            self._input_()
            self._logic_()
            self._draw_()

    @staticmethod
    def _init_pygame():
        pygame.init()
        pygame.display.set_caption("Comets")

    def _input_(self):
        pass

    def _logic_(self):
        pass

    def _draw_(self):
        self.win.fill((0, 0, 255))
        pygame.display.flip()
