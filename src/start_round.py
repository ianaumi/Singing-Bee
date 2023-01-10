import utils as util
import displays as display




def song_info(year_choice, song_choice, value):
    songList = util.get_song_list_file()
    return songList[year_choice[0]][song_choice[0]][value]


#FIXME parameter name


def play_again(player_choice):
    while True:
        player_choice = input("Do you want to play again? Y/N : ")
        if player_choice.upper() in util.options(["Y", "N"]):
            if player_choice.upper() == "Y":
                return

            elif player_choice.upper() == "N":
                return display.quit_screen(player_name)
        else:
            print("Invalid Option")


def is_empty(empty):
    if not empty:
        return True
    else:
        return False


def round_start():
    global player_points
    global hints
    global player_choice
    global player_name
    global year_choice
    global song_choice
    while True:
        hints = 3

        print(song_choice[0])
        print(song_info(year_choice[0], song_choice[0], "lyrics"))
        print(song_info(year_choice[0], song_choice[0], "choice"))

        print("Total hints available: ", hints)
        while True:
            player_choice = input("What is your choice: ")
            if player_choice.upper() in util.options(["A", "B", "C", "D", "H"]):
                hint_used = False

                if player_choice.upper() == "H":
                    if hints > 0:
                        if not hint_used:
                            print(song_info(year_choice[0], song_choice[0], "hint"))
                            hint_used = True
                            hints = hints - 1
                            while True:
                                player_choice = input("What is your choice: ")
                                if player_choice.upper() in song_info(year_choice[0], song_choice[0], "hint"):
                                    break
                                else:
                                    print("Invalid Option")

                if player_choice.upper() == (song_info(year_choice[0], song_choice[0], "answer")):
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

        if is_empty(year_choice):

            play_again(player_choice)