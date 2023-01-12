from pygame import mixer
from song_selection import run_song_selection
from game_menu import run_game_menu
from start_round import run_start_round
import displays as display
import utils as util

player_name = None  # stores the player's name
player_choice = None  # stores the every action of the player.

def game_loop():
    while True:
        # display.loading_screen()
        # run_game_menu(player_name)
        run_song_selection()
        run_start_round(player_name)
# hints = 3

def main():
    songlist = util.get_song_list_file()
    global player_name
    mixer.init()
    display.set_screen_size(80,40)
    # >>>>>>>>>>>>>>>>> TEST BLOCK <<<<<<<<<<<<<<<<<<<
    while True:
        print(songlist["2000s"]["With a Smile - Eraserheads"]["lyrics"])
        # middle line
        print("-"*40)
        choice = input()
        if choice.upper() == 'A':
            exit()

    # display.loading_screen()
    # player_name = util.get_player_name()
    # display.advice_screen()
    # display.copyright_disclaimer_screen()
    # game_loop()

    # start_game_menu(player_name)
    # play sound
    # displays.set_screen_size(80,40)
    # display.set_screen_size(80,40)
    # display.loading_screen()
    # player_name = util.get_player_name()
    # display.advice_screen()
    # display.copyright_disclaimer_screen()
    # song_selection(year_choice,song_choice,choice)
    # round_start

if __name__ == "__main__":
    main()
