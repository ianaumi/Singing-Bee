import json
from colorama import Fore, Style
from displays import clear_screen, print_position, logo, quit_screen, invalid_option
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
def get_input_position(line, column,text):

    # moves the cursor in a chosen position
    print("\n"*line, " " * column, end="")

    # prints out the input sign
    player_choice = input(f"{Fore.YELLOW}{Style.BRIGHT}{text} {Fore.WHITE}")
    return player_choice


def get_player_name():
    while True:
        clear_screen()

        # prints the logo on a certain position
        print_position(10, 20, logo)

        # asks the player's name
        print_position(2, 24, f"{Fore.YELLOW}Welcome brood! your name is?")
        print_position(0, 24, f"{Fore.YELLOW}3-8 name length only please~")
        player_name = get_input_position(1, 27)
        print_position(2,24,f"{Fore.YELLOW}Welcome brood! your name is?")
        print_position(0, 24, f"{Fore.YELLOW}3-8 name length only please ~")
        player_name = get_input_position(1, 27,">>")

        # checks if it's a valid name length
        if len(player_name) > 8 or len(player_name) < 3:
            invalid_option(0, 27)
            continue
        else:
            print_position(0, 26, f"{Fore.YELLOW}nice name!")
            sounds.play_sound("sounds\\Game sounds\\select_sound.wav")
            break
    clear_screen()
    return player_name


# plays select sound after hitting enter


# asks user to play again and returns a boolean
def ask_play_again(player_name):

    print_position(2, 0, f"[{Fore.YELLOW}P{Fore.WHITE}] Play again\n".center(87))
    print_position(0, 0, f"{Fore.YELLOW}{Style.BRIGHT}Press any key to quit{Fore.WHITE}".center(89))
    player_choice = get_input_position(1, 37,"")

    # checks if user wants to play again
    if player_choice.upper() == 'P':
        sounds.play_sound("sounds\\Game sounds\\select_sound.wav")
        return True
    else:
        quit_screen(player_name)
