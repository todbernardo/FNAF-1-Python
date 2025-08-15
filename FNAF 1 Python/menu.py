import pygame
import memory

def play_menu_theme():
    pygame.init()
    pygame.mixer_music.load('sfx/main_menu.mp3')
    pygame.mixer_music.play(-1)
    print("MUSICA")

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


