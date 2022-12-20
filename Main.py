import pygame, sys

WIDTH, HEIGHT = 800, 600
DISPALYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

def main():

    run = True
    while run:

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()