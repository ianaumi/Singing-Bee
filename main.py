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
def displayList(list):
    for num, key in enumerate(list, start=1):
        choice[str(num)] = key

    for n, items in choice.items():
        print(f"[{n}] {items}")

print(" == YEAR == ")
displayList(songList)

print(" == SONG ==")
choice.clear()
displayList(songList[year_choice[0]])







# SONG SELECTION






# TOTAL SONGLIST PLAYER CHOSE




# START OF ROUND




# SONGLIST IS EMPTY = GAME OVER




# EXIT HERE
