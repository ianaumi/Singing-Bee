from pydub import AudioSegment
from pydub.playback import play
from pygame import mixer

def play_sound(path):
    sound = AudioSegment.from_wav(path)
    play(sound)

def stop_sound():
    mixer.music.stop()

def play_background(path,repeat):
    mixer.music.load(path)
    mixer.music.play(repeat)
