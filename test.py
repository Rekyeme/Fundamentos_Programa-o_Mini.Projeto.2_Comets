import pygame
import os
import math

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


class Spaceship(pygame.sprite.Sprite):
    """
    A class representing the spaceship in the game.
    """

    def _init_(self, x, y, angle, velocity):
        """
        Initializes a new Spaceship object.

        :param x: The x-coordinate of the spaceship's starting position.
        :param y: The y-coordinate of the spaceship's starting position.
        :param angle: The angle of the spaceship's direction in degrees.
        :param velocity: The velocity of the spaceship in pixels per frame.
        """
        super()._init_()

        # Set the image and rect attributes
        self.image = SPACESHIP_RED_PNG
        self.rect = self.image.get_rect()

        # Set the starting position and angle of the spaceship
        self.rect.x = x
        self.rect.y = y
        self.angle = angle

        # Set the velocity of the spaceship
        self.velocity = velocity

    def update(self):
        """
        Updates the spaceship's position and angle.
        """
        # Calculate the new x and y positions based on the angle and velocity
        self.rect.x += self.velocity * math.cos(math.radians(self.angle))
        self.rect.y -= self.velocity * math.sin(math.radians(self.angle))

        # Decrease the velocity slightly each frame
        self.velocity *= 0.90

        # Rotate the image of the spaceship to match the angle
        self.image = pygame.transform.rotate(SPACESHIP_RED_PNG, self.angle)

        # Update the rect to match the rotated image
        self.rect = self.image.get_rect(center=self.rect.center)

        # Check if the spaceship has gone off the screen and wrap it around if necessary
        wrap_around = False
        if self.rect.left < 0:
            # Out of screen left
            self.rect.move_ip(SCREEN_WIDTH, 0)
            wrap_around = True
        if self.rect.right > SCREEN_WIDTH:
            # Out of screen right
            self.rect.move_ip(-SCREEN_WIDTH, 0)
            wrap_around = True
        if self.rect.top < 0:
            # Out of screen up
            self.rect.move_ip(0, SCREEN_HEIGHT)
            wrap_around = True
        if self.rect.bottom > SCREEN_HEIGHT:
            # Out of screen down
            self.rect.move_ip(0, -SCREEN_HEIGHT)
            wrap_around = True
        if wrap_around:
            self.rect.x %= SCREEN_WIDTH
            self.rect.y %= SCREEN_HEIGHT

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

        # Create the spaceship and add it to a sprite group
        spaceship = Spaceship(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 90, 0)
        all_sprites = pygame.sprite.Group(spaceship)

        # Set up the main game loop
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # Update the spaceship's angle and velocity based on player input
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LEFT]:  # Go left
                spaceship.angle += spaceship.velocity
            if keys_pressed[pygame.K_RIGHT]:  # Go right
                spaceship.angle -= spaceship.velocity
            if keys_pressed[pygame.K_UP]:  # Go up
                spaceship.velocity += 2
            if keys_pressed[pygame.K_DOWN]:  # Go down
                spaceship.velocity -= 1

            # Update the positions and angles of all sprites
            all_sprites.update()

            # Clear the screen and draw all sprites
            display_surface.fill(WHITE)
            all_sprites.draw(display_surface)

            # Update the display
            pygame.display.update()

    if __name__ == "_main_":
        main() 