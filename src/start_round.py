import utils as util
import displays as display
from song_selection import song_list,choice,year_choice,song_choice


def song_info(value):
    return song_list[year_choice[0]][song_choice[0]][value]


#FIXME parameter name


def ask_play_again(player_name):
    print("[P] Play again")
    print("Press any key to quit!")
    player_choice = input(">>")
    if player_choice.upper() == 'P':
        return True
    else:
        display.quit_screen(player_name)

def run_start_round(player_name):

    player_points = 0 # stores the points of the user once the round started
    player_hints = 3
    while True:
        print(song_choice[0])
        print(song_info("lyrics"))
        print(song_info("choices"))

        print("Total hints available: ", player_hints)
        while True:
            player_choice = input("What is your choice: ")
            if player_choice.upper() in util.options(["A", "B", "C", "D", "H"]):
                hint_used = False

                if player_choice.upper() == "H":
                    if player_hints > 0:
                        if not hint_used:
                            print(song_info("hint"))
                            hint_used = True
                            player_hints -= 1
                            while True:
                                player_choice = input("What is your choice: ")
                                if player_choice.upper() in song_info("hint"):
                                    break
                                else:
                                    print("Invalid Option")

                if player_choice.upper() == (song_info("answer")):
                    print("Correct!")

                    if hint_used:
                        print("You earned 500 honeys!")
                        player_points = player_points + 500
                        break
                    else:
                        print("You earned 1000 honeys!")
                        player_points = player_points + 1000
                        break
                else:
                    print("Wrong")
                    print("You earned 0 honeys")
                    break
            else:
                print("Invalid Option")

        song_choice.pop(0)
        year_choice.pop(0)

        if util.list_is_empty(song_choice):
            player_choice = ask_play_again(player_name)
            if player_choice == True:
                break
