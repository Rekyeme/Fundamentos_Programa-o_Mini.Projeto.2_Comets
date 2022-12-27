import pygame


class Entity:

    def __init__(self, initial_position, frame_surface, list_of_entities: list, image_path=None):

        self.list_of_entities = list_of_entities
        self.list_of_entities.append(self)

        self.frame_surface = frame_surface
        self.position: pygame.Vector2 = initial_position

        self.image = None
        self.image_rect = None
        if image_path is not None:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image_rect = self.image.get_rect(center=self.position)

    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        if self.image is not None:
            self.image_rect = self.image.get_rect(center=self.position)
            self.frame_surface.blit(self.image, self.image_rect)  # img

    def render_gizmos(self):
        pygame.draw.circle(self.frame_surface, (0, 0, 0), self.position, 5)  # position circle
        pygame.draw.rect(self.frame_surface, (255, 0, 0), self.image_rect, 2)  # img rect

    def destroy(self):
        self.list_of_entities.remove(self)

    def scale_img(self, scale):
        if self.image is not None:
            img_size = self.image.get_size()
            self.image = pygame.transform.scale(self.image, [img_size[0] * scale, img_size[1] * scale])

    def wrap_around(self):
        # x
        if self.position.x > self.frame_surface.get_width() + self.image.get_width()/2:
            self.position.x = 0
        elif self.position.x + self.image.get_width()/2 < 0:
            self.position.x = self.frame_surface.get_width()
        # y
        if self.position.y > self.frame_surface.get_height() + self.image.get_height() / 2:
            self.position.y = 0
        elif self.position.y + self.image.get_height()/2 < 0:
            self.position.y = self.frame_surface.get_height()
