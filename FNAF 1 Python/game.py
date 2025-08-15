import time
import pygame
import game_commands as cmds
import random as rand
import show_night as sn

pygame.mixer.init()

def start_game(night):
    sn.show_night(night)
    time.sleep(2)
    hour = 12
    energy = 100
    energy_usage = 1

    cmds.commands_menu(energy)

def power_out():

    print("Power's out! ⚡ 💥")
    pygame.mixer.music.load('sfx/power_outage.mp3')
    pygame.mixer.music.play()
    power_noise_time = rand.randint(3, 5)
    time.sleep(power_noise_time)
    pygame.mixer.music.stop()

    pygame.mixer.music.load('sfx/freddys_song.mp3')
    pygame.mixer.music.play()
    song_time = rand.randint(5, 10)
    time.sleep(song_time)
    pygame.mixer.music.stop()

    pygame.mixer.music.load('sfx/jumpscare.mp3')
    pygame.mixer.music.play()
    time.sleep(1.3)
    pygame.mixer.music.stop()

