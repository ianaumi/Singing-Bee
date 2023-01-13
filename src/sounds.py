from pydub import AudioSegment
from pydub.playback import play
from pygame import mixer
'''
sounds file is used for playing sounds to the other files
'''

# plays a quick sound that overlaps pygame mixer


def play_sound(path):
    sound = AudioSegment.from_wav(path)
    play(sound)


# plays a background music that can loop or not
def play_background(path, repeat):

    # path for the sound file
    mixer.music.load(path)

    # repeat 0 to not loop repeat -1 to infinite loop
    mixer.music.play(repeat)


# stops the currently playing mixer sound
def stop_sound():
    mixer.music.stop()
