import json
import time
import colorama
from colorama import Fore, Back, Style
from os import system
from pygame import mixer
from rich.console import Console
from rich.markdown import Markdown
colorama.init(autoreset=True)


year_choice = []  # stores the year choice of player
song_choice = []  # stores the song choice of player
choice = {}  # stores the keys player can press and use it to call the key from the song list json file
player_name = None  # stores the player's name
player_choice = None  # stores the every action of the player.
player_points = 0  # stores the points of the user once the round started
hints = 3
console = Console()
warning = "# WARNING!"
copyright = "# COPYRIGHT DISCLAMER NOTICE !"
logo = """                                   
                    _____ _         _            _           
                   |   __|_|___ ___|_|___ ___   | |_ ___ ___ 
                   |__   | |   | . | |   | . |  | . | -_| -_|
                   |_____|_|_|_|_  |_|_|_|_  |  |___|___|___|
                               |___|     |___|               
"""
game_menu_header = f"# WELCOME TO SINGING BEE {player_name} !"
about_header = "# ABOUT THE GAME"
help_header = "# INSTRUCTIONS"

# sets the size of the window of  terminal 100x40
system('mode con: cols=80 lines=40')

# reading from the song list json file
with open('songList.json') as f:
    song_list = json.load(f)

# plays the sound from the dictionary
def play_sound(path):
    mixer.music.load(path)
    mixer.music.play()


def clear_screen():
    system('cls')


# input validator for some options
def options(keys):
    option = keys
    return option


def print_position(line,column,text):
    print("\n" * line," " * column, text)

def display_press_any_key():
    print_position(2,24,f"{Style.BRIGHT}{Fore.YELLOW} Press any key to continue")
    print("\n", " " * 37, end="")
    input()

def display_advice():
    clear_screen()
    md = Markdown(warning)
    console.print(md)
    print_position(10,10,f"{Fore.YELLOW}We advise to lower your volume to prevent any ear injuries.")
    display_press_any_key()

def display_copyright_disclamer():
    clear_screen()
    md = Markdown(copyright)
    console.print(md)
    print_position(5, 3, f"""We do not claim the {Fore.YELLOW}ownership{Fore.WHITE} of all of the {Fore.YELLOW}music/sounds{Fore.WHITE} you will hear.
        All material is the copyright property of its respective owner(s).\n
                     Under Section {Fore.YELLOW}107{Fore.WHITE} of the {Fore.YELLOW}Copyright Act 1976{Fore.WHITE},
         allowance is made for {Fore.YELLOW}“fair use”{Fore.WHITE} for purposes such as criticism, 
          comment, news reporting, teaching, scholarship, and research.\n
                  Fair use is a use permitted by {Fore.YELLOW}copyright statute{Fore.WHITE} 
                        that might otherwise be infringing.\n
                       Non-profit, {Fore.YELLOW}educational{Fore.WHITE} or personal use 
                      tips the balance in favour of fair use.\n
        {Fore.YELLOW}               WE DO NOT OWN THE RIGHTS OF ANY SONG. 
                     No Copyright infringement intended here.
    """)
    display_press_any_key()

def get_player_name():
    global player_name
    clear_screen()
    print_position(10, 20, logo)
    print_position(2,24,f"{Fore.YELLOW}Welcome brood! your name is? : ")
    player_choice = get_user_choice_in_position(1,27)
    print()
    return player_name


def display_loading_screen():
    count = 0
    while count < 4:
        clear_screen()
        print_position(10, 20, logo)
        print("\n", " " * 30, f"{Fore.YELLOW}Loading", "." * count)
        time.sleep(1)
        count += 1

def display_welcome_screen():
    # display_loading_screen()
    get_player_name()
    display_advice()
    display_copyright_disclamer()
    clear_screen()


def get_user_choice_in_position(line, column):
    print("\n"*line, " " * column, end="")
    player_choice = input(f"{Fore.YELLOW}{Style.BRIGHT}>> {Fore.WHITE}")
    return player_choice


def display_game_menu_header():
    game_menu_header = f"# WELCOME TO SINGING BEE {player_name} !"
    md = Markdown(game_menu_header)
    console.print(md)

def display_about():
    md = Markdown(about_header)
    console.print(md)
    print_position(3,30,f"""
                      {Fore.YELLOW}Singing Bee{Fore.WHITE} is a {Fore.YELLOW}console game{Fore.WHITE} that 
                tests your knowledge of the most {Fore.YELLOW}iconic songs{Fore.WHITE}.
                   Fill in the missing lyrics and {Fore.YELLOW}sing along{Fore.WHITE} 
          to your most treasured tunes from the {Fore.YELLOW}1960s{Fore.WHITE} up to the {Fore.YELLOW}2020s{Fore.WHITE}!\n\n
        
              {Fore.YELLOW}Singing Bee{Fore.WHITE} was based on a {Fore.YELLOW}Philippine TV show{Fore.WHITE} called 
                "The Singing Bee". We combined this TV show with 
               "Who Wants to be a Millionaire". Both concepts of
                    the said shows results to this game.\n\n
                    
                        {Fore.YELLOW}  Bees communicate by dancing!{Fore.WHITE}  
    """)
    display_press_any_key()
    clear_screen()


def display_help():
    md = Markdown(help_header)
    console.print(md)
    print_position(3, 0, f""" 
    {Fore.YELLOW}•{Fore.WHITE} You can choose {Fore.YELLOW}any songs{Fore.WHITE} based on the songlist\n
    {Fore.YELLOW}•{Fore.WHITE} You should guess the {Fore.YELLOW}missing word/s{Fore.WHITE} on the lyrics of the song.\n
    {Fore.YELLOW}•{Fore.WHITE} Your choices will be: {Fore.YELLOW}A{Fore.WHITE},{Fore.YELLOW}B{Fore.WHITE},{Fore.YELLOW}C{Fore.WHITE},{Fore.YELLOW}D{Fore.WHITE} and {Fore.YELLOW}H{Fore.WHITE} for a {Fore.YELLOW}hint{Fore.WHITE} that may use in the round.\n
    {Fore.YELLOW}•{Fore.WHITE} Correct answer without hint will be {Fore.YELLOW}1000 honeys{Fore.WHITE}.\n
    {Fore.YELLOW}•{Fore.WHITE} While correct answer using hint will be {Fore.YELLOW}500 honey{Fore.WHITE}.\n
    {Fore.YELLOW}•{Fore.WHITE} And if your answer is wrong with or without hint, you get {Fore.YELLOW}0 honey{Fore.WHITE}.\n
    {Fore.YELLOW}•{Fore.WHITE} Check the song list here -> {Fore.YELLOW}tinyurl.com/DaBeeBook{Fore.WHITE}\n
    {Fore.YELLOW}•{Fore.WHITE} May you gather the most honeys in the game. Enjoy!\n\n

            {Fore.YELLOW}    Bees can fly up to 12 mph. On every foraging trip, 
                a bee will visit 50-100 flowers to collect nectar!{Fore.WHITE}
    """)
    display_press_any_key()


def display_quit_screen():
    print("\n🐝---Goodbye", player_name, "Sing-you soon!---🎙")
    quit()

def game_menu():
    global player_name
    global player_choice
    while True:
        clear_screen()
        display_game_menu_header()
        print_position(3, 32,f"{Fore.YELLOW}[P] Play")
        print_position(1, 32,f"{Fore.YELLOW}[A] About")
        print_position(1, 32,f"{Fore.YELLOW}[H] Help")
        print_position(1, 32,f"{Fore.YELLOW}[Q] Quit\n")
        player_choice = get_user_choice_in_position(1,31)

        if player_choice.upper() in options(["P", "A", "H", "Q"]):
            if player_choice.upper() == "A":
                clear_screen()
                display_about()

            elif player_choice.upper() == "H":
                clear_screen()
                display_help()

            elif player_choice.upper() == "Q":
                clear_screen()
                display_quit_screen()

            elif player_choice.upper() == "P":
                clear_screen()
                break
        else:
            print_position(0,30,"Invalid Option")
            time.sleep(1)


# calls the key from a specific song
def song_info(value):
    return song_list[year_choice[0]][song_choice[0]][value]


# displays the enumeration list of year or song
def display_list(item):
    for num, key in enumerate(item, start=1):
        choice[str(num)] = key

    for n, items in choice.items():
        print(f"[{n}] {items}")


# SONG SELECTION
def song_selection():
    global year_choice
    global song_choice
    global player_choice

    while True:
        clear_screen()
        print("🛒SONG CART: ", str(len(song_choice)), "\n🐝-------")
        print(" == YEAR == ")
        # clears the key choices from songs
        choice.clear()

        # displays the year of the songlist file
        display_list(song_list)
        print("🐝-------\n[D] Done")
        player_choice = input("Select a Year: ")

        # checks if player is done choosing
        if player_choice.upper() == 'D':
            clear_screen()
            print("🐝-------\n== YOUR SONGS ==")

            for song in song_choice:
                print(song)

            # allows player to go back to year category
            print("🐝-------\n[B] Back")
            print("😉Press any key to start the game")
            player_choice = input("Choice:")

            if player_choice.upper() == 'B':
                clear_screen()
                continue
            else:
                year_choice.reverse()
                song_choice.reverse()
                clear_screen()
                break

        if player_choice in choice:
            # inserts the year choice of user from the year category
            year_choice.insert(0, choice[player_choice])
            clear_screen()
        else:
            print("❌Invalid Option❌")
            clear_screen()
            continue

        print("🐝-------\n == SONGS ==")
        # clears the key choices from year
        choice.clear()
        display_list(song_list[year_choice[0]])
        print("🐝-------\n[B] To go back.")

        player_choice = input("🎶Choice>> ")
        if player_choice.upper() == 'B':
            year_choice.pop()
            clear_screen()
            continue

        if player_choice in choice:
            # inserts the song choice of user from the song category
            song_choice.insert(0, choice[player_choice])
            clear_screen()

        else:
            print("❌Invalid Option❌")
            time.sleep(2)
            clear_screen()


def is_empty(empty):
    if not empty:
        return True
    else:
        return False


# TODO
# START OF ROUND
def round_start():
    while True:

        print(song_choice[0])
        print(song_info("lyrics"))
        print(song_info("choices"))

        player_choice = input("What is your choice: ")
        hint_used = False

        if player_choice.upper() == (song_info("answer")):
            print("correct")
            if hint_used:
                int(player_points) + 500
            else:
                int(player_points) + 1000
        elif player_choice.upper() == "H":
            if hints > 0:
                if not hint_used:
                    print(song_info("hint"))
                    hint_used = True
                    int(hints) - 1
        else:
            print("wrong")

        #TODO
        # must add hint checker if user has enough hint before using one
        # Line 212
        # Just need to add a define function for the hint
        # -Zen

        song_choice.pop(0)
        year_choice.pop(0)

        if is_empty(year_choice):
            player_choice = input("Do you want to play again? Y/N")
            if player_choice.upper() == "Y":
                return main()
            elif player_choice.upper() == "N":
                return display_quit_screen()
            else:
                print("Invalid Option")






def main():
    pass
    mixer.init()
    # play_sound("sounds\\Song musics\\2020's\\Fallen - Lola Amour.wav")
    # display_welcome_screen()
    game_menu()
    # player_choice = input("test")
    # print(player_choice)
    # display_welcome_screen()
    # get_player_name()
    # game_menu()

    # while True:
    #     pass
    # game_menu()
    # song_selection()
    # round_start()

if __name__ == "__main__":
    main()
