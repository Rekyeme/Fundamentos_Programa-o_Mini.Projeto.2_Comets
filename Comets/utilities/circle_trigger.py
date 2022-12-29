import pygame


class CircleTrigger:

    def __init__(self, position: pygame.Vector2, radius):
        # initiating fields
        self.radius = radius
        self.x = position.x
        self.y = position.y

    def update_trigger_position(self, new_position: pygame.Vector2):
        self.x = new_position.x
        self.y = new_position.y

    def is_there_overlap_with_point(self, point: pygame.Vector2):
        squared_dist = (self.x - point.x) ** 2 + (self.y - point.y) ** 2
        return squared_dist <= self.radius ** 2

    def is_there_overlap_with_rect(self, rect: pygame.Rect):
        X1 = rect.x
        X2 = rect.x + rect.width
        Y1 = rect.y
        Y2 = rect.y + rect.height

        def smaller(a, b):
            if a < b:
                return a
            return b

        def bigger(a, b):
            if a > b:
                return a
            return b
        # - Finds the nearest point on the rectangle to the center of the circle
        Xn = bigger(X1, smaller(self.x, X2))
        Yn = bigger(Y1, smaller(self.y, Y2))
        # - Finds the distance between the nearest point and the center of the circle
        # - Distance between 2 points, (x1, y1) & (x2, y2) in 2D Euclidean space is ((x1-x2)**2 + (y1-y2)**2)**0.5
        Dx = Xn - self.x
        Dy = Yn - self.y
        return (Dx ** 2 + Dy ** 2) <= self.radius ** 2
