import pygame
import game_AI as ai
import game as game

pygame.init()
pygame.mixer.init()

close_open_left = "🚫 Close left door"
close_open_right = "🚫 Close right door"
light_up_off_left = "🌟 Light up left hall"
light_up_off_right = "🌟 Light up right hall"
pull_up_down_cam = "📷 Enter/leave cams"
energy_usage = 0
energy_usage_emoji = ""

office_ambience_sound = pygame.mixer.Sound('sfx/office_ambience.mp3')
door_triggering_sound = pygame.mixer.Sound('sfx/door_triggering.ogg')
light_triggering_sound = pygame.mixer.Sound('sfx/light_triggering.ogg')
cam_pull_sound = pygame.mixer.Sound('sfx/cam_pull_up.ogg')
cam_put_down_sound = pygame.mixer.Sound('sfx/cam_put_down.ogg')

def convert_eu_to_emoji():
    global energy_usage_emoji
    match energy_usage:
        case 0:
            energy_usage_emoji = ""
        case 1:
            energy_usage_emoji = "⚡"
        case 2:
            energy_usage_emoji = "⚡⚡"
        case 3:
            energy_usage_emoji = "⚡⚡⚡"
        case 4:
            energy_usage_emoji = "⚡⚡⚡⚡"
        case 5:
            energy_usage_emoji = "⚡⚡⚡⚡⚡"

    return energy_usage_emoji

def commands_menu(energy):

    office_ambience_sound.play(-1)
    office_ambience_sound.set_volume(0.1)

    if energy > 0:
        while True:
            command = (
input(f'''
1 - {close_open_left}
2 - {close_open_right}
3 - {light_up_off_left}
4 - {light_up_off_right}
5 - {pull_up_down_cam}
ENERGY: {energy}%
{convert_eu_to_emoji()}
'''))

            match command:
                case "1":
                    trigger_left_door()
                case "2":
                    trigger_right_door()
                case "3":
                    light_left_door("pedro")
                case "4":
                    light_right_door("gabriel")
                case "5":
                    cam_pull()
                case _:
                    print("INVALID COMMAND")

    else:
        game.power_out()

left_door_controller = 0

def trigger_left_door():
    global left_door_controller
    global close_open_left
    global energy_usage

    left_door_controller += 1

    if left_door_controller % 2 != 0:
        door_triggering_sound.play()
        energy_usage += 1
        close_open_left = "✅ Open left door"
    else:
        door_triggering_sound.play()
        energy_usage -= 1
        close_open_left = "🚫 Close left door"
###################################################
right_door_controller = 0

def trigger_right_door():
    global right_door_controller
    global close_open_right
    global energy_usage

    right_door_controller += 1

    if right_door_controller % 2 != 0:
        door_triggering_sound.play()
        energy_usage += 1
        close_open_right = "✅ Open right door"
    else:
        door_triggering_sound.play()
        energy_usage -= 1
        close_open_right = "🚫 Close right door"
###################################################
left_light_controller = 0

def light_left_door(animatronic):
    global left_light_controller
    global light_up_off_left
    global energy_usage

    left_light_controller += 1

    if left_light_controller % 2 != 0:
        light_triggering_sound.play()
        energy_usage += 1
        light_up_off_left = "⚫ Light off left hall"
    else:
        light_triggering_sound.stop()
        energy_usage -= 1
        light_up_off_left = "🌟 Light up left hall"

    if ai.is_at_left_window(animatronic):
        print(animatronic + " is at your left window ⚠️")
###################################################
right_light_controller = 0

def light_right_door(animatronic):
    global right_light_controller
    global light_up_off_right
    global energy_usage

    right_light_controller += 1

    if right_light_controller % 2 != 0:
        light_triggering_sound.play()
        energy_usage += 1
        light_up_off_right = "⚫ Light off right hall"
    else:
        light_triggering_sound.stop()
        energy_usage -= 1
        light_up_off_right = "🌟 Light up right hall "

    if ai.is_at_right_window(animatronic):
        print(animatronic + " is at your right window ⚠️")
###################################################
cam_pull_controller = 0

def cam_pull():
    global cam_pull_controller
    global cam_pull_left
    global energy_usage

    cam_pull_controller += 1
    if cam_pull_controller % 2 != 0:
        cam_pull_sound.play()
        energy_usage += 1
        office_ambience_sound.set_volume(0.03)
        print('''
                            ┌───────┐
                            │CAM 1A │
                            └───┬───┘
                          ┌─────┘  
                      ┌───────┐
                      │CAM 1B │                        ┌───────┐
                      └───┬───┘                        │CAM 7  │
                          │                            └───┬───┘
            ┌───────┐     │    ┌───────────────────────────┘
            │CAM 5  │─────│    │   
            └───────┘     │    │             ┌────────────┐
                     ┌────┘    │             │            │
                 ┌───────┐     │             │        ┌───────┐
                 │CAM 1C │     │             │        │CAM 6  │
                 └───────┘     │             │        └───────┘
                     └──────┐  │             │     
                            │  │            ┌┘
            ┌───────┐    ┌───────┐     ┌───────┐
            │CAM 3  │────│CAM 2A │     │CAM 4A │
            └───────┘    └───────┘     └───────┘
                         ┌───────┐     ┌───────┐
                         │CAM 2B │     │CAM 4B │
                         └───────┘     └───────┘
                               │   YOU   │
                               └─────────┘       
                        ''')
    else:
        cam_put_down_sound.play()
        office_ambience_sound.set_volume(0.1)
        energy_usage -= 1

