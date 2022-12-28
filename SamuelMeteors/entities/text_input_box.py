import pygame

from entities.comet import CometManager
from entities.entity import Entity
from files.file_manager_system import FileManager
from utilities.key_tracker import KeyTracker
from utilities.rect_trigger import RectTrigger


class TextInputBox(Entity):
    def __init__(self, go_to_score_sheet_scene_func, initial_position, width, height, frame_surface, list_of_entities: list):
        super().__init__(initial_position, frame_surface, list_of_entities)

        self.go_to_score_sheet_scene_func = go_to_score_sheet_scene_func

        self.__FONT_SIZE = 25
        self.__font = pygame.font.Font('freesansbold.ttf', self.__FONT_SIZE)

        self.color = (255, 255, 255)
        self.backcolor = None
        self.width = width
        self.height = height
        self.__is_active = True
        self.text = ""
        self.render_text()
        self.rect_trigger = RectTrigger(self.position, self.width, self.height)

        self.keys = [
            ["a", KeyTracker(pygame.K_a)], ["b", KeyTracker(pygame.K_b)],
            ["c", KeyTracker(pygame.K_c)], ["d", KeyTracker(pygame.K_d)],
            ["e", KeyTracker(pygame.K_e)], ["f", KeyTracker(pygame.K_f)],
            ["g", KeyTracker(pygame.K_g)], ["h", KeyTracker(pygame.K_h)],
            ["i", KeyTracker(pygame.K_i)], ["j", KeyTracker(pygame.K_j)],
            ["k", KeyTracker(pygame.K_k)], ["l", KeyTracker(pygame.K_l)],
            ["m", KeyTracker(pygame.K_m)], ["n", KeyTracker(pygame.K_n)],
            ["o", KeyTracker(pygame.K_o)], ["p", KeyTracker(pygame.K_p)],
            ["q", KeyTracker(pygame.K_q)], ["r", KeyTracker(pygame.K_r)],
            ["s", KeyTracker(pygame.K_s)], ["t", KeyTracker(pygame.K_t)],
            ["u", KeyTracker(pygame.K_u)], ["v", KeyTracker(pygame.K_v)],
            ["x", KeyTracker(pygame.K_x)], ["y", KeyTracker(pygame.K_y)],
            ["z", KeyTracker(pygame.K_z)], ["ENTER", KeyTracker(pygame.K_RETURN)]
        ]

    def update(self):
        if not self.__is_active:
            return

        if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
            self.text = self.text[:-1]
            self.render_text()

        for key in self.keys:
            key[1].update_tracker()
        for i in range(len(self.keys)):
            if self.keys[i][1].has_key_been_fired_at_this_frame_read_only:
                if self.keys[i][0] == "ENTER":
                    if len(self.text) == 3:
                        FileManager.write_new_row_in_csv_file("files/scores.csv", [self.text, str(CometManager.Score)])
                        FileManager.sort_csv_file_by_column_values("files/scores.csv", 1)
                        self.go_to_score_sheet_scene_func()
                    else:
                        print("please insert exactly 3 characters")
                    return
                self.text += self.keys[i][0]
                self.render_text()

    def render_text(self):
        t_surf = self.__font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((max(self.width, t_surf.get_width()+10), t_surf.get_height()+20), pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 10))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)



