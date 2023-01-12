import json
from colorama import Fore, Style
from displays import clear_screen,print_position,logo,quit_screen
import sounds

def get_song_list_file():
    with open('songList.json') as f:
        song_list = json.load(f)
    return song_list

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


#FIXME LIMIT THE NAME CHARACTERS TO 3 MIN 8 MAX
def get_player_name():
    clear_screen()
    print_position(10, 20, logo)
    print_position(2,24,f"{Fore.YELLOW}Welcome brood! your name is? : ")
    player_name = get_input_position(1,27)
    sounds.play_sound("sounds\\Game sounds\\select_sound.wav")
    clear_screen()
    return player_name

def ask_play_again(player_name):
    # print total score here
    print_position(0, 30, f"[{Fore.YELLOW}P{Fore.WHITE}] Play again\n")
    print_position(0, 26, f"{Fore.YELLOW}{Style.BRIGHT}Press any key to quit{Fore.WHITE}")
    player_choice = get_input_position(0, 30)
    if player_choice.upper() == 'P':
        sounds.play_sound("sounds\\Game sounds\\select_sound.wav")
        return True
    else:
        quit_screen(player_name)