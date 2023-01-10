import utils as util
import displays as display
from song_selection import song_list,choice,year_choice,song_choice

def song_info(value):
    return song_list[year_choice[0]][song_choice[0]][value]

def ask_play_again(player_name):
    print("[P] Play again")
    print("Press any key to quit!")
    player_choice = input(">>")
    if player_choice.upper() == 'P':
        return True
    else:
        display.quit_screen(player_name)

def player_status(player_name,player_hints,player_points):
    display.print_position(2, 5, f"Player:{player_name}")
    display.print_position(0, 5, f"Hints:{player_hints}")
    display.print_position(0, 5, f"Honeys:{player_points}")

def run_start_round(player_name):
    player_points = 0 # stores the points of the user once the round started
    player_hints = 3
    while True:
        display.header_text(f"# Song playing - {song_choice[0]}")
        player_status(player_name,player_hints,player_points)
        display.print_position(2,10,song_info("lyrics"))
        print(song_info("choices"))

        print("Hints", player_hints)
        while True:
            player_choice = input("What is your choice: ")
            if player_choice.upper() in util.options(["A", "B", "C", "D", "H"]):
                hint_used = False
                #FIXME
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
