from time import sleep
from os import system
from rich.console import Console
from rich.markdown import Markdown
import colorama
from colorama import Fore, Style
import sounds
'''displays file is for the User Interface.
It contains all of the needed designs.
'''

# resets the color per new line
colorama.init(autoreset=True)


# the logo of the game
logo = """                                   
                    _____ _         _            _           
                   |   __|_|___ ___|_|___ ___   | |_ ___ ___ 
                   |__   | |   | . | |   | . |  | . | -_| -_|
                   |_____|_|_|_|_  |_|_|_|_  |  |___|___|___|
                               |___|     |___|               
"""

# console from the rich module
console = Console()


# header text that converts markdown and print it in the terminal
def header_text(text):
    md = Markdown(text)
    console.print(md)


# sets the window size of the terminal
def set_screen_size(column, line):
    system(f'mode con: cols={column} lines={line}')


# clears the current output
def clear_screen():
    system('cls')


# player can proceed after pressing any key
def press_any_key():
    print_position(2, 24, f"{Style.BRIGHT}{Fore.YELLOW} Press any key to continue")

    # moves the cursor into the middle
    print("\n", " " * 37, end="")
    input()
    sounds.play_sound("sounds\\Game sounds\\select_sound.wav")


# prints something in a specific location
def print_position(line, column, text):
    print("\n" * line, " " * column, text)


# informs the user that the input was invalid
def invalid_option(line, column):

    # plays the invalid sound
    sounds.play_sound("sounds\\Game sounds\\invalid_sound.wav")
    print_position(line, column, "Invalid Option")
    sleep(1)
    clear_screen()

# >>>>>>>>>>> GAME INTRO SECTION <<<<<<<<<<<<<<<<<<<<<

# created own style of loading text


def loading_screen():
    global logo

    # main animated loading text
    count = 0
    while count < 4:
        clear_screen()
        print_position(10, 20, logo)
        print("\n", " " * 30, f"{Fore.YELLOW}Loading", "." * count)
        sleep(1)
        count += 1
    clear_screen()

# informs the player to lower the volume to avoid accidentally lound sounds


def advice_screen():
    header_text("# WARNING!")
    print_position(10, 10, f"{Fore.YELLOW}We advise to lower your volume to prevent any ear injuries.")
    press_any_key()
    clear_screen()


# informs the user that we do not own any song the game will play
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

# displays the game menu header
def game_menu_header(player_name):
    header_text(f"# WELCOME TO SINGING BEE {player_name} !")


# displays the options of the game menu
def game_menu_options():
    print_position(3, 32, f"{Fore.YELLOW}[P] Play")
    print_position(1, 32, f"{Fore.YELLOW}[A] About")
    print_position(1, 32, f"{Fore.YELLOW}[H] Help")
    print_position(1, 32, f"{Fore.YELLOW}[Q] Quit\n")


# informs the user about the game and it's history
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


# informs the player about how to play the game
def help_screen():
    header_text("# INSTRUCTIONS")

    # { COLOR }   { STYLE }   TEXT
    print_position(3, 0, f""" 
    {Fore.YELLOW}•{Fore.WHITE} You can choose {Fore.YELLOW}any songs{Fore.WHITE} based on the songlist\n
    {Fore.YELLOW}•{Fore.WHITE} Check the song list here -> {Fore.YELLOW}tinyurl.com/DaBeeBook{Fore.WHITE}\n
    {Fore.YELLOW}•{Fore.WHITE} You should guess the {Fore.YELLOW}missing word/s{Fore.WHITE} on the lyrics of the song.\n
    {Fore.YELLOW}•{Fore.WHITE} Your choices will be: {Fore.YELLOW}A{Fore.WHITE},{Fore.YELLOW}B{Fore.WHITE},{Fore.YELLOW}C{Fore.WHITE},{Fore.YELLOW}D{Fore.WHITE} and {Fore.YELLOW}H{Fore.WHITE} for a {Fore.YELLOW}hint{Fore.WHITE} that may use in the round.\n
    {Fore.YELLOW}•{Fore.WHITE} Correct answer without hint will be {Fore.YELLOW}1000 honeys{Fore.WHITE}.\n
    {Fore.YELLOW}•{Fore.WHITE} While correct answer using hint will be {Fore.YELLOW}500 honey{Fore.WHITE}.\n
    {Fore.YELLOW}•{Fore.WHITE} And if your answer is wrong with or without hint, you get {Fore.YELLOW}0 honey{Fore.WHITE}.\n
    {Fore.YELLOW}•{Fore.WHITE} May you gather the most honeys in the game. Enjoy!\n\n

            {Fore.YELLOW}    Bees can fly up to 12 mph. On every foraging trip, 
                a bee will visit 50-100 flowers to collect nectar!{Fore.WHITE}
    """)
    press_any_key()
    clear_screen()


# displays the quit screen with the player name
def quit_screen(player_name):

    # stops the last sound played
    sounds.stop_sound()
    clear_screen()

    # final message for the player
    print_position(15, 30, f"""Goodbye, {Fore.YELLOW}{player_name}{Fore.WHITE}.\n
        No matter where you are, the hive will be always a home for you.\n
                              Sing-you soon!
    """)
    print_position(15,0,f"Goodbye, {Fore.YELLOW}{player_name}{Fore.WHITE}.".center(84))
    print_position(1,0,"No matter where you are, the hive will be always a home for you.".center(82))
    print_position(1,0,"Sing-you soon!".center(72))

    sounds.play_sound("sounds\\Game sounds\\quit_sound.wav")
    sleep(1)
    clear_screen()
    exit()

# >>>>>>>>>>>>>>>>>>>> END OF GAME MENU SECTION <<<<<<<<<<<<<<


# >>>>>>>>>>>>>>>>>> SONG SELECTION <<<<<<<<<<<<<<<<<<<<<

# prints out the year/song list player can choose from
def choice_list(item, choice):

    # enumerates to the list and assign it to the choice dictionary
    for num, key in enumerate(item, start=1):
        choice[str(num)] = key

    # prints out the choices from the choice dictionary
    for n, items in choice.items():
        print_position(1, 13, f"[{Fore.YELLOW}{n}{Fore.WHITE}] {items}")

# header for the year or song


def category_header(text, song_choice):
    header_text(f"# {text} \n\n## SONG CART:{len(song_choice)}")
    print("\n" * 2)


# displays the year choices
def select_year_from(year_list, choice):
    choice_list(year_list, choice)
    print_position(1, 13, f"[{Fore.YELLOW}D{Fore.WHITE}] Done")


# displays the song choices
def select_song_from(song_list, year_choice, choice):
    choice_list(song_list[year_choice], choice)
    print_position(1, 13, f"[{Fore.YELLOW}B{Fore.WHITE}] Back")


# displays out all the song player chose
def player_chosen_songs(song_choice):

    # used the length of the array to access how many song player has
    header_text(f"# YOUR SONG LIST \n## Total songs:{len(song_choice)}")
    print("\n" * 2)

    # prints out the song chosen
    for num, song in enumerate(song_choice, start=1):
        print_position(1, 14, f"{Fore.YELLOW}{num}{Fore.WHITE}. {song}")

    print_position(4, 32, f"[{Fore.YELLOW}B{Fore.WHITE}] Back")
    print_position(1, 25, f"{Fore.YELLOW}Press any key to start")

# >>>>>>>>>>>>>>>>>>>>>>> END OF SONG SELECTION <<<<<<<<<<<<<<<<<


# >>>>>>>>>>>>>>>>>>>>>>>>> START OF ROUND <<<<<<<<<<<<<<<<<<<<<<

# informs the player with the current status of hints and points
def player_status(player_name, player_hints, player_points):
    print_position(0, 5, f"""{Fore.YELLOW}/{Fore.WHITE}Status""")
    print_position(0, 5, ("+" + "-" * 18 + "+"))
    print_position(0, 5, ("|" + (" " * 18) + "|"))
    print_position(0, 5, "| " + (f"Player:{Style.NORMAL}{Fore.YELLOW}"+ str(f"{player_name}{Fore.WHITE}").ljust(15)) + "|")
    print_position(0, 5, "| " + (f"Hints:{Style.NORMAL}{Fore.YELLOW}"+ str(f"{player_hints}{Fore.WHITE}").ljust(16)) + "|")
    print_position(0, 5, "| " + (f"Points:{Style.NORMAL}{Fore.YELLOW}" + str(f"{player_points}{Fore.WHITE}").ljust(14))  + " |")
    print_position(0, 5, ("|" + (" " * 18) + "|"))
    print_position(0, 5, ("+" + "-" * 18 + "+"))


# displays the total score of the player
def total_score(player_name,player_points):
    clear_screen()

    # plays the background music
    sounds.play_background("sounds\\Game sounds\\total_score_sound.wav",-1)
    print_position(15, 30, f"CONGRATS, {Fore.YELLOW}{player_name}{Fore.WHITE}!\n\n" + " " * 23 + f"You managed to get {Fore.YELLOW}{player_points}{Fore.WHITE} Honeys!\n\n")


# prints the result of the answer of the player
def answer_result(text, points):
    print_position(0, 30, text)
    print_position(15,0,f"CONGRATS, {Fore.YELLOW}{player_name}{Fore.WHITE}!".center(85))
    print_position(1,0,f"You managed to get {Fore.YELLOW}{player_points}{Fore.WHITE} Honeys!".center(85))


# prints the result of the answer of the player
def answer_result(text,points):
    print(text.center(80))

    # prints out how many honey did the user got from the answer
    print(f"+ {points} Honey".center(80))
    # print_position(0, 30, f"+ {points} Honey")
    sleep(2)
    clear_screen()


# displays the information about the hint
def hint_text_info(text):
    print(text.center(80))
    sleep(1)
    clear_screen()


# >>>>>>>>>>>>>>>>>>>>>>>>> END OF ROUND <<<<<<<<<<<<<<<<<<<<<<<<
