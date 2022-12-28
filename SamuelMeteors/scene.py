import pygame

from entities.entity import Entity


class Scene:

    def __init__(self, list_of_entities, frame_surface):
        self.list_of_entities: list[Entity] = list_of_entities
        self.frame_surface = frame_surface

    def update_scene(self):
        for entity in self.list_of_entities:
            entity.update()

    def wrap_around_scene(self):
        for entity in self.list_of_entities:
            entity.wrap_around()

    def render_scene(self):
        # clears frame
        self.frame_surface.fill(pygame.Color("blue"))
        # renders
        for entity in self.list_of_entities:
            entity.render()

    def render_gizmos_scene(self):
        # RENDER GIZMOS
        for entity in self.list_of_entities:
            entity.render_gizmos()

