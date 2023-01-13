import utilities as util
import displays as display
from song_selection import song_list, year_choice, song_choice
import sounds
'''
start_round file is for the main game.
it contains of printing the lyrics , the sound, etc. related to the game.
it's the core of the game where player can finally guess the blank lines.
'''


# gets the value from the key of a song
def song_info(value):
    return song_list[year_choice[0]][song_choice[0]][value]


def run_start_round(player_name):
    # always resets the scores and hints every start round
    player_points = 0
    player_hint_count = 3
    player_skipped_song = False
    player_used_hint = False

    while True:

        # displays the header of start round contains the number of remaining songs
        display.header_text(f"# Song playing - {song_choice[0]}\n\n ## Remaining songs: {len(song_choice)}")
        display.player_status(player_name, player_hint_count, player_points)

        # prints out the lyrics of a song
        display.print_position(2, 0, song_info("lyrics"))

        # checks if user already skipped a song
        if not player_skipped_song:
            sounds.play_background(song_info("sound"), 0)

            # lets the user skip the sound
            display.press_any_key()

            # stops the sound
            sounds.stop_sound()

            # plays the background music while player is choosing answer
            sounds.play_background("sounds/game_sounds\\waiting_choice_sound.wav", -1)
            player_skipped_song = True
            display.clear_screen()
            continue

        # checks if player used a hint
        if player_used_hint:
            display.print_position(2, 0, song_info("hint").center(75))
        else:
            display.print_position(2, 0, song_info("choices").center(80))

        player_choice = util.get_input_position(2, 37, "")
        # input validation
        if player_choice.upper() not in ['A', 'B', 'C', 'D', 'H']:
            display.invalid_option(0, 30)
            continue

        # checks if the player already used hint
        if player_choice.upper() == 'H':

            # checks if player already used a hint
            if player_used_hint:
                sounds.play_sound("sounds/game_sounds\\invalid_sound.wav")
                display.hint_text_info("You already used hint")
                continue

            # checks if player has enough hint
            if player_hint_count <= 0:
                sounds.play_sound("sounds/game_sounds\\invalid_sound.wav")
                display.hint_text_info("You dont have enough hints")
                continue

            # checks player wants to use hint and has enough hint count
            if player_hint_count > 0:
                sounds.play_sound("sounds/game_sounds\\used_hint_sound.wav")
                player_hint_count = player_hint_count - 1
                player_used_hint = True
                display.hint_text_info("You used hint")
                continue

        # checks if user will enter an input aside from printed hint
        if player_used_hint:

            # checks if input is not in the hint choices
            if player_choice.upper() not in song_info("hint"):
                sounds.play_sound("sounds/game_sounds\\invalid_sound.wav")
                display.invalid_option(0, 30)
                continue

        # >>>>>>>>> answer checker <<<<<<<<<<<<<<<<<
        # checks if it's the wrong answer
        if player_choice.upper() != song_info("answer"):
            sounds.play_sound("sounds/game_sounds\\wrong_answer_sound.wav")
            display.answer_result("Wrong answer.", 0)

        # checks if it's a correct answer and player used hint
        elif player_used_hint and player_choice.upper() == song_info("answer"):
            sounds.play_sound("sounds/game_sounds\\correct_with_hint_sound.wav")
            display.answer_result("Correct answer!", 500)
            player_points = player_points + 500

        # checks if it's a correct answer and player didn't use hint
        else:
            sounds.play_sound("sounds/game_sounds\\correct_answer_sound.wav")
            display.answer_result("Correct answer!", 1000)
            player_points = player_points + 1000

        # reset
        sounds.stop_sound()
        player_used_hint = False
        player_skipped_song = False

        # removes the last played song
        song_choice.pop(0)
        year_choice.pop(0)
        display.clear_screen()

        # checks if there's no more song to play
        if util.list_is_empty(song_choice):

            # displays the total number of score player has
            display.total_score(player_name, player_points)

            # asks the user if they want to play again that returns a boolean
            player_choice = util.ask_play_again(player_name)

            # if player choice is true, it will go back to game menu
            if player_choice:
                break
