import json
from colorama import Fore, Style
from displays import clear_screen,print_position,logo,quit_screen
import sounds
'''
Utilities file is for some utility function needed in other files
'''


# gets the data from the json file
def get_song_list_file():
    with open('song_list.json') as f:
        song_list = json.load(f)
    return song_list


# checks if a certain list is empty
def list_is_empty(chosen_songs):

    # checks if it's not a list
    if not chosen_songs:
        return True
    else:
        return False


# gets the user input on a certain position using line and column
def get_input_position(line, column):

    # moves the cursor in a chosen position
    print("\n"*line, " " * column, end="")

    # prints out the input sign
    player_choice = input(f"{Fore.YELLOW}{Style.BRIGHT}>> {Fore.WHITE}")
    return player_choice


#FIXME LIMIT THE NAME CHARACTERS TO 3 MIN 8 MAX
def get_player_name():
    clear_screen()

    # prints the logo on a certain position
    print_position(10, 20, logo)

    # asks the player's name
    print_position(2,24,f"{Fore.YELLOW}Welcome brood! your name is? : ")
    player_name = get_input_position(1,27)

    # plays select sound after hitting enter
    sounds.play_sound("sounds\\Game sounds\\select_sound.wav")
    clear_screen()
    return player_name


# asks user to play again and returns a boolean
def ask_play_again(player_name):

    print_position(0, 30, f"[{Fore.YELLOW}P{Fore.WHITE}] Play again\n")
    print_position(0, 26, f"{Fore.YELLOW}{Style.BRIGHT}Press any key to quit{Fore.WHITE}")
    player_choice = get_input_position(0, 30)

    # checks if user wants to play again
    if player_choice.upper() == 'P':
        sounds.play_sound("sounds\\Game sounds\\select_sound.wav")
        return True
    else:
        quit_screen(player_name)