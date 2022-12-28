import pygame
from pygame import *
from entities.comet import CometManager
from entities.entity import Entity
from entities.player import Player
from scene import Scene

pygame.init()
frame_surface = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
fps_target = 60

# game scene
list_of_entities_game_scene: list[Entity] = []
back_ground = Entity(pygame.Vector2(0, 0), frame_surface, list_of_entities_game_scene, "assets/BG.jpg")
back_ground.scale_img(0.75)
player = Player(frame_surface, list_of_entities_game_scene)
comet_manager = CometManager(frame_surface, list_of_entities_game_scene)
game_scene = Scene(list_of_entities_game_scene, frame_surface)

# menu scene
list_of_entities_menu_scene: list[Entity] = []
test_obj = Entity(pygame.Vector2(300, 300), frame_surface, list_of_entities_menu_scene, "assets/comet.png")
menu_scene = Scene(list_of_entities_menu_scene, frame_surface)

# GAME LOOP
current_scene = game_scene
running = True
while running:

    clock.tick(fps_target)
    pygame.display.set_caption(f"FPS: {clock.get_fps():.2f}")

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_p:
                print(len(list_of_entities_game_scene))
            if event.key == K_q:
                current_scene = menu_scene
            if event.key == K_e:
                current_scene = game_scene
        elif event.type == QUIT:
            running = False

    #if CometManager.GameOver:
        #continue
    current_scene.update_scene()
    current_scene.wrap_around_scene()
    current_scene.render_scene()
    current_scene.render_gizmos_scene()

    # frame update
    pygame.display.update()