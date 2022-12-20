# Imports Pygame
import pygame
import os

# Screen width and height;
WIDTH, HEIGHT = 800, 600
DISPALYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Comets")

# Colors;
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Controls how fast the game will run;
FPS = 60

# Spaceship sprites import
Spaceship_RED_PNG = pygame.image.load(os.path.join("Assets", "SpaceShipRed_Comets.png"))

# Draws objects on the display;
def window_draw():
    DISPALYSURF.fill(WHITE)
    DISPALYSURF.blit(Spaceship_RED_PNG, (365, 285))
    pygame.display.update()

# Main loop;
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run = False

        window_draw()

    pygame.quit()

# Guarantees that the program only runs the main function if this file is read directly;
if __name__ == "__main__":
    main()