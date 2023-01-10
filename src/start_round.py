

def song_info(value):
    return song_list[year_choice[0]][song_choice[0]][value]

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

        if is_empty(year_choice):
            while True:
                player_choice = input("Do you want to play again? Y/N : ")
                if player_choice.upper() in options(["Y", "N"]):
                    if player_choice.upper() == "Y":
                        return main()
                    elif player_choice.upper() == "N":
                        return display_quit_screen()
                else:
                    print("Invalid Option")