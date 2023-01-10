import  colorama
import utils as util
import  displays as display
from displays import print_position,clear_screen,header_text
from colorama import Fore


def display_menu_options():
    print_position(3, 32, f"{Fore.YELLOW}[P] Play")
    print_position(1, 32, f"{Fore.YELLOW}[A] About")
    print_position(1, 32, f"{Fore.YELLOW}[H] Help")
    print_position(1, 32, f"{Fore.YELLOW}[Q] Quit\n")

def start_game_menu(player_name):
    while True:
        clear_screen()
        header_text(f"# WELCOME TO SINGING BEE {player_name}!")
        display_menu_options()
        player_choice = util.get_input_position(1,31)

        if player_choice.upper() in util.options(["P", "A", "H", "Q"]):
            if player_choice.upper() == "A":
                clear_screen()
                display.about_game_screen()

            elif player_choice.upper() == "H":
                clear_screen()
                display.help_screen()

            elif player_choice.upper() == "Q":
                clear_screen()
                display.quit_screen(player_name)

            elif player_choice.upper() == "P":
                clear_screen()
                break
        else:
            invalid_option_screen(0,11)