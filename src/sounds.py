from pygame import mixer
from playsound import playsound
'''
sounds file is used for playing sounds to the other files
'''

# plays a quick sound that overlaps pygame mixer
def play_sound(path):
    playsound(path)


# plays a background music that can loop or not
def play_background(path, repeat):

    # path for the sound file
    mixer.music.load(path)

    # repeat 0 to not loop repeat -1 to infinite loop
    mixer.music.play(repeat)


# stops the currently playing mixer sound
def stop_sound():
    mixer.music.stop()
