import sys

import pygame
from pygame import *

from entities.button import Button
from entities.comet import CometManager
from entities.entity import Entity
from entities.player import Player
from entities.game_over_scene_manager import GameOverSceneManager
from entities.score_registration_text_holder import ScoreRegistrationTextHolder
from entities.score_sheet_manager import ScoreSheetManager
from entities.text_input_box import TextInputBox
from utilities.scene import Scene


class GameLoop:

    def __init__(self):
        pygame.init()
        frame_surface = pygame.display.set_mode((800, 600))
        middle_screen_position = pygame.Vector2(frame_surface.get_width() / 2, frame_surface.get_height() / 2)
        self.clock = pygame.time.Clock()
        self.fps_target = 60

        self.__current_scene: Scene = None

        # game scene
        list_of_entities_game_scene: list[Entity] = []
        back_ground = Entity(pygame.Vector2(0, 0), frame_surface, list_of_entities_game_scene, "assets/BG.jpg")
        back_ground.scale_img(0.75)
        comet_manager = CometManager(self.go_to_game_over_scene, frame_surface, list_of_entities_game_scene)
        player = Player(frame_surface, list_of_entities_game_scene)
        self.__game_scene = Scene(list_of_entities_game_scene, frame_surface)

        # menu scene
        list_of_entities_menu_scene: list[Entity] = []
        background = Entity(pygame.Vector2(0, 0), frame_surface, list_of_entities_menu_scene, "assets/BG.jpg")
        buttons_background = Entity(middle_screen_position, frame_surface, list_of_entities_menu_scene, "assets/Comets_Startscreen.png")
        buttons_background.scale_img(1.3)
        start_button = Button("assets/Start_Button_Unpressed.png", "assets/Start_Button_Pressed.png", 1, self.go_to_game_scene, pygame.Vector2(400, 290), frame_surface, list_of_entities_menu_scene)
        exit_button = Button("assets/Exit_Button_Unpressed.png", "assets/Exit_Button_Pressed.png", 1, self.quit,  pygame.Vector2(400, 370), frame_surface, list_of_entities_menu_scene)
        self.__menu_scene = Scene(list_of_entities_menu_scene, frame_surface)

        # game over scene
        list_of_entities_game_over_scene = []
        background = Entity(pygame.Vector2(0, 0), frame_surface, list_of_entities_game_over_scene, "assets/BG.jpg")
        game_over_scene_manager = GameOverSceneManager(self.go_to_score_registration_scene, self.got_to_score_sheet_scene, frame_surface, list_of_entities_game_over_scene)
        self.__game_over_scene = Scene(list_of_entities_game_over_scene, frame_surface)

        # score registration scene
        list_of_entities_score_registration_scene = []
        background = Entity(pygame.Vector2(0, 0), frame_surface, list_of_entities_score_registration_scene, "assets/BG.jpg")
        score_registration_text_holder = ScoreRegistrationTextHolder(frame_surface, list_of_entities_score_registration_scene)
        text_input = TextInputBox(self.got_to_score_sheet_scene, middle_screen_position, 90, 70, frame_surface, list_of_entities_score_registration_scene)
        self.__score_registration_scene = Scene(list_of_entities_score_registration_scene, frame_surface)

        # score-sheet scene
        list_of_entities_score_sheet_scene = []
        background = Entity(pygame.Vector2(0, 0), frame_surface, list_of_entities_score_sheet_scene, "assets/BG.jpg")
        score_sheet_manager = ScoreSheetManager(self.go_to_menu_scene, frame_surface, list_of_entities_score_sheet_scene)
        self.__score_sheet_scene = Scene(list_of_entities_score_sheet_scene, frame_surface)

    def got_to_score_sheet_scene(self):
        self.__current_scene = self.__score_sheet_scene
        self.__current_scene.start_scene()

    def go_to_score_registration_scene(self):
        self.__current_scene = self.__score_registration_scene
        self.__current_scene.start_scene()

    def go_to_game_over_scene(self):
        self.__current_scene = self.__game_over_scene
        self.__current_scene.start_scene()

    def go_to_menu_scene(self):
        self.__current_scene = self.__menu_scene
        self.__current_scene.start_scene()

    def go_to_game_scene(self):
        self.__current_scene = self.__game_scene
        self.__current_scene.start_scene()

    def quit(self):
        pygame.quit()
        sys.exit()

    # GAME LOOP
    def run(self):

        if self.__current_scene is None:
            self.go_to_menu_scene()
        running = True

        while running:
            self.clock.tick(self.fps_target)
            pygame.display.set_caption(f"FPS: {self.clock.get_fps():.2f}")

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        print(len(self.__current_scene.list_of_entities))
                    if event.key == K_ESCAPE:
                        self.go_to_menu_scene()
                elif event.type == QUIT:
                    running = False

            self.__current_scene.update_scene()
            self.__current_scene.wrap_around_scene()
            self.__current_scene.render_scene()
            #self.__current_scene.render_gizmos_scene()

            # frame update
            pygame.display.update()


GameLoop().run()