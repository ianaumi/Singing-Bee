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
        display_list(songList)



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
            print(song_choice)
        else:
            print("invalid option")


song_selection()


# TOTAL SONGLIST PLAYER CHOSE




# START OF ROUND




# SONGLIST IS EMPTY = GAME OVER




# EXIT HERE

# call main
