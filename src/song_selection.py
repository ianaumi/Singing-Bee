import displays as display
import utilities as util
import sounds
'''song_selection file contains the main aspect of choosing songs from a specific era.
it allows the user to navigate through year list and song list. They can add "n" number of songs
and this file prints the list of all song player chose before proceeding to the start of the round
'''

song_list = util.get_song_list_file()
# stores the year choice of player
year_choice = []
# stores the song choice of player
song_choice = []
# stores the keys player can press and use it to call the key from the song list json file
choice = {}


def run_song_selection():
    while True:
        # >>>>>>>>>>>>YEAR SELECT<<<<<<<<<<<
        # clears the key choices from songs
        choice.clear()
        display.clear_screen()

        # displays the main header for the year selection
        display.category_header("YEAR", song_choice)
        display.select_year_from(song_list, choice)

        # checks if player is done choosing
        player_choice = util.get_input_position(2, 12)
        if player_choice.upper() == 'D':
            sounds.play_sound("sounds\\Game sounds\\select_sound.wav")

            # checks if player didn't chose any songs
            if util.list_is_empty(song_choice):
                sounds.play_sound("sounds\\Game sounds\\invalid_sound.wav")
                display.print_position(0, 11, "Please fill your cart first.")
                display.sleep(1)
                continue

            display.clear_screen()
            # prints all the songs player chose
            display.player_chosen_songs(song_choice)
            player_choice = util.get_input_position(1, 24)
            sounds.play_sound("sounds\\Game sounds\\select_sound.wav")

            # checks if player wants to go back to song selection
            if player_choice.upper() == 'B':
                display.clear_screen()
                continue

            else:
                # reverses the choices so system can play the first song player chose
                year_choice.reverse()
                song_choice.reverse()
                display.clear_screen()
                display.loading_screen()
                break

        # checks if player's choice is valid
        if player_choice in choice:
            sounds.play_sound("sounds\\Game sounds\\select_sound.wav")
            # inserts the year choice of user from the year category
            year_choice.insert(0, choice[player_choice])

        else:
            display.invalid_option(0, 11)
            display.clear_screen()
            continue

        # >>>>>>>>>>SONG SELECT<<<<<<<<<<<
        # clears the key choices from year
        display.clear_screen()
        choice.clear()

        # prints out main header for the song selection
        display.category_header(f"SONGS FROM {year_choice[0]}", song_choice)
        display.select_song_from(song_list, year_choice[0], choice)
        player_choice = util.get_input_position(2, 12)

        # checks if player wants to go back
        if player_choice.upper() == 'B':
            sounds.play_sound("sounds\\Game sounds\\select_sound.wav")

            # removes the last chosen year
            year_choice.pop(0)
            display.clear_screen()
            continue

        # checks if player input is valid
        if player_choice in choice:

            # checks if player chose the song already chose
            if choice[player_choice] in song_choice:
                sounds.play_sound("sounds\\Game sounds\\invalid_sound.wav")
                display.print_position(0, 11, "You already chose that song")
                display.sleep(1)
                continue

            else:
                sounds.play_sound("sounds\\Game sounds\\select_sound.wav")
                # inserts the song choice of user from the song category
                song_choice.insert(0, choice[player_choice])
                continue
        else:
            display.invalid_option(0, 11)
            year_choice.pop(0)
            continue
