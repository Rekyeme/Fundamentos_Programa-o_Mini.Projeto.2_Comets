import pygame
from entities.entity import Entity
from files.file_manager_system import FileManager


class ScoreSheetManager(Entity):
    def __init__(self, go_to_menu_scene, frame_surface, list_of_entities: list):

        mid_screen = pygame.Vector2(frame_surface.get_width()/2, frame_surface.get_height()/2)

        super().__init__(mid_screen, frame_surface, list_of_entities)

        self.go_to_menu_scene_func = go_to_menu_scene

        self.image = pygame.Surface((frame_surface.get_width(), frame_surface.get_height()))
        self.image_rect = self.image.get_rect(center=self.position)

    def start(self):
        mid_screen = pygame.Vector2(self.frame_surface.get_width() / 2, self.frame_surface.get_height() / 2)
        self.image.fill(pygame.Color("black"))
        self.text_color = pygame.Color("white")
        self.font_size = 35
        self.font = pygame.font.Font('freesansbold.ttf', self.font_size)

        self.text1 = f"RANKING"
        self.text1_surf = self.font.render(self.text1, True, self.text_color)
        self.image.blit(self.text1_surf, (mid_screen.x - self.text1_surf.get_width() / 2, 70))

        self.font_size = 25
        self.font = pygame.font.Font('freesansbold.ttf', self.font_size)

        mid_screen = pygame.Vector2(self.frame_surface.get_width() / 2, self.frame_surface.get_height() / 2)
        rows = FileManager.read_from_csv_file('files/scores.csv')
        tot = 10 if len(rows) >= 10 else len(rows)
        print(f"tot = {tot}")

        y_initial = 130
        y_current = y_initial
        y_spacing = 40
        for i in range(0, tot):
            text = f"{rows[i][0]}.............{rows[i][1]}"
            text_surf = self.font.render(text, True, self.text_color)
            self.image.blit(text_surf, (mid_screen.x - text_surf.get_width() / 2, y_current))
            y_current = y_current + y_spacing

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.go_to_menu_scene_func()
