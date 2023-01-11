import time

import utils as util
import displays as display
from song_selection import song_list,year_choice,song_choice

def song_info(value):
    return song_list[year_choice[0]][song_choice[0]][value]

def ask_play_again(player_name):
    #print total score here
    display.print_position(0,14,"[P] Play again")
    display.print_position(0,10,"Press any key to quit!")
    player_choice = util.get_input_position(0,10)
    if player_choice.upper() == 'P':
        return True
    else:
        display.quit_screen(player_name)

def run_start_round(player_name):
    # >>>>>>>>>>>>>>>>>>>>>TESTING BLOCK <<<<<<<<<<<<<<<<<<<<<
    # while True:
    #     print(song_list["2020s"]["The 1"]["lyrics"])
    #     choice = input()
    #     if choice == 'A':
    #         exit()
    player_points = 0 # stores the points of the user once the round started
    player_hints = 3
    player_skipped_song = False
    player_used_hint = False

    while True:
        display.header_text(f"# Song playing - {song_choice[0]}\n\n ## Remaining songs: {len(song_choice)}")

        display.player_status(player_name,player_hints,player_points)
        # FIXME alignment -> assist w members
        display.print_position(2,0,song_info("lyrics"))


        if not player_skipped_song:
            pass
            # util.play_sound(song_info("sound"))
            # display.print_position(3,27,"press enter to continue")
            # util.get_input_position(1, 27)
            # util.stop_sound()
            # player_skipped_song = True
            # display.clear_screen()
            # continue

        #FIXME alignment
        #FIXME IF CONDITION WETHER TO PRINT CHOICES OR HINT CHOICES
        display.print_position(2,15,song_info("choices"))

        while True:
            #FIXME
            # Fails the readability of the code
            player_choice = util.get_input_position(3,27)
            if player_choice.upper() in util.options(["A", "B", "C", "D", "H"]):
                player_used_hint = False

                if player_choice.upper() == "H":
                    if player_hints > 0:
                        if not player_used_hint:
                            #FIXME CODE FROM THE TOP NOT PRINTING (LYRICS, CHOICES ETC.)
                            display.print_position(3,35,song_info("hint"))
                            player_used_hint = True
                            player_hints = player_hints - 1
                            while True:
                                player_choice = util.get_input_position(0,27)
                                if player_choice.upper() in song_info("hint"):
                                    break
                                else:
                                    display.invalid_option(0,27)

                #FIXME WHERE TO PUT THE ANSWER CHECKINGS
                #>>>>>>>>>> ANSWER CHECKER <<<<<<<<<<<<<<<<<<
                if player_choice.upper() == (song_info("answer")):
                    print("Correct!")

                    #FIXME player used hint is still true after moving on to the next song
                    if player_used_hint:
                        print("You earned 500 honeys!")
                        player_points = player_points + 500
                        display.sleep(2)
                        display.clear_screen()
                        break

                    else:
                        print("You earned 1000 honeys!")
                        player_points = player_points + 1000
                        display.sleep(2)
                        display.clear_screen()
                        break
                else:
                    print("Wrong")
                    print("You earned 0 honeys")
                    display.sleep(2)
                    display.clear_screen()
                    break
            else:
                display.invalid_option(0,27)

        song_choice.pop(0)
        year_choice.pop(0)
        player_skipped_song = False

        if util.list_is_empty(song_choice):
            display.total_score(player_name,player_points)
            player_choice = ask_play_again(player_name)
            if player_choice == True:
                break
