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
        display.loading_screen()
        run_game_menu(player_name)
        run_song_selection()
        run_start_round(player_name)

def main():
    global player_name
    mixer.init()
    display.set_screen_size(80,40)
    display.loading_screen()
    player_name = util.get_player_name()
    display.advice_screen()
    display.copyright_disclaimer_screen()
    game_loop()


if __name__ == "__main__":
    main()
