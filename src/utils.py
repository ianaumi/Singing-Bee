import json
from pygame import mixer
from colorama import Fore, Style
from displays import clear_screen,print_position,logo


def get_song_list_file():
    with open('songList.json') as f:
        song_list = json.load(f)
    return song_list
def play_sound(path):
    mixer.music.load(path)
    mixer.music.play()

def stop_sound():
    mixer.music.stop()

def list_is_empty(chosen_songs):
    if not chosen_songs:
        return True
    else:
        return False


def options(keys):
    option = keys
    return option

def get_input_position(line, column):
    print("\n"*line, " " * column, end="")
    player_choice = input(f"{Fore.YELLOW}{Style.BRIGHT}>> {Fore.WHITE}")
    return player_choice

def get_player_name():
    clear_screen()
    print_position(10, 20, logo)
    print_position(2,24,f"{Fore.YELLOW}Welcome brood! your name is? : ")
    player_name = get_input_position(1,27)
    print()
    clear_screen()
    return player_name