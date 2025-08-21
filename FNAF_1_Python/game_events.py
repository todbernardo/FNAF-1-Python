import time
import pygame
import game_commands as cmds
import random as rand
import show_texts as st
import game_AI as ai
import threading
import os
import jumpscares

pygame.init()
pygame.mixer.init()

BASE_DIR = os.path.dirname(__file__)

hour = 0
energy = 99.9
start_time = pygame.time.get_ticks()

def start_game(night):
    print("\033[H\033[2J")

    st.show_nights(night)
    time.sleep(2)

    if energy > 0:
        cmds.commands_menu(energy, night)
    else:
        if hour < 6:
            power_out()
        else:
            six_am()
    
def hours_count():
    global energy, hour, start_time

    now = pygame.time.get_ticks()
    elapsed = (now - start_time) // 1000
    target_hour = min(elapsed // 90, 6)

    if target_hour > hour:
        hour = target_hour
        cmds.print_menu(energy, hour)
    
    return hour

def energy_bars_drain(controllers):
    for controller in controllers:
        if controller == True:
            # energy_consumption()
            None
            
def six_am():
    global hour
    
    if hour == 6:
        def play_six_am_sound():
            global BASE_DIR

            cmds.office_ambience_sound.stop()
            pygame.mixer.music.load(os.path.join(BASE_DIR, 'sfx', 'six_am_sound.mp3'))
            pygame.mixer.music.play()
            time.sleep(10)
            pygame.mixer.music.stop()

        animation_thread = threading.Thread(target=st.show_six_am_screen, args=(1,))
        sound_thread = threading.Thread(target=play_six_am_sound)

        animation_thread.start()
        sound_thread.start()
        
        animation_thread.join()
        sound_thread.join()
        
def is_at_left_window():
    None

def is_at_right_window():
    None

def jumpscare(animatronic):
    global BASE_DIR

    pygame.mixer.music.load(os.path.join(BASE_DIR, 'sfx', 'static.ogg'))
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
            pygame.music.mixer.load(os.path.join(BASE_DIR, 'sfx', 'golden_freddy_scream.mp3'))
            pygame.music.mixer.play()
            time.sleep(6)
            pygame.music.mixer.stop()


def power_out():
    global BASE_DIR

    power_outage = pygame.mixer.Sound(os.path.join(BASE_DIR, 'sfx', 'power_outage.mp3'))
    freddys_song = pygame.mixer.Sound(os.path.join(BASE_DIR, 'sfx', 'freddys_song.mp3'))

    print("\033[H\033[2J")
    print("Power's out! ⚡💥")
    
    power_outage.play()
    power_noise_time = rand.randint(6, 9)
    time.sleep(power_noise_time)
    pygame.mixer.music.stop()

    freddys_song.play()
    song_time = rand.randint(6, 10)
    time.sleep(song_time)

    power_outage.stop()
    freddys_song.stop()

    pygame.mixer.music.load(os.path.join(BASE_DIR, 'sfx', 'jumpscare.mp3'))
    time.sleep(2.5)
    pygame.mixer.music.play()
    jumpscares.freddy_jumpscare()
    time.sleep(1)
    pygame.mixer.music.stop()

    pygame.mixer.music.load(os.path.join(BASE_DIR, 'sfx', 'static.ogg'))
    pygame.mixer.music.play()
    time.sleep(6.5)
    pygame.mixer.music.stop()


