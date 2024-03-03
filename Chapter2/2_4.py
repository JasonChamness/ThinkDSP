import sys
sys.path.insert(0, '..')
import thinkdsp
from matplotlib import pyplot

chapter = 2
exercise = 4

print("\nExercise ",chapter,"-",exercise)

triangle = thinkdsp.TriangleSignal()
wave = triangle.make_wave(duration=.01)

print("Plotting triangle wave")
wave.plot()
pyplot.title('Triangle')
pyplot.xlabel('Time')
pyplot.show()

spectrum = wave.make_spectrum()
print("Spectrum at t=0: ", spectrum.hs[0])
spectrum.hs[0] = 100
print("New spectrum at t=0: ", spectrum.hs[0])
new_wave = spectrum.make_wave()

print("Plotting modified triangle wave")
new_wave.plot()
pyplot.title('Modified Triangle')
pyplot.xlabel('Time')
pyplot.show()

print("Exercise ",chapter,"-",exercise," complete\n")