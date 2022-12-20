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

# Spaceship sprite
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 50
VELOCITY = 5
SPACESHIP_RED_PNG = pygame.image.load(os.path.join("Assets", "SpaceShipRed_Comets.png"))
SPACESHIP_RED_PNG = pygame.transform.scale(SPACESHIP_RED_PNG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

# Draws objects on the display;
def window_draw(red):
    DISPALYSURF.fill(WHITE)
    DISPALYSURF.blit(SPACESHIP_RED_PNG, (red.x, red.y))
    pygame.display.update()

#Spaceship sprite movement
def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY: # Go left;
            red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY: # Go right
            red.x += VELOCITY
    if keys_pressed[pygame.K_UP]: # Go up
            red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN]: # Go down
            red.y += VELOCITY

# Main loop;
def main():
    red = pygame.Rect(375, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        red_movement(keys_pressed, red)
            
        window_draw(red)

    pygame.quit()

# Guarantees that the program only runs the main function if this file is read directly;
if __name__ == "__main__":
    main()