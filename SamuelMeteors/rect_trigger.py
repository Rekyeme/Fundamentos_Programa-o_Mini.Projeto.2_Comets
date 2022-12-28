import pygame


class RectTrigger:
    def __init__(self, position: pygame.Vector2, width, height):

        # initiating fields
        self.width = width
        self.height = height
        self.position = position

        self.__trigger_inner_rect: pygame.Rect = pygame.Rect(0, 0, 0, 0)

        self.__trigger_inner_rect.width = self.width
        self.__trigger_inner_rect.height = self.height
        self.__trigger_inner_rect.centerx = self.position.x
        self.__trigger_inner_rect.centery = self.position.y

    def update_trigger_position(self, new_position: pygame.Vector2):
        self.__trigger_inner_rect.width = self.width
        self.__trigger_inner_rect.height = self.height
        self.position = new_position
        self.__trigger_inner_rect.centerx = self.position.x
        self.__trigger_inner_rect.centery = self.position.y

    @property
    def inner_rect_read_only(self):
        return self.__trigger_inner_rect.copy()

    def is_there_overlap_with_point(self, point: pygame.Vector2):
        return self.__trigger_inner_rect.collidepoint(point.x, point.y)
