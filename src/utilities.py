import json
import os
from colorama import Fore, Style
from displays import clear_screen, print_position, logo, quit_screen,  invalid_option, login_option, back_button, success_name, sleep
import sounds

'''
Utilities file is for some utility function needed in other files
'''


# gets the data from the json file
def get_song_list_file():

    # opens the song list json file from the directory
    with open("song_list.json") as f:

        # reads the data from json file and stores it in to the variable
        song_list = json.load(f)

        # returns the data from song list
    return song_list


# checks if player name exists on the file
def info_exist(player_input,file_name):

    # opens the file
    with open(file_name) as f:

        # reads through the file and assign it to the variable
        usernames = f.readlines()

        # iterate to the lines of the file
        for line in usernames:

            # returns true if player input is in the file
            if player_input in line:
                return True
    return False


# checks if a certain list is empty
def list_is_empty(chosen_songs):

    # checks if it's not a list
    if not chosen_songs:
        return True
    else:
        return False


# gets the user input on a certain position using line and column
def get_input_position(line, column, text):

    # moves the cursor in a chosen position
    print("\n"*line, " " * column, end="")

    # prints out the input sign
    player_choice = input(f"{Fore.YELLOW}{Style.BRIGHT}{text} {Fore.WHITE}")
    return player_choice


def get_player_name():
    while True:
        clear_screen()
        print_position(10, 20, logo)
        # asks the player's name
        print_position(2, 24, f"{Fore.YELLOW}Welcome brood! your name is?")
        print_position(0, 24, f"{Fore.YELLOW}3-8 name length only please ~")
        player_name = get_input_position(1, 27, ">>")

        # checks if it's a valid name length
        if len(player_name) > 8 or len(player_name) < 3:
            invalid_option(0, 27)
            continue
        else:
            sounds.play_sound("sounds/game_sounds\\select_sound.wav")
            break
    clear_screen()
    return player_name


# asks user to play again and returns a boolean
def ask_play_again(player_name):

    print_position(2, 0, f"[{Fore.YELLOW}P{Fore.WHITE}] Play again\n".center(87))
    print_position(0, 0, f"{Fore.YELLOW}{Style.BRIGHT}Press any key to quit{Fore.WHITE}".center(89))
    player_choice = get_input_position(1, 37, "")

    # checks if user wants to play again
    if player_choice.upper() == 'P':
        sounds.play_sound("sounds/game_sounds\\select_sound.wav")
        return True
    else:
        quit_screen(player_name)


# asks user to log in
def ask_to_login():
    player_input = None

    while True:
        clear_screen()
        print_position(10, 20, logo)
        login_option()
        choice = get_input_position(1,31,">>")

        # input validation
        if choice not in ['1', '2']:
            invalid_option(0,31)
            continue

        # >>>>>>>>>> log in <<<<<<<<<
        if choice == '1':
            sounds.play_sound("sounds/game_sounds\\select_sound.wav")
            clear_screen()
            print_position(10, 20, logo)
            print_position(1, 25, "Enter your player name")
            back_button()
            player_input = get_input_position(1,31,">>")

            if player_input.upper() == 'B':
                sounds.play_sound("sounds/game_sounds\\select_sound.wav")
                continue

            if info_exist(player_input, "player_info"):
                sounds.play_sound("sounds/game_sounds\\select_sound.wav")
                break
            else:
                print_position(1,25,"player name doesn't exist.")
                sounds.play_sound("sounds/game_sounds\\invalid_sound.wav")
                sleep(1)
                continue

        # >>>>>>>>>> register <<<<<<<<<<
        if choice == '2':
            sounds.play_sound("sounds/game_sounds\\select_sound.wav")
            print_position(10, 20, logo)
            player_input = get_player_name()
            clear_screen()

            if not info_exist(player_input,"player_info"):

                # opens the file player info from the directory
                with open("player_info", 'a') as f:

                    # writes a new line in the file
                    f.write('\n')

                    # writes the player name in the file
                    f.write(player_input)

                    # prints out it's a success registration
                    success_name(player_input)
                continue
            else:
                print_position(15, 27, "you're already registered")
                sounds.play_sound("sounds/game_sounds\\invalid_sound.wav")
                sleep(1)
                continue

    return player_input
