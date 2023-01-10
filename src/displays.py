from os import system
from rich.console import Console
from rich.markdown import Markdown
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

warning = "# WARNING!"
copyright = "# COPYRIGHT DISCLAMER NOTICE !"
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


def advice_screen():
    clear_screen()
    md = Markdown(warning)
    console.print(md)
    print_position(10,10,f"{Fore.YELLOW}We advise to lower your volume to prevent any ear injuries.")
    press_any_key()


def copyright_disclaimer_screen():
    clear_screen()
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
