import pygame.transform
from entities.entity import Entity
from timer import Timer


class Bullet(Entity):

    Instantiated_Bullets = []

    def __init__(self, initial_position, angle, direction, frame_surface, list_of_entities: list, img_path):
        super().__init__(initial_position, frame_surface, list_of_entities, img_path)

        Bullet.Instantiated_Bullets.append(self)

        self.scale_img(0.03)
        self.angle = angle
        self.direction = direction
        self.bullet_speed = 4
        self.image = pygame.transform.rotate(self.image, angle)

        self.life_time_timer = Timer(4*1000)
        self.life_time_timer.activate()

    def update(self):
        self.position += self.direction * self.bullet_speed
        self.life_time_timer.timer_update()
        if not self.life_time_timer.is_timer_active_read_only:
            self.destroy()

    def destroy(self):
        super(Bullet, self).destroy()
        Bullet.Instantiated_Bullets.remove(self)
