import time
import colorama
from main import player_name
from os import system
from rich.console import Console
from rich.markdown import Markdown
from colorama import Fore, Back, Style

def colorama_set_auto_style():
    colorama.init(autoreset=True)

logo = """                                   
                    _____ _         _            _           
                   |   __|_|___ ___|_|___ ___   | |_ ___ ___ 
                   |__   | |   | . | |   | . |  | . | -_| -_|
                   |_____|_|_|_|_  |_|_|_|_  |  |___|___|___|
                               |___|     |___|               
"""
warning = "# WARNING!"
copyright = "# COPYRIGHT DISCLAMER NOTICE !"
about_header = "# ABOUT THE GAME"
help_header = "# INSTRUCTIONS"
game_menu_header = f"# WELCOME TO SINGING BEE {player_name} !"
song_header = f"# SELECT A SONG FROM {year_choice[0]} \n## SONG CART:{len(song_choice)}"
year_header = f"# SELECT YEAR \n\n## SONG CART:{len(song_choice)}"
your_songs_header = f"# YOUR SONG LIST \n## Total songs:{len(song_choice)}"
console = Console()

def set_screen_size(column,line):
    system(f'mode con: cols={column} lines={line}')

def clear_screen():
    system('cls')


def press_any_key():
    print_position(2, 24, f"{Style.BRIGHT}{Fore.YELLOW} Press any key to continue")
    print("\n", " " * 37, end="")
    input()


def print_position(line,column,text):
    print("\n" * line," " * column, text)


def invalid_option_screen(line, column):
    clear_screen()
    print_position(line, column, "Invalid Option")
    time.sleep(1)


# >>>>>>>>>>> GAME INTRO SECTION <<<<<<<<<<<<<<<<<<<<<
def loading_screen():
    count = 0
    while count < 4:
        clear_screen()
        print_position(10, 20, logo)
        print("\n", " " * 30, f"{Fore.YELLOW}Loading", "." * count)
        time.sleep(1)
        count += 1
    clear_screen()


def advice_screen():
    md = Markdown(warning)
    console.print(md)
    print_position(10,10,f"{Fore.YELLOW}We advise to lower your volume to prevent any ear injuries.")
    press_any_key()
    clear_screen()


def copyright_disclaimer_screen():
    md = Markdown(copyright)
    console.print(md)
    print_position(5, 3, f"""{Fore.YELLOW}We do not claim the ownership of all of the music/soundsyou will hear.
        All material is the copyright property of its respective owner(s).\n
                     Under Section 107 of the Copyright Act 1976,
         allowance is made for “fair use” for purposes such as criticism, 
          comment, news reporting, teaching, scholarship, and research.\n
                  Fair use is a use permitted by copyright statute 
                        that might otherwise be infringing.\n
                       Non-profit, educational or personal use 
                      tips the balance in favour of fair use.\n
                       WE DO NOT OWN THE RIGHTS OF ANY SONG. 
                     No Copyright infringement intended here.{Fore.WHITE}
    """)
    press_any_key()
    clear_screen()

# >>>>>>>>>>>>>>>>>>>>> GAME MENU SECTION <<<<<<<<<<<<<<<<<<<<<<<<<<<
def game_menu_header():
    game_menu_header = f"# WELCOME TO SINGING BEE {player_name} !"
    md = Markdown(game_menu_header)
    console.print(md)

def about_game_screen():
    md = Markdown(about_header)
    console.print(md)
    print_position(3, 30, f"""
                      {Fore.YELLOW}Singing Bee is a console game that 
                tests your knowledge of the most iconic songs.
                   Fill in the missing lyrics and sing along
          to your most treasured tunes from the 1960s up to the 2020s!\n\n

              Singing Beewas based on a Philippine TV show called 
                "The Singing Bee". We combined this TV show with 
               "Who Wants to be a Millionaire". Both concepts of
                    the said shows results to this game.\n\n

                          Bees communicate by dancing!{Fore.WHITE}  
    """)
    press_any_key()
    clear_screen()

def help_screen():
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
    press_any_key()
    clear_screen()

def quit_screen():
    print_position(15,29,f"""Goodbye, {Fore.YELLOW}{player_name}{Fore.WHITE}.\n
        No matter where you are, the hive will be always a home for you.\n
                              Sing-you soon!
    """)
    time.sleep(5)
    clear_screen()
    exit()


# >>>>>>>>>>>>>>>>>> SONG SELECTION <<<<<<<<<<<<<<<<<<<<<
def song_header():
    md = Markdown(song_header)
    console.print(md)

def year_header():
    md = Markdown(year_header)
    console.print(md)

def your_song_list():
    md = Markdown(your_songs_header)
    console.print(md)

def display_list(item):
    for num, key in enumerate(item, start=1):
        choice[str(num)] = key

    for n, items in choice.items():
        print_position(1,13,f"[{Fore.YELLOW}{n}{Fore.WHITE}] {items}")