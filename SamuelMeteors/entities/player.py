
import pygame
from pygame import *
import math

from entities.bullet import Bullet
from entities.entity import Entity
from rect_trigger import RectTrigger
from timer import Timer


class Player(Entity):

    Score = 0
    Rect_Trigger = RectTrigger(Vector2(0, 0), 0, 0)

    def __init__(self, frame_surface, list_of_entities: list):
        super().__init__(Vector2(300, 400), frame_surface, list_of_entities, "assets/SpaceshipRed.png")

        # RENDER

        self.scale_img(0.4)
        self.img_original = self.image.copy()

        # ---------------------------------

        # STATICS

        Player.Score = 0

        Player.Rect_Trigger.width = 50
        Player.Rect_Trigger.height = 50
        Player.Rect_Trigger.update_trigger_position(self.position)

        # ---------------------------------

        # UPDATE

        # shoot
        # 1s * 1000 = 0.001 ms
        self.timer = Timer(1*1000)
        self.timer.activate()

        # move
        self.max_move_speed = 2.5
        self.current_move_speed = 0
        self.acceleration = 0.05
        self.deceleration = 0.02

        # rotate
        self.angle = 0
        self.angular_velocity = 2

        # direction
        self.move_direction = Vector2(0, 0)

    # ==================================================================================================================

    def update(self):
        self.__rotate()
        self.__generate_move_direction()
        self.__move()
        self.__shoot()

        Player.Rect_Trigger.update_trigger_position(self.position)

    # ==================================================================================================================

    def __shoot(self):
        keys = pygame.key.get_pressed()
        self.timer.timer_update()
        if keys[K_SPACE] and not self.timer.is_timer_active_read_only:
            self.timer.activate()
            # instantiate bullet
            bullet_position = self.position.copy()
            Bullet(bullet_position, self.angle, self.move_direction, self.frame_surface,
                   self.list_of_entities, "assets/bullet.png")

    def __rotate(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.angle -= self.angular_velocity
        elif keys[K_LEFT]:
            self.angle += self.angular_velocity
        self.image = pygame.transform.rotate(self.img_original, self.angle)
        self.image_rect = self.image.get_rect(center=self.position)

    def __generate_move_direction(self):
        angle_in_rads = math.radians(self.angle + 180)
        self.move_direction.x = math.sin(angle_in_rads)
        self.move_direction.y = math.cos(angle_in_rads)
        if self.move_direction.magnitude() != 0:
            self.move_direction = self.move_direction.normalize()

    def __accelerate(self):
        self.current_move_speed += self.acceleration
        if self.current_move_speed > self.max_move_speed:
            self.current_move_speed = self.max_move_speed

    def __decelerate(self):
        self.current_move_speed -= self.deceleration
        if self.current_move_speed < 0:
            self.current_move_speed = 0

    def __move(self):
        keys = pygame.key.get_pressed()
        move = False
        if keys[K_UP]:
            move = True

        if move:
            self.__accelerate()
        else:
            self.__decelerate()

        incremento = self.move_direction * self.current_move_speed
        new_position = self.position + incremento
        self.position = new_position

    def render_gizmos(self):
        super(Player, self).render_gizmos()
        pygame.draw.rect(self.frame_surface, pygame.Color("green"), Player.Rect_Trigger.inner_rect_read_only, 2)
