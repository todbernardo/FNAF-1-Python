import sys
import game_AI as ai
import os
import pygame
import game_commands as cmds
import game_events as events

BASE_DIR = os.path.dirname(__file__)
loop = True

def check_cams(cam, animatronic):
    None

def check_cam_inputs(energy):
    global BASE_DIR
    global loop
    cam_swap = pygame.mixer.Sound(os.path.join(BASE_DIR, "sfx", "cam_swap.ogg"))

    while loop == True:
        for event in pygame.event.get():
            if cmds.cam_controller == True:
                if event.type == pygame.KEYDOWN:
                    cam_swap.play()
                    if event.key == pygame.K_1:
                        None
                    elif event.key == pygame.K_2:
                        None
                    elif event.key == pygame.K_3:
                        None
                    elif event.key == pygame.K_4:
                        None
                    elif event.key == pygame.K_e:
                        None
                    elif event.key == pygame.K_6:
                        sys.stdout.write("Cam disabled")
                    elif event.key == pygame.K_7:
                        None
                    elif event.key == pygame.K_a:
                        None
                    elif event.key == pygame.K_b:
                        None
                    elif event.key == pygame.K_c:
                        None
                    elif event.key == pygame.K_d:
                        None
                    elif event.key == pygame.K_5:
                        loop = False
    loop = True
    cmds.cam_pull(energy)
