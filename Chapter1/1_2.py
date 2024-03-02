import sys
sys.path.insert(0, '..')
import thinkdsp
from matplotlib import pyplot

# afplay for Mac
# aplay for Linux (default)

print("\nExercise 1-2")

Gsharp7M9 = thinkdsp.read_wave('80459__everdream__g7m9no5.wav')
print("Playing original G#7M9 wave...")
thinkdsp.play_wave('80459__everdream__g7m9no5.wav', player='afplay')

print("Plotting original spectrum")
spectrum = Gsharp7M9.make_spectrum()
spectrum.plot()
pyplot.show()

print("Plotting low-pass filtered spectrum")
spectrum.low_pass(cutoff=145, factor=0.01)
spectrum.plot()
pyplot.show()

print("Playing filtered G#7M9 wave...")
newG7 = spectrum.make_wave()
newG7.write('temp_1_2.wav')
thinkdsp.play_wave(filename='temp_1_2.wav', player='afplay')

print("Exercise 1-2 complete\n")