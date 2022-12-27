import pygame
from pygame import *
from entity import Entity
from player import Player

pygame.init()

s_width = 800
s_height = 600

frame_surface = pygame.display.set_mode((s_width, s_height))
clock = pygame.time.Clock()
fps_target = 60

list_of_entities: list[Entity] = []

back_ground = Entity(pygame.Vector2(0,0), frame_surface, list_of_entities, "assets/BG.jpg")
player = Player(frame_surface, list_of_entities, "assets/SpaceshipRed.png")

running = True
while running:

    clock.tick(fps_target)
    pygame.display.set_caption(f"FPS: {clock.get_fps():.2f}")

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_p:
                print(len(list_of_entities))
        elif event.type == QUIT:
            running = False

    # clears frame
    frame_surface.fill(pygame.Color("blue"))

    # UPDATE
    for entity in list_of_entities:
        entity.update()

    for entity in list_of_entities:
        entity.wrap_around()

    # RENDER
    for entity in list_of_entities:
        entity.render()

    # RENDER GIZMOS
    for entity in list_of_entities:
        entity.render_gizmos()

    # frame update
    pygame.display.update()