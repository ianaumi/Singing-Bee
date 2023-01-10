import displays as display
import utils as util


def song_selection(year_choice, song_choice, choice):
    while True:
        # >>>>>>>>>>>>YEAR SELECT<<<<<<<<<<<
        # clears the key choices from songs
        song_list = util.get_song_list_file()
        choice.clear()
        display.clear_screen()
        display.category_header("YEAR", song_choice)
        display.select_year_from(song_list, choice)

        # checks if player is done choosing
        player_choice = util.get_input_position(2, 12)
        if player_choice.upper() == 'D':
            display.clear_screen()
            display.player_chosen_songs(song_choice)

            player_choice = util.get_input_position(1, 24)

            if player_choice.upper() == 'B':
                display.clear_screen()
                continue

            else:
                year_choice.reverse()
                song_choice.reverse()
                display.clear_screen()
                break

        if player_choice in choice:
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
        display.category_header(f"SONGS FROM {year_choice[0]}", song_choice)
        display.select_song_from(song_list, year_choice[0], choice)

        player_choice = util.get_input_position(2, 12)
        if player_choice.upper() == 'B':
            year_choice.pop()
            display.clear_screen()
            continue

        if player_choice in choice:
            if choice[player_choice] in song_choice:
                display.print_position(0, 11, "You already chose that song")
                display.sleep(1)
                continue

            else:
                # inserts the song choice of user from the song category
                song_choice.insert(0, choice[player_choice])
                continue
        else:
            display.invalid_option(0, 11)
            year_choice.pop()
            continue
