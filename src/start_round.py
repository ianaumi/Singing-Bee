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
        if player_used_hint :
            display.print_position(3, 35, song_info("hint"))
        else:
            display.print_position(2, 15, song_info("choices"))

        player_choice = util.get_input_position(3, 27)

        # input validation
        if player_choice.upper() in util.options(["A", "B", "C", "D", "H"]):

            # checks if the player already used hint
            if player_choice.upper() == 'H':

                if player_used_hint:
                    print("you already used hint")
                    continue

                # checks hint count and if player wants to use hint
                if not player_used_hint and player_hints > 0:
                    player_hints = player_hints - 1
                    player_used_hint = True
                    continue

                else:
                    print("you don't have enough hints")
                    continue

            # checks if user will enter an input aside from printed hint
            if player_used_hint:
                if player_choice.upper() not in song_info("hint"):
                    print("invalid option")
                    continue

            # answer checker
            elif player_choice.upper() == song_info("answer") :
                if player_used_hint:
                    player_points = player_points + 500
                    continue

                else:
                    player_points = player_points + 1000
            else:
                print("wrong answer")
        else:
            display.invalid_option(0,0)
            continue

        player_used_hint = False
        player_skipped_song = False

        # removes the last played song
        song_choice.pop(0)
        year_choice.pop(0)

        # checks if there's no more song to play
        if util.list_is_empty(song_choice):
            display.total_score(player_name,player_points)
            player_choice = ask_play_again(player_name)
            #FIXME
            if player_choice == True:
                break
