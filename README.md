#  Fundamentos_Programa-o_Mini.Projeto.2_Comets
## Members

Samuel Carvalho / Nº a 22201379

## What each one have done
Since i worked in this project alone, it can be said that i was the one who have done everything. Of course, with help of some collegues.

## Game Mechanics

### Starting of the project
This project was started like many others, by setting the game window and creating the main loop of the game.

'''

    def __init__(self):
        pygame.init()
        frame_surface = pygame.display.set_mode((800, 600))
        middle_screen_position = pygame.Vector2(frame_surface.get_width() / 2, frame_surface.get_height() / 2)
        self.clock = pygame.time.Clock()
        self.fps_target = 60
        
'''
