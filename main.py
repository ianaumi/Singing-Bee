import json

# reading from the song list json file
with open('songList.json') as f:
    song_list = json.load(f)

year_choice = []  # stores the year choice of player
song_choice = []  # stores the song choice of player
choice = {}  # stores the keys player can press and use it to call the key from the song list json file
player_name = None  # stores the player's name
player_choice = None  # stores the every action of the player.
# player_points = 0  # stores the points of the user once the round started


# input validator for some options
def options(list):
    option = list
    return option

#TODO
# WELCOME SCREEN
print("Welcome to Who Wants To Be A Singing Bee!")

#TODO
# ASK USER NAME
input("Enter your name: ")

#TODO
# GAME MENU
while True:
    print("\n== MENU == ")
    print("[S] Start\n[A] About\n[H] Help\n[Q] Quit\n")
    player_choice = input("Choice: ")

    match player_choice.upper():
        case "A":
            print("\n== ABOUT GAME == ")
            print("Who Wants To Be A Singing Bee is a console game that tests your knowledge of the most iconic songs. Fill in the missing lyrics and sing along to your most treasured tunes from the 60s up to the 2020s!")
            input("\nEnter any key to go back to the Menu ")

        case "H":
            print("== HELP == ")
            print(" ")
            input("\nEnter any key to go back to the Menu ")

        case "Q":
            print("Goodbye. Come back soon!")
            quit()

        case "S":
            print("== SONG SELECTION == ")




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
        print(" == YEAR == ")
        print("SONG CART: ", str(len(song_choice)), "\n")
        # clears the choices from songs
        choice.clear()

        display_list(song_list)
        print("\n[D] Done")
        player_choice = input("Select a Year: ")

        # checks if player is done choosing
        if player_choice.upper() == 'D':
            print("==YOUR SONGS==")
            print("Press any key to start the game")

            for song in song_choice:
                print(song)

            # allows player to go back to year category
            print("[B] Back")
            player_choice = input("Choice: ")

            if player_choice.upper() == 'B':
                continue
            else:
                song_choice.reverse()
                year_choice.reverse()
                break

        if player_choice in choice:
            # inserts the year choice of user from the year category
            year_choice.insert(0, choice[player_choice])
        else:
            print("Invalid")
            continue

        print(" == SONG ==")
        # displays the song list selection
        display_list(song_list[year_choice[0]])
        print("[B] To go back.")

        player_choice = input("choice>> ")
        if player_choice.upper() == 'B':
            year_choice.pop()
            continue

        if player_choice in choice:
            # inserts the song choice of user from the song category
            song_choice.insert(0, choice[player_choice])

        else:
            print("invalid option")


#TODO
# START OF ROUND



#TODO
# SONGLIST IS EMPTY = GAME OVER




# EXIT HERE


def main():
    pass


if __name__ == "__main__":
    main()
