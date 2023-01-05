# Welcome !
# Use this comments as guide to our project
# make sure you're on a development branch!

# modules
import os
import json

# clears the terminal using os command
def clear_screen():
    os.system('cls')

# reading from the song list json file
with open('songList.json') as f:
    song_list = json.load(f)

year_choice = []
song_choice = []
choice = {}
player_name = None
player_choice = None
player_points = 0

def options(list):
    option = list
    return option

# START




# WELCOME SCREEN





# ASK USER NAME






# GAME MENU





# SONG SELECTION
def song_info(value):
    return song_list[year_choice[0]][song_choice[0]][value]


def display_list(song_list):
    # enumerates to the list
    for num, key in enumerate(song_list, start=1):
        choice[str(num)] = key

    # prints the choices with numbering
    for n, items in choice.items():
        print(f"[{n}] {items}")


# SONG SELECTION
def song_selection():
    global year_choice
    global song_choice

    while True:
        print(" == YEAR == ")
        # counts how many player chose
        print("SONG CART: ", str(len(song_choice)), "\n")
        # clears the choices from songs
        choice.clear()
        display_list(song_list)
        print("\nPress [D] if you're done choosing")
        player_choice = input("Select a Year: ")

        # checks if player is done choosing
        if player_choice.upper() == 'D':
            print("==YOUR SONGS==")
            print("Press any key to start the game")

            # prints all of the songs player chose
            for song in song_choice:
                print(song)
            print("[B] Back")

            player_choice = input("Choice: ")

            # allows the player to go back
            if player_choice.upper() == 'B':
                continue
            else:
                song_choice.reverse()
                year_choice.reverse()
                break

        if player_choice in choice:
            # inserts the year choice of user in the year choice list
            year_choice.insert(0, choice[player_choice])
        else:
            print("Invalid")
            continue

        print(" == SONG ==")
        choice.clear() # clears the year choices

        # displays the song list selection
        display_list(song_list[year_choice[0]])
        print("[B] To go back.")

        player_choice = input("choice>> ")

        # checks if user wants to go back on year selection
        if player_choice.upper() == 'B':
            year_choice.pop()
            continue

        if player_choice in choice:
            # inserts the year choice of user in the year choice list
            song_choice.insert(0, choice[player_choice])

        else:
            print("invalid option")

song_selection()


# TOTAL SONGLIST PLAYER CHOSE




# START OF ROUND




# SONGLIST IS EMPTY = GAME OVER




# EXIT HERE

# call main
