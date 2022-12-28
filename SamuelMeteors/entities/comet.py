import enum
import pygame
import math
import random
from circle_trigger import CircleTrigger
from entities.bullet import Bullet
from entities.entity import Entity
from entities.player import Player


class Rank(enum.Enum):
    Big = 1,
    Mid = 2,
    Small = 3


class CometManager(Entity):

    Instantiated_Comets = []
    GameOver = False

    def __init__(self, frame_surface, list_of_entities: list):
        super().__init__(pygame.Vector2(0, 0), frame_surface, list_of_entities)
        self.__instantiate_big_comet_at_random_position()

    def __instantiate_big_comet_at_random_position(self):
        Comet(Rank.Big, pygame.Vector2(random.randint(1, 800-1), random.randint(1, 600-1)),
                      self.frame_surface, self.list_of_entities)

    def update(self):
        # make a new big comet whenever there is less than 2 comets on screen
        if len(CometManager.Instantiated_Comets) < 2:
            self.__instantiate_big_comet_at_random_position()


class Comet(Entity):

    def __init__(self, rank: Rank, initial_position, frame_surface, list_of_entities: list):
        super().__init__(initial_position, frame_surface, list_of_entities, "assets/comet.png")

        self.rank = rank

        if rank == Rank.Big:
            self.scale_img(0.4)
            self.circle_trigger = CircleTrigger(self.position, 80)
            self.alpha = 1
        elif rank == Rank.Mid:
            self.scale_img(0.2)
            self.circle_trigger = CircleTrigger(self.position, 40)
            self.alpha = 255
        elif rank == Rank.Small:
            self.scale_img(0.1)
            self.circle_trigger = CircleTrigger(self.position, 20)
            self.alpha = 255

        self.appearing_speed = 1.5

        # random direction and movement
        self.angle = random.randint(1, 360)
        self.angle_in_rads = math.radians(self.angle + 180)
        self.direction = pygame.Vector2(math.sin(self.angle_in_rads), math.cos(self.angle_in_rads))
        self.move_speed = 2

        # adds itself to comets list
        CometManager.Instantiated_Comets.append(self)

        # debugging
        print(f"comet ({self.rank.name}) angle: {self.angle}")

    def update(self):

        # updates when has finished to appear
        has_finished_to_appear = self.alpha >= 255
        if not has_finished_to_appear:
            self.__make_appearing_animation()
            return

        # update trigger for collisions
        self.circle_trigger.update_trigger_position(self.position)

        # collision player
        if self.circle_trigger.is_there_overlap_with_rect(Player.Rect_Trigger.inner_rect_read_only):
            print("player is inside me")
            CometManager.GameOver = True

        # collision bullet
        for bullet in Bullet.Instantiated_Bullets:
            if self.circle_trigger.is_there_overlap_with_point(bullet.position):
                bullet.destroy()
                self.destroy()
                if self.rank == Rank.Big:
                    Player.Score += 3
                    for i in range(0, 3):
                        Comet(Rank.Mid, self.position.copy(), self.frame_surface, self.list_of_entities)
                elif self.rank == Rank.Mid:
                    Player.Score += 6
                    for i in range(0, 5):
                        Comet(Rank.Small, self.position.copy(), self.frame_surface, self.list_of_entities)
                elif self.rank == Rank.Small:
                    Player.Score += 12

        # player score debugging
        print(f"score: {Player.Score}")

        # move
        self.position += self.direction * self.move_speed

    def __make_appearing_animation(self):
        # appearing animation
        self.alpha += self.appearing_speed
        if self.alpha > 255:
            self.alpha = 255
        self.image.set_alpha(self.alpha)

    def render_gizmos(self):
        super(Comet, self).render_gizmos()
        pygame.draw.circle(self.frame_surface, pygame.Color("green"), (self.circle_trigger.x, self.circle_trigger.y),
                           self.circle_trigger.radius, 3)

    def destroy(self):
        super(Comet, self).destroy()
        CometManager.Instantiated_Comets.remove(self)
