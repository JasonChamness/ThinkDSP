import sys
sys.path.insert(0, '..')
import thinkdsp
from matplotlib import pyplot

print("\nExercise 1-3")

A440 = thinkdsp.SinSignal(freq=440) + thinkdsp.CosSignal(freq=440)
WaveA440 = A440.make_wave()
WaveA440.normalize()

print("Playing combined sin and cos 440 Hz wave...")
WaveA440.write('temp_1_3.wav')
thinkdsp.play_wave('temp_1_3.wav', player='afplay')

print("Plotting combined sin and cos 440 Hz spectrum")
spectrum = WaveA440.make_spectrum()
spectrum.plot()
pyplot.show()

print("Exercise 1-3 complete\n")