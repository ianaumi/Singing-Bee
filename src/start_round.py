import utils as util
import displays as display
from song_selection import song_list,year_choice,song_choice

def song_info(value):
    return song_list[year_choice[0]][song_choice[0]][value]

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
            util.play_sound(song_info("sound"))
            display.print_position(3,27,"press enter to continue")
            util.get_input_position(1, 27)
            util.stop_sound()
            player_skipped_song = True
            display.clear_screen()
            continue

        #FIXME alignment
        if player_used_hint :
            display.print_position(2    ,0,song_info("hint").center(80))
        else:
            display.print_position(2,0,song_info("choices").center(80))

        player_choice = util.get_input_position(2, 30)

        # input validation
        #FIXME add UI
        if player_choice.upper() not in util.options(["A", "B", "C", "D", "H"]):
            display.invalid_option(0,30)
            continue

        # checks if the player already used hint
        if player_choice.upper() == 'H':
            if player_hints <= 0:
                display.hint_text_info("You dont have enough hints")
                continue
            if player_used_hint:
                display.hint_text_info("You already used hint")
                continue
            # checks hint count and if player wants to use hint
            if not player_used_hint and player_hints > 0:
                player_hints = player_hints - 1
                player_used_hint = True
                display.hint_text_info("You used hint")
                continue

        # checks if user will enter an input aside from printed hint
        if player_used_hint:
            if player_choice.upper() not in song_info("hint"):
                display.invalid_option(0,30)
                continue

        # answer checker
        if player_choice.upper() != song_info("answer"):
            display.answer_result("Wrong answer.",0)

        elif player_used_hint and player_choice.upper() == song_info("answer"):
            display.answer_result("Correct answer!",500)
            player_points = player_points + 500

        else:
            display.answer_result("Correct answer!",1000)
            player_points = player_points + 1000

        player_used_hint = False
        player_skipped_song = False

        # removes the last played song
        song_choice.pop(0)
        year_choice.pop(0)
        display.clear_screen()

        # checks if there's no more song to play
        if util.list_is_empty(song_choice):
            display.total_score(player_name,player_points)
            player_choice = util.ask_play_again(player_name)
            #FIXME
            if player_choice == True:
                break