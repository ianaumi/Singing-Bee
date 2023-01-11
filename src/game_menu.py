import utils as util
import  displays as display
from displays import print_position,clear_screen,header_text

def run_game_menu(player_name):
    while True:
        clear_screen()
        header_text(f"# WELCOME TO SINGING BEE {player_name}!")
        display.game_menu_options()
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
                display.loading_screen()
                break
        else:
            display.invalid_option(0,30)