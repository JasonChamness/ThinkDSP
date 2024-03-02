import sys
sys.path.insert(0, '..')
import thinkdsp
from matplotlib import pyplot

chapter = 1
exercise = 4

print("\nExercise ",chapter,"-",exercise)

def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

Gsharp7M9 = thinkdsp.read_wave('80459__everdream__g7m9no5.wav')

print("Playing original G#7M9 wave...")
Gsharp7M9.write('temp_1_4.wav')
thinkdsp.play_wave('temp_1_4.wav', player='afplay')

stretch(Gsharp7M9, 0.5)

print("Playing G#7M9 wave at 2x speed...")
Gsharp7M9.write('temp_1_4.wav')
thinkdsp.play_wave('temp_1_4.wav', player='afplay')

print("Exercise ",chapter,"-",exercise," complete\n")