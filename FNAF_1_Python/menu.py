import pygame
import memory
import os

def play_menu_theme():
    pygame.init()

    BASE_DIR = os.path.dirname(__file__)

    pygame.mixer_music.load(os.path.join(BASE_DIR, 'sfx', 'main_menu.mp3'))
    pygame.mixer_music.play(-1)

def show_menu(night):
    choice = ""

    if 0 < night <= 1:
         choice = input("1 - New game\n").strip()

         if choice == "1":
             pygame.mixer_music.stop()
             memory.new_game()

    elif 1 < night <= 5:
         choice = (
input('''
1 - New game
2 - Continue
''').strip())

    if choice == "1" or choice == "2":
        pygame.mixer_music.stop()
        memory.continuee(night)


