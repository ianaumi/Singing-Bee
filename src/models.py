



def get_input_position(line, column):
    print("\n"*line, " " * column, end="")
    player_choice = input(f"{Fore.YELLOW}{Style.BRIGHT}>> {Fore.WHITE}")
    return player_choice

def get_player_name():
    from displays import print_position
    from displays import clear_screen
    from main import player_name
    from main import get_input_position
    clear_screen()
    print_position(10, 20, logo)
    print_position(2,24,f"{Fore.YELLOW}Welcome brood! your name is? : ")
    player_name = get_input_position(1,27)
    print()
    return player_name