import pygame

from entities.entity import Entity


class ScoreRegistrationTextHolder(Entity):

    def __init__(self, frame_surface, list_of_entities: list):

        mid_screen = pygame.Vector2(frame_surface.get_width()/2, frame_surface.get_height()/2)

        super().__init__(mid_screen, frame_surface, list_of_entities)

        self.image = pygame.Surface((frame_surface.get_width(), frame_surface.get_height()))
        self.image.set_alpha(130)
        self.image_rect = self.image.get_rect(center=self.position)

        self.text_color = pygame.Color("white")
        self.font_size = 33
        self.font = pygame.font.Font('freesansbold.ttf', self.font_size)

        self.text1 = f"CONGRATULATIONS!"
        self.text1_surf = self.font.render(self.text1, True, self.text_color)
        self.image.blit(self.text1_surf, (mid_screen.x - self.text1_surf.get_width() / 2, 70))

        self.text2 = "YOU HAVE REACHED THE TOP 10"
        self.text2_surf = self.font.render(self.text2, True, self.text_color)
        self.image.blit(self.text2_surf, (mid_screen.x - self.text2_surf.get_width() / 2, 120))

        self.text3 = "INSERT YOUR NAME"
        self.text3_surf = self.font.render(self.text3, True, self.text_color)
        self.image.blit(self.text3_surf, (mid_screen.x - self.text3_surf.get_width() / 2, 170))

        self.text4 = "TO REGISTER YOUR SCORE:"
        self.text4_surf = self.font.render(self.text4, True, self.text_color)
        self.image.blit(self.text4_surf, (mid_screen.x - self.text4_surf.get_width() / 2, 220))

        self.text5 = "Please insert 3 characters only! Press ENTER to registrate."
        self.font = pygame.font.Font('freesansbold.ttf', 25)
        self.text5_surf = self.font.render(self.text5, True, self.text_color)
        self.image.blit(self.text5_surf, (mid_screen.x - self.text5_surf.get_width() / 2, 400))



