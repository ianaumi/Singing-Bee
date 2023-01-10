import json
from pygame import mixer
from song_selection import song_selection
from game_menu import start_game_menu
import displays as display
import utils as util

year_choice = []  # stores the year choice of player
song_choice = []  # stores the song choice of player
choice = {}  # stores the keys player can press and use it to call the key from the song list json file
player_name = "mimi"  # stores the player's name
player_choice = None  # stores th   e every action of the player.
player_points = 0  # stores the points of the user once the round started
# hints = 3

def main():
    mixer.init()
    # start_game_menu(player_name)
    # play sound
    util.play_sound("sounds\\Song musics\\2020's\\Fallen - Lola Amour.wav")
    # displays.set_screen_size(80,40)
    # display.set_screen_size(80,40)
    # display.loading_screen()
    # player_name = util.get_player_name()
    # display.advice_screen()
    # display.copyright_disclaimer_screen()
    # song_selection(year_choice,song_choice,choice)


if __name__ == "__main__":
    main()
