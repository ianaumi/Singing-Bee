import utilities as util
import  displays as display
from displays import clear_screen,header_text,logo
import  sounds
'''game_menu is where player can know more about the game 
such as: about the game, the instructions. This is where also the
player can proceed to the main game.
'''


def run_game_menu(player_name):
    while True:
        clear_screen()
        header_text(f"# WELCOME TO SINGING BEE {player_name}!")
        display.print_position(3, 20, logo)
        display.game_menu_options()
        player_choice = util.get_input_position(1,31,">>")

        if player_choice.upper() in ["P", "A", "H", "Q"]:
            if player_choice.upper() == "A":
                sounds.play_sound("sounds\\Game sounds\\select_sound.wav")
                clear_screen()
                display.about_game_screen()

            elif player_choice.upper() == "H":
                sounds.play_sound("sounds\\Game sounds\\select_sound.wav")
                clear_screen()
                display.help_screen()

            elif player_choice.upper() == "Q":
                sounds.play_sound("sounds\\Game sounds\\select_sound.wav")
                sounds.stop_sound()
                clear_screen()
                display.quit_screen(player_name)


            elif player_choice.upper() == "P":
                sounds.play_sound("sounds\\Game sounds\\select_sound.wav")
                clear_screen()
                display.loading_screen()
                break
        else:
            display.invalid_option(0,30)