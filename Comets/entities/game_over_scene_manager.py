import pygame

from entities.comet import CometManager
from entities.entity import Entity
from files.file_manager_system import FileManager
from utilities.timer import Timer


class GameOverSceneManager(Entity):

    def __init__(self, go_to_registration_scene_func, go_to_score_sheet_scene_func, frame_surface, list_of_entities: list):
        super().__init__(pygame.Vector2(frame_surface.get_width()/2, frame_surface.get_height()/2), frame_surface, list_of_entities)

        self.text = "GAME OVER"
        self.font_size = 40
        self.text_color = pygame.Color("white")
        self.font = pygame.font.Font('freesansbold.ttf', self.font_size)
        self.text_surf = self.font.render(self.text, True, self.text_color)
        self.image = pygame.Surface((500, 500))
        self.image_rect = self.image.get_rect(center=self.position)
        self.image.blit(self.text_surf, pygame.Vector2(frame_surface.get_width()/2-260, 250))

        # ranking and changing scene
        self.is_ranking = self.should_be_ranked()
        self.exit_timer = Timer(3 * 1000)
        self.go_to_registration_scene_func = go_to_registration_scene_func
        self.go_to_score_sheet_scene_func = go_to_score_sheet_scene_func

    def start(self):
        self.is_ranking = self.should_be_ranked()
        self.exit_timer.activate()
        self.exit_timer.timer_update()

    def update(self):
        self.exit_timer.timer_update()
        if not self.exit_timer.is_timer_active_read_only:
            if self.is_ranking:
                self.go_to_registration_scene_func()
            else:
                self.go_to_score_sheet_scene_func()

    def should_be_ranked(self) -> bool:
        path = "files/scores.csv"
        FileManager.sort_csv_file_by_column_values(path, 1)
        rows = FileManager.read_from_csv_file(path)
        print(f"{rows}")

        print(f"score: {CometManager.Score}")
        if CometManager.Score == 0:
            print("did not scored")
            return False

        if len(rows) < 10:
            print("<10")
            return True

        last_guy_score = int(rows[9][1])
        if CometManager.Score > last_guy_score:
            print(f"last guy points: {last_guy_score}")
            return True

        print("default false, did not scored enough")
        return False

