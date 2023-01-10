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
    player = player_name
    hints = player_hints
    honey = player_points
    #FIXME
    display.print_position(2, 5, f"| Player: {player:^{20}} |")
    display.print_position(0, 5, f"| Hints: {hints:^{20}} |")
    display.print_position(0, 5, f"| Honeys: {honey:^{20}} |")

def run_start_round(player_name):
    display.loading_screen()
    player_points = 0 # stores the points of the user once the round started
    player_hints = 3
    player_skipped_song = False

    # # >>>>>>>>>>>>>>>>>>>>>TESTING BLOCK <<<<<<<<<<<<<<<<<<<<<
    # while True:
    #     print(song_list["2020s"]["About you - 1975"]["lyrics"])
    #     choice = input()
    #     if choice == 'A':
    #         exit()


    while True:
        display.header_text(f"# Song playing - {song_choice[0]}\n\n ## Remaining songs: {len(song_choice)}")

        #FIXME alignment
        player_status(player_name,player_hints,player_points)
        display.print_position(2,5,song_info("lyrics"))

        if not player_skipped_song:
            util.play_sound(song_info("sound"))
            display.print_position(3,23,"press enter to continue")
            util.get_input_position(1, 23)
            util.stop_sound()
            player_skipped_song = True
            display.clear_screen()
            continue

        #FIXME alignment
        display.print_position(3,0,song_info("choices"))

        while True:
            #FIXME
            # Fails the readability of the code
            player_choice = util.get_input_position(3,15)
            if player_choice.upper() in util.options(["A", "B", "C", "D", "H"]):
                hint_used = False
                if player_choice.upper() == "H":
                    if player_hints > 0:
                        if not hint_used:
                            display.print_position(3,0,song_info("hint"))
                            hint_used = True
                            player_hints -= 1
                            while True:
                                player_choice = util.get_input_position(0,15)
                                if player_choice.upper() in song_info("hint"):
                                    break
                                else:
                                    display.invalid_option(0,15)

                #FIXME
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
        player_skipped_song = False

        if util.list_is_empty(song_choice):
            player_choice = ask_play_again(player_name)
            if player_choice == True:
                break
