import sys
sys.path.insert(0, '..')
import thinkdsp
from matplotlib import pyplot

chapter = 2
exercise = 3

print("\nExercise ",chapter,"-",exercise)

square = thinkdsp.SquareSignal(freq=1100)
wave = square.make_wave(framerate=10000)
spectrum = wave.make_spectrum()

print("Plotting aliased square wave")
spectrum.plot()
pyplot.title('Aliased Square Wave')
pyplot.xlabel('Freq (Hz)')
pyplot.show()

print("Playing aliased square wave...")
wave.write('temp_2_3.wav')
thinkdsp.play_wave('temp_2_3.wav', 'afplay')

print("Exercise ",chapter,"-",exercise," complete\n")