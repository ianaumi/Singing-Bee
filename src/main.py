from pygame import mixer
from song_selection import run_song_selection
from game_menu import run_game_menu
from start_round import run_start_round
import displays as display
import utilities as util
import sounds


player_name = None  # stores the player's name
player_choice = None  # stores the every action of the player.


# the main game loop
def game_loop():
    while True:

        # background sound for the game menu
        sounds.play_background("sounds\\Game sounds\\game_menu_background.wav",-1)
        # stores the playername for the game menu
        run_game_menu(player_name)
        # stop the sound after player pressing play
        sounds.stop_sound()

        # background sound for song selection
        sounds.play_background("sounds\\Game sounds\\song_selection_background.wav",-1)
        run_song_selection()

        sounds.stop_sound()
        # starts the round and plays the song
        run_start_round(player_name)


def main():

    global player_name
    # initialize the audio player
    mixer.init()

    # sets the screen to 80 x 40
    display.set_screen_size(80,40)

    # plays the intro sound theme
    sounds.play_background("sounds\\Game sounds\\intro_background.wav",1)
    display.loading_screen()

    # gets the player name
    player_name = util.get_player_name()
    display.advice_screen()
    display.copyright_disclaimer_screen()

    # stops the sound after displaying advice and copyright
    sounds.stop_sound()

    # will proceed to game menu
    game_loop()

    # >>>>>>>>>>>>>>>>> TEST BLOCK <<<<<<<<<<<<<<<<<<<
    # while True:
    #     print(songlist["2000s"]["With a Smile - Eraserheads"]["lyrics"])
    #     # middle line
    #     print("-"*40)
    #     choice = input()
    #     if choice.upper() == 'A':
    #         exit()

if __name__ == "__main__":
    main()