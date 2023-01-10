from pygame import mixer
from song_selection import run_song_selection
from game_menu import run_game_menu
from start_round import run_start_round
import displays as display
import utils as util

player_name = None  # stores the player's name
player_choice = None  # stores th   e every action of the player.
player_points = 0  # stores the points of the user once the round started

def game_loop():
    while True:
        # run_game_menu(player_name)
        run_song_selection()
        run_start_round()

def main():
    mixer.init()
    # start_game_menu(player_name)
    # play sound
    # util.play_sound("sounds\\Song musics\\2020's\\Fallen - Lola Amour.wav")
    display.set_screen_size(80,40)
    # display.loading_screen()
    # player_name = util.get_player_name()
    # display.advice_screen()
    # display.copyright_disclaimer_screen()
    game_loop()


if __name__ == "__main__":
    main()
