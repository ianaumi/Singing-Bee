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
    songList = json.load(f)


year_choice = []
song_choice = ["song1", "song2", "song3"]

year_choice = ["2020's"]
song_choice = []
choice = {}

player_name = None
player_choice = None
player_points = 0

# START
def options(list):
    option = list
    return option





# WELCOME SCREEN


# ASK USER NAME






# GAME MENU






def song_info(value):
    return songList[year_choice[0]][song_choice[0]][value]


def display_list(list):
    for num, key in enumerate(list, start=1):
        choice[str(num)] = key

    for n, items in choice.items():
        print(f"[{n}] {items}")


def remove_last(list):
    return list.pop()



# SONG SELECTION
def song_selection():
    while True:
        print(" == YEAR == ")
        print("SONG CART: ", str(len(song_choice)), "\n")
        choice.clear()
        display_list(songList)
        print("\nPress [D] if you're done choosing")
        player_choice = input("Select a Year: ")

        if player_choice.upper() == 'D':
            print("==YOUR SONGS==")
            print("Press any key to start the game")
            print("[B] Back")

            # prints all of the songs player choise
            for song in song_choice:
                print(song)

            player_choice = input("Choice: ")

            if player_choice.upper() == 'B':
                continue
            else:
                song_choice.reverse()
                year_choice.reverse()
                break

        if player_choice in choice:
            year_choice.insert(0, choice[player_choice])
        else:
            print("Invalid")
            continue

        print(" == SONG ==")
        choice.clear()
        display_list(songList[year_choice[0]])
        print("[B] To go back.")

        player_choice = input("choice>> ")

        if player_choice.upper() == 'B':
            remove_last(year_choice)
            continue

        if player_choice in choice:
            song_choice.insert(0, choice[player_choice])

        else:
            print("invalid option")

song_selection()


# TOTAL SONGLIST PLAYER CHOSE




# START OF ROUND




# SONGLIST IS EMPTY = GAME OVER




# EXIT HERE

# call main
