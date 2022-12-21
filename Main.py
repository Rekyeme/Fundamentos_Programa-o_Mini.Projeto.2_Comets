# Imports 
import pygame, os, math

# Screen width and height;
WIDTH, HEIGHT = 800, 600
DISPALYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Comets")

# Colors;
WHITE = (255, 255, 255)

# Controls how fast the game will run;
FPS = 60

# Spaceship sprite
SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 50
SPACESHIP_RED_PNG = pygame.image.load(os.path.join("Assets", "SpaceShipRed_Comets.png"))
SPACESHIP_RED_PNG = pygame.transform.scale(SPACESHIP_RED_PNG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

# Draws objects on the display;
def window_draw(x, y):
    DISPALYSURF.fill(WHITE)
    DISPALYSURF.blit(SPACESHIP_RED_PNG, (x, y))
    pygame.display.update()

# Main loop;
def main():

    clock = pygame.time.Clock()
    run = True
    while run:
        angle = 90
        VELOCITY = 0

        if angle == 360: angle = 0
        if angle == -1: angle = 359

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]: # Go left;
            angle += VELOCITY
        if keys_pressed[pygame.K_RIGHT]: # Go right
            angle -= VELOCITY
        if keys_pressed[pygame.K_UP]: # Go up
             VELOCITY += 2
        if keys_pressed[pygame.K_DOWN]: # Go down
             VELOCITY -= 1

        x = SPACESHIP_WIDTH
        y = SPACESHIP_HEIGHT 

        x += VELOCITY*math.cos(math.radians(angle))
        y -= VELOCITY*math.cos(math.radians(angle))
        VELOCITY *= .90

        mid = x, y
        SPACESHIP_ROT = pygame.transform.rotate(SPACESHIP_RED_PNG, angle)
        position = SPACESHIP_ROT.get_rect(mid)

        wrap_around = False
        
        
        if position[0] <  0 :
        # out screen left
            position.move_ip(SPACESHIP_WIDTH, 0)
            wrap_around = True

        if position[0]  + SPACESHIP_ROT.get_width() > SPACESHIP_WIDTH:
        # out screen right
            position.move_ip(-SPACESHIP_WIDTH, 0)
            wrap_around = True

        if position[1]  < 0:
        # out screen up
            position.move_ip(0, SPACESHIP_HEIGHT) 
            wrap_around = True

        if position[1] + SPACESHIP_ROT.get_height() > SPACESHIP_HEIGHT:
        # out screen down
            position.move_ip(0, -SPACESHIP_HEIGHT) 
            wrap_around = True

        if wrap_around:

            DISPALYSURF.blit(SPACESHIP_ROT, position)

        position[0] %= WIDTH
        position[1] %= HEIGHT  
        WIDTH %= WIDTH
        HEIGHT %= HEIGHT

    window_draw(x, y)

    pygame.quit()

# Guarantees that the program only runs the main function if this file is read directly;
if __name__ == "__main__":
    main()