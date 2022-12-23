import pygame, os

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

# Controls the frame rate of the game
FPS = 60

# Spaceship sprite
SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 50

# Load the spaceship image and resize it
SPACESHIP_RED_PNG = pygame.image.load(os.path.join("Assets", "SpaceShipRed_Comets.png"))
SPACESHIP_RED_PNG = pygame.transform.scale(SPACESHIP_RED_PNG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))


def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
  
    # draw rectangle around the image
    pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()),2)

def blitRotate2(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
    pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)

    image = pygame.image.load('Spaceship.png')


def main():
    """
    The main game loop.
    """
    # Set the window caption
    pygame.display.set_caption("Comets")

    # Create the display surface
    display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock to control the frame rate
    clock = pygame.time.Clock()

    # Set up the main game loop
    run = True
    angle = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pos = (display_surface.get_width()/2, display_surface.get_height()/2)

        # Update the spaceship's angle and velocity based on player input
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:  # Go left
            spaceship.angle += spaceship.velocity
        if keys_pressed[pygame.K_RIGHT]:  # Go right
            spaceship.angle -= spaceship.velocity
        if keys_pressed[pygame.K_UP]:  # Go up
            spaceship.velocity += 1
        if keys_pressed[pygame.K_DOWN]:  # Go down
            spaceship.velocity -= 1

       
        # Clear the screen and draw all sprites
        display_surface.fill(WHITE)
        blitRotate(display_surface, Spa, pos, (w/2, h/2), angle)
        angle += 1

        # Update the display
        pygame.display.update()


if __name__ == "__main__":
    main()