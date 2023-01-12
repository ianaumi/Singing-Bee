from time import sleep
from os import system
from rich.console import Console
from rich.markdown import Markdown
import colorama
from colorama import Fore, Style


colorama.init(autoreset=True)

logo = """                                   
                    _____ _         _            _           
                   |   __|_|___ ___|_|___ ___   | |_ ___ ___ 
                   |__   | |   | . | |   | . |  | . | -_| -_|
                   |_____|_|_|_|_  |_|_|_|_  |  |___|___|___|
                               |___|     |___|               
"""
console = Console()

def header_text(text):
    md = Markdown(text)
    console.print(md)

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


def invalid_option(line, column):
    print_position(line, column, "Invalid Option")
    sleep(1)
    clear_screen()


# >>>>>>>>>>> GAME INTRO SECTION <<<<<<<<<<<<<<<<<<<<<
def loading_screen():
    global logo
    count = 0
    while count < 4:
        clear_screen()
        print_position(10, 20, logo)
        print("\n", " " * 30, f"{Fore.YELLOW}Loading", "." * count)
        sleep(1)
        count += 1
    clear_screen()


def advice_screen():
    header_text("# WARNING!")
    print_position(10,10,f"{Fore.YELLOW}We advise to lower your volume to prevent any ear injuries.")
    press_any_key()
    clear_screen()

def copyright_disclaimer_screen():
    header_text("# COPYRIGHT DISCLAIMER NOTICE !")
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

# >>>>>>>>>>>>>>>>>>>>> END OF GAME INTRO SECTION <<<<<<<<<<<<<<<<<<<


# >>>>>>>>>>>>>>>>>>>>> GAME MENU SECTION <<<<<<<<<<<<<<<<<<<<<<<<<<<
def game_menu_header(player_name):
    header_text(f"# WELCOME TO SINGING BEE {player_name} !")

def game_menu_options():
    print_position(3, 32, f"{Fore.YELLOW}[P] Play")
    print_position(1, 32, f"{Fore.YELLOW}[A] About")
    print_position(1, 32, f"{Fore.YELLOW}[H] Help")
    print_position(1, 32, f"{Fore.YELLOW}[Q] Quit\n")

def about_game_screen():
    header_text("# ABOUT THE GAME")
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
    header_text("# INSTRUCTIONS")
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

def quit_screen(player_name):
    clear_screen()
    #FIXME CENTRALIZE ALIGNMENT
    print_position(15,30,f"""Goodbye, {Fore.YELLOW}{player_name}{Fore.WHITE}.\n
        No matter where you are, the hive will be always a home for you.\n
                              Sing-you soon!
    """)
    sleep(5)
    clear_screen()
    exit()

# >>>>>>>>>>>>>>>>>>>> END OF GAME MENU SECTION <<<<<<<<<<<<<<





# >>>>>>>>>>>>>>>>>> SONG SELECTION <<<<<<<<<<<<<<<<<<<<<

def choice_list(item, choice):
    for num, key in enumerate(item, start=1):
        choice[str(num)] = key

    for n, items in choice.items():
        print_position(1,13,f"[{Fore.YELLOW}{n}{Fore.WHITE}] {items}")
def category_header(text,song_choice):
    header_text(f"# {text} \n\n## SONG CART:{len(song_choice)}")
    print("\n" * 2)


def select_year_from(year_list, choice):
    choice_list(year_list, choice)
    print_position(1, 13, f"[{Fore.YELLOW}D{Fore.WHITE}] Done")


def select_song_from(song_list, year_choice, choice):
    choice_list(song_list[year_choice], choice)
    print_position(1, 13, f"[{Fore.YELLOW}B{Fore.WHITE}] Back")


def player_chosen_songs(song_choice):
    header_text(f"# YOUR SONG LIST \n## Total songs:{len(song_choice)}")
    print("\n" * 2)
    for num, song in enumerate(song_choice, start=1):
        print_position(1, 14, f"{Fore.YELLOW}{num}{Fore.WHITE}. {song}")
    print_position(4, 32, f"[{Fore.YELLOW}B{Fore.WHITE}] Back")
    print_position(1, 25, f"{Fore.YELLOW}Press any key to start")

# >>>>>>>>>>>>>>>>>>>>>>> END OF SONG SELECTION <<<<<<<<<<<<<<<<<




# >>>>>>>>>>>>>>>>>>>>>>>>> START OF ROUND <<<<<<<<<<<<<<<<<<<<<<
def player_status(player_name,player_hints,player_points):
    print_position(0,5,f"""{Fore.YELLOW}_|___|_    
       ({Style.BRIGHT}{Fore.RED}●{Fore.WHITE}'◡'{Style.BRIGHT}{Fore.RED}●{Style.NORMAL}{Fore.YELLOW})/{Fore.WHITE}Status""")
    print_position(0,5,("+" + "-" * 18 + "+"))
    print_position(0, 5,("|" + (" " * 18) + "|"))
    print_position(0, 5, "| " + (f"Player:{Style.NORMAL}{Fore.YELLOW}"+str(f"{player_name}{Fore.WHITE}").ljust(15)) + "|")
    print_position(0, 5, "| " + (f"Hints:{Style.NORMAL}{Fore.YELLOW}"+str(f"{player_hints}{Fore.WHITE}").ljust(16)   ) + "|")
    print_position(0, 5, "| " + (f"Points:{Style.NORMAL}{Fore.YELLOW}" + str(f"{player_points}{Fore.WHITE}").ljust(14)) + " |")
    print_position(0, 5,("|" + (" " * 18) + "|"))
    print_position(0,5,("+" + "-" * 18 + "+"))

def total_score(player_name,player_points):
    clear_screen()
    print_position(15,30,f"CONGRATS, {Fore.YELLOW}{player_name}{Fore.WHITE}!\n\n" + " " * 23 + f"You managed to get {Fore.YELLOW}{player_points}{Fore.WHITE} Honeys!\n\n")

def answer_result(text,points):
    print_position(0, 27, text)
    print_position(0, 27, f"+ {points} Honey")
    sleep(2)
    clear_screen()

def hint_text_info(text):
    print_position(0, 27, text)
    sleep(1)
    clear_screen()


# >>>>>>>>>>>>>>>>>>>>>>>>> END OF ROUND <<<<<<<<<<<<<<<<<<<<<<<<