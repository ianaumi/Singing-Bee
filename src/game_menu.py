
def start_game_menu():
    from displays import clear_screen
    from displays import game_menu_header
    from displays import about_game_screen
    from displays import help_screen
    from displays import quit_screen
    from displays import print_position
    from displays import invalid_option_screen
    from main import player_choice
    from main import get_input_position
    from main import options
    import colorama
    from colorama import Fore, Back, Style

    while True:
        clear_screen()
        game_menu_header()
        print_position(3, 32,f"{Fore.YELLOW}[P] Play")
        print_position(1, 32,f"{Fore.YELLOW}[A] About")
        print_position(1, 32,f"{Fore.YELLOW}[H] Help")
        print_position(1, 32,f"{Fore.YELLOW}[Q] Quit\n")
        player_choice = get_input_position(1,31)

        if player_choice.upper() in options(["P", "A", "H", "Q"]):
            if player_choice.upper() == "A":
                clear_screen()
                about_game_screen()

            elif player_choice.upper() == "H":
                clear_screen()
                help_screen()

            elif player_choice.upper() == "Q":
                clear_screen()
                quit_screen()

            elif player_choice.upper() == "P":
                clear_screen()
                break
        else:
            invalid_option_screen(0,0)

