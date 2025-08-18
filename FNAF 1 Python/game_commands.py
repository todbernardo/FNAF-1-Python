import sys

import pygame
import game_AI as ai
import game_events as events

pygame.init()
pygame.mixer.init()

close_open_left = "🚫 Close left door"
close_open_right = "🚫 Close right door"
light_up_off_left = "🌟 Light up left hall"
light_up_off_right = "🌟 Light up right hall"
pull_up_down_cam = "📷 Enter/leave cams"
energy_usage = 0

left_door_controller = False
right_door_controller = False
left_light_controller = False
right_light_controller = False
cam_controller = False

office_ambience_sound = pygame.mixer.Sound('C:\FNAF 1 Python VSCode\FNAF-1-Python\FNAF 1 Python\sfx\office_ambience.mp3')
door_triggering_sound = pygame.mixer.Sound('C:\FNAF 1 Python VSCode\FNAF-1-Python\FNAF 1 Python\sfx\door_triggering.ogg')
light_triggering_sound = pygame.mixer.Sound('C:\FNAF 1 Python VSCode\FNAF-1-Python\FNAF 1 Python\sfx\light_triggering.ogg')
cam_pull_sound = pygame.mixer.Sound('C:\FNAF 1 Python VSCode\FNAF-1-Python\FNAF 1 Python\sfx\cam_pull_up.ogg')
cam_put_down_sound = pygame.mixer.Sound('C:\FNAF 1 Python VSCode\FNAF-1-Python\FNAF 1 Python\sfx\cam_put_down.ogg')
cam_moving_sound = pygame.mixer.Sound('C:\FNAF 1 Python VSCode\FNAF-1-Python\FNAF 1 Python\sfx\cam_moving_sound.ogg')

def convert_eu_to_emoji():
    match energy_usage:
        case 0:
            return ""
        case 1:
            return "🟩"
        case 2:
            return "🟩🟩"
        case 3:
            return "🟩🟩🟨"
        case 4:
            return "🟩🟩🟨🟥"

def print_menu(energy, hour):
    print("\033[H\033[2J")

    sys.stdout.write(f'''
1 - {close_open_left}
2 - {close_open_right}
3 - {light_up_off_left}
4 - {light_up_off_right}
5 - {pull_up_down_cam}
ENERGY: {energy}%
{convert_eu_to_emoji()}
{hour} AM
''')
    sys.stdout.flush()

def commands_menu(energy):

    events.hours_count()
    pygame.display.set_mode((1, 1))
    office_ambience_sound.play(-1)
    office_ambience_sound.set_volume(0.1)

    print_menu(energy, events.hours_count())

    while True:
        events.hours_count()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if not cam_controller:
                    if event.key == pygame.K_1:
                        trigger_left_door()
                        print_menu(energy, events.hours_count())
                    elif event.key == pygame.K_2:
                        trigger_right_door()
                        print_menu(energy, events.hours_count())
                    elif event.key == pygame.K_3:
                        light_left_door("") 
                        print_menu(energy, events.hours_count())
                    elif event.key == pygame.K_4:
                        light_right_door("")
                        print_menu(energy, events.hours_count())
                if event.key == pygame.K_5:
                    cam_pull(energy)

def trigger_left_door():
    global left_door_controller, close_open_left, energy_usage

    if not left_door_controller:
        door_triggering_sound.play()
        energy_usage += 1

        close_open_left = "✅ Open left door"
        left_door_controller = True
    else:
        door_triggering_sound.play()
        energy_usage -= 1

        close_open_left = "🚫 Close left door"
        left_door_controller = False
###################################################

def trigger_right_door():
    global right_door_controller, close_open_right, energy_usage

    if not right_door_controller :
        door_triggering_sound.play()
        energy_usage += 1

        close_open_right = "✅ Open right door"
        right_door_controller = True
    else:
        door_triggering_sound.play()
        energy_usage -= 1

        close_open_right = "🚫 Close right door"
        right_door_controller = False
###################################################

def light_left_door(animatronic):
    global left_light_controller, light_up_off_left, right_light_controller, light_up_off_right, energy_usage

    if not left_light_controller:
        light_triggering_sound.play()
        energy_usage += 1

        light_up_off_left = "⚫ Light off left hall"

        if right_light_controller == True:
            right_light_controller = False
            light_up_off_right = "🌟 Light up right hall"
            energy_usage -= 1

        left_light_controller = True

    else:
        light_triggering_sound.stop()
        energy_usage -= 1

        light_up_off_left = "🌟 Light up left hall"
        left_light_controller = False

    if events.is_at_left_window(animatronic):
        print(animatronic + " is at your left window ⚠️")

###################################################

def light_right_door(animatronic):
    global right_light_controller, light_up_off_right, left_light_controller, light_up_off_left, energy_usage

    if not right_light_controller :
        light_triggering_sound.play()
        energy_usage += 1

        light_up_off_right = "⚫ Light off right hall"

        if left_light_controller == True:
            left_light_controller = False
            light_up_off_left = "🌟 Light up left hall"
            energy_usage -= 1

        right_light_controller = True
    else:
        light_triggering_sound.stop()
        energy_usage -= 1

        light_up_off_right = "🌟 Light up right hall"
        right_light_controller = False


    if events.is_at_right_window(animatronic):
        print(animatronic + " is at your right window ⚠️")

###################################################

def print_cam_map():
    print("\033[H\033[2J")
    sys.stdout.write('''
Press the number to check the cam:
                     
                            ┌───────┐
                            │CAM 1  │
                            └───┬───┘
                          ┌─────┘  
                      ┌───────┐
                      │CAM 2  │                        ┌───────┐
                      └───┬───┘                        │CAM 7  │
                          │                            └───┬───┘
            ┌───────┐     │    ┌───────────────────────────┘
            │CAM 3  │─────│    │   
            └───────┘     │    │             ┌────────────┐
                     ┌────┘    │             │            │
                 ┌───────┐     │             │        ┌───────┐
                 │CAM 4  │     │             │        │CAM 6  │
                 └───────┘     │             │        └───────┘
                     └──────┐  │             │     
                            │  │            ┌┘
            ┌───────┐    ┌───────┐     ┌───────┐
            │CAM 5  │────│CAM 8  │     │CAM 10 │
            └───────┘    └───────┘     └───────┘
                             │              │ 
                         ┌───────┐     ┌───────┐
                         │CAM 9  │     │CAM 11 │
                         └───────┘     └───────┘
                               │   YOU   │
                               └─────────┘       
                        ''')
    sys.stdout.flush()

def cam_pull(energy):
    global cam_controller, energy_usage

    if not cam_controller :
        print_cam_map()
        cam_pull_sound.play()
        cam_moving_sound.play()
        office_ambience_sound.set_volume(0.03)
        energy_usage += 1
        cam_controller = True
    else:
        cam_put_down_sound.play()
        cam_pull_sound.stop()
        cam_moving_sound.stop()
        office_ambience_sound.set_volume(0.1)
        energy_usage -= 1
        cam_controller = False
        print_menu(energy, events.hours_count())

