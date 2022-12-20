# Imports Pygame
import pygame

# Screen width and height;
WIDTH, HEIGHT = 800, 600
DISPALYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

# Main loop;
def main():

    run = True
    while run:

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run = False

    pygame.quit()


# Guarantees that the program only runs the main function if this file is read directly;
if __name__ == "__main__":
    main()