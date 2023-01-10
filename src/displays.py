import time
import colorama
from os import system
from rich.console import Console
from rich.markdown import Markdown
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

warning = "# WARNING!"
copyright = "# COPYRIGHT DISCLAMER NOTICE !"
logo = """                                   
                    _____ _         _            _           
                   |   __|_|___ ___|_|___ ___   | |_ ___ ___ 
                   |__   | |   | . | |   | . |  | . | -_| -_|
                   |_____|_|_|_|_  |_|_|_|_  |  |___|___|___|
                               |___|     |___|               
"""
about_header = "# ABOUT THE GAME"
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