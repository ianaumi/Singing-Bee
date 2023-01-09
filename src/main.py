import json
import time
import os
from pygame import mixer

year_choice = []  # stores the year choice of player
song_choice = []  # stores the song choice of player
choice = {}  # stores the keys player can press and use it to call the key from the song list json file
player_name = None  # stores the player's name
player_choice = None  # stores the every action of the player.
player_points = 0  # stores the points of the user once the round started
hints = 3

# reading from the song list json file
with open('songList.json') as f:
    song_list = json.load(f)
# plays the sound from the dictionary
def play_sound(path):
    mixer.music.load(path)
    mixer.music.play()


def clear_screen():
    os.system('cls')


# input validator for some options
def options(keys):
    option = keys
    return option


# TODO
# GAME MENU
def display_about():
    print("\n== ABOUT GAME == ")
    print("🐝----Who Wants To Be A Singing Bee is a console game that tests your knowledge of the most iconic songs🎙️"
        + "\nFill in the missing lyrics and sing along to your most treasured tunes from the 1960s up to the 2020s!🎵")
    input("\n😉Enter any key to go back to the Menu ")


def display_help():
    print("\n== HELP == ")
    print("🎙•••Player can choose any songs based on the songlist."
          + "\n🐝•••Then the player should guess the missing word/s on the lyrics of the song."
          + "\n🎙️•••The choices will be: A,B,C,D and H for a hint that may use in the round."
          + "\n🐝•••Correct answer without hint will be 1000 points."
          + "\n🎙️•••While correct answer using hint will be 500 points"
          + "\n🐝•••And if you answer is wrong with or without hint, you get 0 point."
          + "\n🎙•••May you gather the most points in the game. Enjoy!")
    input("\n😉Enter any key to go back to the Menu")

#FIXME
# #Quit Game
# display_quit()
def display_quit_screen():
    print(player_name, "'s total points is ", player_points)
    print("\n🐝---Goodbye", player_name, "Sing-you soon!---🎙")
    quit()


def display_welcome_screen():
    # TODO
    # WELCOME SCREEN
    print("🐝---Welcome to Who Wants To Be A Singing Bee!---🎙")

    # TODO
    # ASK USER NAME

def game_menu():
    global player_name
    player_name = input("Enter your name: ")

    while True:
        print("\n== GAME MENU == ")
        print("[P]--Play🎙️\n[A]--About🐝\n[H]--Help🤔\n[Q]--Quit👋\n")
        player_choice = input("Choice: ")
        if player_choice.upper() in options(["P", "A", "H", "Q"]):
            if player_choice.upper() == "A":
                display_about()
                clear_screen()

            elif player_choice.upper() == "H":
                clear_screen()
                display_help()

            elif player_choice.upper() == "Q":
                display_quit_screen()
                clear_screen()

            elif player_choice.upper() == "P":
                clear_screen()
                break
        else:
            print("❌Invalid Option❌")
            time.sleep(2)
            clear_screen()


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
            clear_screen()


def is_empty(empty):
    if not empty:
        return True
    else:
        return False


# TODO
# START OF ROUND
def round_start():
    global player_points
    global hints
    global player_choice
    while True:

        print(song_choice[0])
        print(song_info("lyrics"))
        print(song_info("choices"))

        print("Total hints available: ", hints)
        while True:
            player_choice = input("What is your choice: ")
            if player_choice.upper() in options(["A", "B", "C", "D", "H"]):

                hint_used = False

                if player_choice.upper() == "H":
                    if hints > 0:
                        if not hint_used:
                            print(song_info("hint"))
                            hint_used = True
                            hints = hints - 1
                            while True:
                                player_choice = input("What is your choice: ")
                                if player_choice.upper() in options(["A", "B", "C", "D"]):
                                    break
                                else:
                                    print("Invalid Option")

                            break

                if player_choice.upper() == (song_info("answer")):
                    print("correct")

                    if hint_used:
                        player_points = player_points + 500
                        break

                    else:
                        player_points = player_points + 1000
                        break

                else:
                    print("wrong")
                    break

            else:
                print("Invalid Option")
        song_choice.pop(0)
        year_choice.pop(0)

        if is_empty(year_choice):
            player_choice = input("Do you want to play again? Y/N : ")
            if player_choice.upper() == "Y":
                return main()
            elif player_choice.upper() == "N":
                return display_quit_screen()
            else:
                print("Invalid Option")

def main():
    mixer.init()
    game_menu()
    song_selection()
    round_start()

if __name__ == "__main__":
    main()
