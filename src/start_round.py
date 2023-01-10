import utils as util
import displays as display
import songList.json
import main as mains


def song_info(value):
    return util.get_song_list_file[songList.year_choice[0]][songList.song_choice[0]][value]


#FIXME parameter name
def is_empty(empty):
    if not empty:
        return True
    else:
        return False


def round_start():
    global player_points
    global hints
    global player_choice
    while True:

        print(songList.song_choice[0])
        print(song_info("lyrics"))
        print(song_info("choices"))

        print("Total hints available: ", hints)
        while True:
            player_choice = input("What is your choice: ")
            if player_choice.upper() in util.options(["A", "B", "C", "D", "H"]):
                hint_used = False

                if player_choice.upper() == "H":
                    if hints > 0:
                        if not hint_used:
                            print(song_info("hint"))
                            hint_used = True
                            hints = hints - 1
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

        songList.song_choice.pop(0)
        songList.year_choice.pop(0)

        if is_empty(songList.year_choice):
            while True:
                player_choice = input("Do you want to play again? Y/N : ")
                if player_choice.upper() in util.options(["Y", "N"]):
                    if player_choice.upper() == "Y":
                        return mains.main()
                    elif player_choice.upper() == "N":
                        return display.quit_screen()
                else:
                    print("Invalid Option")
