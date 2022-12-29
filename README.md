#  Fundamentos_Programa-o_Mini.Projeto.2_Comets
## Members

Samuel Carvalho / Nº a 22201379

## What each one have done
Since i worked in this project alone, it can be said that i was the one who have done everything. Of course, with help of some collegues.

## Game Mechanics

### Starting of the project
This project was started like many others, by setting the game window and creating the main loop of the game.

#

    def __init__(self):
        pygame.init()
        frame_surface = pygame.display.set_mode((800, 600))
        middle_screen_position = pygame.Vector2(frame_surface.get_width() / 2, frame_surface.get_height() / 2)
        self.clock = pygame.time.Clock()
        self.fps_target = 60

#       
        
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

'

### Creation of the player
After setting the main loop and the background, the next thing that was done was the creation of the player and it's statistics like movement, acceleration and etc.

'

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
        
'
