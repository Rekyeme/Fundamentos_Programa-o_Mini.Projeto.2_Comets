import enum
import pygame
import math
import random
from utilities.circle_trigger import CircleTrigger
from entities.bullet import Bullet
from entities.entity import Entity
from entities.player import Player
from utilities.timer import Timer


# ======================================================================================================================
# ======================================================================================================================


class Rank(enum.Enum):
    Big = 1,
    Mid = 2,
    Small = 3


# ======================================================================================================================
# ======================================================================================================================


class CometManager(Entity):

    GameOver = False
    Instantiated_Comets = []
    Score = 0

    def __init__(self, go_to_game_over_func, frame_surface, list_of_entities: list):
        super().__init__(pygame.Vector2(400, 15), frame_surface, list_of_entities)

        # got to game over func is used to set the score at the score sheet
        self.go_to_game_over_func = go_to_game_over_func

        self.text = f"score: {self.Score}"
        self.font_size = 25
        self.text_color = pygame.Color("white")
        self.font = pygame.font.Font('freesansbold.ttf', self.font_size)
        self.text_surf = self.font.render(self.text, True, self.text_color)
        self.image = pygame.Surface((200, 30))
        self.image_rect = self.image.get_rect(center=self.position)
        self.image.blit(self.text_surf, (0, 0))

        self.last_score = 0

        # limpa a cena por 1 segundo. saí libera os meteoros para serem instanciados
        self.timer = Timer(1*1000)

    def start(self):
        CometManager.Score = 0
        self.update_score_text()
        CometManager.GameOver = False
        self.try_to_clean_up_scene_from_comets()
        self.timer.activate()
        self.timer.timer_update()

    def update(self):

        if CometManager.GameOver:
            self.go_to_game_over_func()

        self.timer.timer_update()
        if self.timer.is_timer_active_read_only:
            self.try_to_clean_up_scene_from_comets()
            return

        # make a new big comet whenever there is less than 2 comets on screen
        if len(CometManager.Instantiated_Comets) < 2:
            self.__instantiate_big_comet_at_random_position()
        if self.last_score != CometManager.Score:
            self.update_score_text()
            self.last_score = CometManager.Score

    def try_to_clean_up_scene_from_comets(self):
        for comet in CometManager.Instantiated_Comets:
            comet.destroy()
        for comet in self.list_of_entities:
            if isinstance(comet, Comet):
                comet.destroy()

    def __instantiate_big_comet_at_random_position(self):
        Comet(Rank.Big, pygame.Vector2(random.randint(1, 800-1), random.randint(1, 600-1)), self.frame_surface, self.list_of_entities)

    def update_score_text(self):
        self.text = f"score: {self.Score}"
        self.text_surf = self.font.render(self.text, True, self.text_color)
        self.image.fill(color=pygame.Color("black"))
        self.image.blit(self.text_surf, (0, 0))


# ======================================================================================================================
# ======================================================================================================================


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
                    CometManager.Score += 3
                    for i in range(0, 3):
                        Comet(Rank.Mid, self.position.copy(), self.frame_surface, self.list_of_entities)
                elif self.rank == Rank.Mid:
                    CometManager.Score += 6
                    for i in range(0, 5):
                        Comet(Rank.Small, self.position.copy(), self.frame_surface, self.list_of_entities)
                elif self.rank == Rank.Small:
                    CometManager.Score += 12

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
