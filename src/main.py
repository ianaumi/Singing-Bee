from song_selection import run_song_selection
from start_round import run_start_round
from game_menu import run_game_menu
from pygame import mixer
import displays as display
from displays import logo
import utilities as util
import sounds
import os


player_name = None  # stores the player's name
player_choice = None  # stores the every action of the player.


# the main game loop
def game_loop():
    while True:

        # background sound for the game menu
        sounds.play_background("sounds/game_sounds\\game_menu_background.wav", -1)

        # stores the player name for the game menu
        run_game_menu(player_name)

        # stop the sound after player pressing play
        sounds.stop_sound()

        # background sound for song selection
        sounds.play_background("sounds/game_sounds\\song_selection_background.wav", -1)
        run_song_selection()

        sounds.stop_sound()
        # starts the round and plays the song
        run_start_round(player_name)


def main():
    global player_name
    # initialize the audio player
    mixer.init()

    # sets the screen to 80 x 40
    display.set_screen_size(80, 40)

    # plays the intro sound theme
    sounds.play_background("sounds/game_sounds\\intro_background.wav", -1)
    display.loading_screen()

    player_name = util.ask_to_login()
    display.clear_screen()
    display.welcome_back(player_name)

    display.clear_screen()
    display.advice_screen()
    display.copyright_disclaimer_screen()

    # stops the sound after displaying advice and copyright
    sounds.stop_sound()

    # will proceed to game menu
    game_loop()


if __name__ == "__main__":
    main()
