import time
import pygame
import game_commands as cmds
import random as rand
import show_texts as st
import game_AI as ai
import threading
import jumpscares

pygame.init()
pygame.mixer.init()

hour = 0
energy = 100
start_time = pygame.time.get_ticks()

def hours_count():
    global energy, hour, start_time

    now = pygame.time.get_ticks()
    elapsed = (now - start_time) // 1000
    target_hour = min(elapsed // 130, 6)

    if target_hour > hour:
        hour = target_hour
        cmds.print_menu(energy, hour)
    
    return hour

def start_game(night):
    print("\033[H\033[2J")

    st.show_nights(night)
    time.sleep(2)

    if hour < 6:
        ai.animatronic_on()
    else:
        ai.animatronic_off()
        six_am()

    if energy > 0:
        cmds.commands_menu(energy)
    else:
        power_out()
    
def six_am():
    global hour
    
    if hour == 6:
        def play_six_am_sound():
            pygame.mixer.music.load('C:\FNAF 1 Python VSCode\FNAF-1-Python\FNAF 1 Python\sfx\six_am_sound.mp3')
            pygame.mixer.music.play()
            time.sleep(10)
            pygame.mixer.music.stop()

        animation_thread = threading.Thread(target=st.show_six_am_screen, args=(1,))
        sound_thread = threading.Thread(target=play_six_am_sound)

        animation_thread.start()
        sound_thread.start()
        
def is_at_left_window(animatronic):
    print(animatronic)

def is_at_right_window(animatronic):
    print(animatronic)

def jumpscare(animatronic):
    pygame.mixer.music.load('C:\FNAF 1 Python VSCode\FNAF-1-Python\FNAF 1 Python\sfx\static.ogg')
    pygame.mixer.music.play()
    time.sleep(6.5)
    pygame.mixer.music.stop()

    match animatronic:
        case "freddy":
            jumpscares.freddy_jumpscare()
        case "bonnie":
            jumpscares.bonnie_jumpscare()
        case "chica": 
            jumpscares.chica_jumpscare()
        case "foxy":
            jumpscares.foxy_jumpscare()
        case "golden_freddy":
            pygame.music.mixer.load('C:\FNAF 1 Python VSCode\FNAF-1-Python\FNAF 1 Python\sfx\golden_freddy_scream.mp3')
            pygame.music.mixer.play()
            time.sleep(6)
            pygame.music.mixer.stop()


def power_out():

    power_outage = pygame.mixer.Sound('C:\FNAF 1 Python VSCode\FNAF-1-Python\FNAF 1 Python\sfx\power_outage.mp3')
    freddys_song = pygame.mixer.Sound('C:/FNAF 1 Python VSCode/FNAF-1-Python/FNAF 1 Python/sfx/freddys_song.mp3')

    print("\033[H\033[2J")
    print("Power's out! ⚡💥")
    
    power_outage.play()
    power_noise_time = rand.randint(5, 7)
    time.sleep(power_noise_time)
    pygame.mixer.music.stop()

    freddys_song.play()
    song_time = rand.randint(6, 10)
    time.sleep(song_time)

    power_outage.stop()
    freddys_song.stop()

    pygame.mixer.music.load('C:\FNAF 1 Python VSCode\FNAF-1-Python\FNAF 1 Python\sfx\jumpscare.mp3')
    time.sleep(2.5)
    pygame.mixer.music.play()
    jumpscares.freddy_jumpscare()
    time.sleep(1)
    pygame.mixer.music.stop()

    pygame.mixer.music.load('C:\FNAF 1 Python VSCode\FNAF-1-Python\FNAF 1 Python\sfx\static.ogg')
    pygame.mixer.music.play()
    time.sleep(6.5)
    pygame.mixer.music.stop()


