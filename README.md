#  Fundamentos_Programa-o_Mini.Projeto.2_Comets

# Members:

Samuel Carvalho / Nº a 22201379

# What each one have done:
Since i worked in this project alone, it can be said that i was the one who have done everything. Of course, with help of some collegues.

# Game Mechanics:

## Starting of the project
This project was started like many others, by setting the game window and creating the main loop of the game.

### Setting the window size -

    def __init__(self):
        pygame.init()
        frame_surface = pygame.display.set_mode((800, 600))
        middle_screen_position = pygame.Vector2(frame_surface.get_width() / 2, frame_surface.get_height() / 2)
        self.clock = pygame.time.Clock()
        self.fps_target = 60

### Game Main Loop -
        
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

## Creation of the player:
After setting the main loop and the background, the next thing that was done was the creation of the player and it's statistics like movement, acceleration and etc.
Inside the player was also set the shoot option.

### Parameters for each actions -

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
        
### Shoot function inside the player -

        def __shoot(self):
            keys = pygame.key.get_pressed()
            self.timer.timer_update()
            if keys[K_SPACE] and not self.timer.is_timer_active_read_only:
                self.timer.activate()
                # instantiate bullet
                bullet_position = self.position.copy()
                Bullet(bullet_position, self.angle, self.move_direction, self.frame_surface,
                       self.list_of_entities, "assets/bullet.png")

### Function regarding the rotation of the player -

        def __rotate(self):
            keys = pygame.key.get_pressed()
            if keys[K_RIGHT]:
                self.angle -= self.angular_velocity
            elif keys[K_LEFT]:
                self.angle += self.angular_velocity
            self.image = pygame.transform.rotate(self.img_original, self.angle)
            self.image_rect = self.image.get_rect(center=self.position)
         
### Function regarding the direction of the player -
        def __generate_move_direction(self):
            angle_in_rads = math.radians(self.angle + 180)
            self.move_direction.x = math.sin(angle_in_rads)
            self.move_direction.y = math.cos(angle_in_rads)
            if self.move_direction.magnitude() != 0:
                self.move_direction = self.move_direction.normalize()
                
### Acceleration -

         def __accelerate(self):
             self.current_move_speed += self.acceleration
             if self.current_move_speed > self.max_move_speed:
                 self.current_move_speed = self.max_move_speed

### Deceleration -

        def __decelerate(self):
            self.current_move_speed -= self.deceleration
            if self.current_move_speed < 0:
                self.current_move_speed = 0
                
### Movement -  

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

## Creation of the bullet:
Like it's possible to observe in the previous code samples there is a shoot function, that will be used to interact with the comets later on. At the time the focus was to define the bullet parameters and for it to be shot from the player and travel throught scene.

### The bullet class -

        class Bullet(Entity):

            Instantiated_Bullets = []

            def __init__(self, initial_position, angle, direction, frame_surface, list_of_entities: list, img_path):
                super().__init__(initial_position, frame_surface, list_of_entities, img_path)

                Bullet.Instantiated_Bullets.append(self)

                self.scale_img(0.03)
                self.angle = angle
                self.direction = direction
                self.bullet_speed = 4
                self.image = pygame.transform.rotate(self.image, angle)

                self.life_time_timer = Timer(4*1000)
                self.life_time_timer.activate()

            def update(self):
                self.position += self.direction * self.bullet_speed
                self.life_time_timer.timer_update()
                if not self.life_time_timer.is_timer_active_read_only:
                    self.destroy()

            def destroy(self):
                super(Bullet, self).destroy()
                Bullet.Instantiated_Bullets.remove(self)
                
## Wrap Around:
After creating and setting the scenario, the player and the bullet, it was time to create the wrap around function. A function in which allows the player and the game objects like the bullet or the comets to appear in the opposite side of the map after exceeding the limits of the himself. Every object as a connection to this function.

            def wrap_around(self):
                if self.image is None:
                    return
                # x
                if self.position.x > self.frame_surface.get_width() + self.image.get_width()/2:
                    self.position.x = 0
                elif self.position.x + self.image.get_width()/2 < 0:
                    self.position.x = self.frame_surface.get_width()
                # y
                if self.position.y > self.frame_surface.get_height() + self.image.get_height() / 2:
                    self.position.y = 0
                elif self.position.y + self.image.get_height()/2 < 0:
                    self.position.y = self.frame_surface.get_height()
                    
## Creation of the comets and the interactions with the other objects:


