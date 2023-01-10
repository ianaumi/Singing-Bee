from os import system
from rich.console import Console
from rich.markdown import Markdown
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

warning = "# WARNING!"
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