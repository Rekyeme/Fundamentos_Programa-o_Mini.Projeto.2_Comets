import pygame

from entities.entity import Entity
from utilities.rect_trigger import RectTrigger


class Button(Entity):

    def __init__(self, path_normal, path_active, scale, func, initial_position, frame_surface, list_of_entities: list):
        super().__init__(initial_position, frame_surface, list_of_entities, path_normal)


        self.path_normal = path_normal
        self.path_active = path_active

        self.position = initial_position
        self.scale = scale
        self.scale_img(scale)
        self.rect_trigger = RectTrigger(self.position, self.image_rect.width, self.image.get_height())
        self.func = func

    def update(self) -> None:

        if self.rect_trigger.is_there_overlap_with_point(pygame.Vector2(pygame.mouse.get_pos())):
            self.image = pygame.image.load(self.path_active)
            self.scale_img(self.scale)
            if pygame.mouse.get_pressed(3)[0]:
                self.func()
        else:
            self.image = pygame.image.load(self.path_normal)
            self.scale_img(self.scale)

    def render_gizmos(self):
        super(Button, self).render_gizmos()
        pygame.draw.rect(self.frame_surface, pygame.Color("green"), self.rect_trigger.inner_rect_read_only, 2)