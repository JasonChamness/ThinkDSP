import sys
sys.path.insert(0, '..')
import thinkdsp
from matplotlib import pyplot

chapter = 2
exercise = 1

print("\nExercise ",chapter,"-",exercise)

print("Plotting 500 Hz sawtooth wave")
signal = thinkdsp.SawtoothSignal(500)
wave = signal.make_wave(duration=1, framerate=10000)
segment = wave.segment(duration=0.005)
segment.plot()
pyplot.title('500 Hz Sawtooth Wave')
pyplot.xlabel('Time (s)')
pyplot.show()

print("Playing 500 Hz sawtooth wave...")
wave.write('temp_2_1.wav')
thinkdsp.play_wave('temp_2_1.wav', 'afplay')

import numpy as np
hs = np.fft.rfft(wave.ys)
n = len(wave.ys)                 # number of samples
d = 1 / wave.framerate           # time between samples
fs = np.fft.rfftfreq(n, d)

print("Plotting magnitude vs. freq of 500 Hz sawtooth wave")
magnitude = np.absolute(hs)
pyplot.plot(fs, magnitude)
pyplot.title('Magnitude vs. Freq of 500 Hz Sawtooth Wave')
pyplot.xlabel('Freq (Hz)')
pyplot.show()

print("Plotting angle vs. freq of 500 Hz sawtooth wave")
angle = np.angle(hs)
pyplot.plot(fs, angle)
pyplot.title('Angle vs. Freq of 500 Hz Sawtooth Wave')
pyplot.xlabel('Freq (Hz)')
pyplot.show()

# shuffling phases and inserting them into the spectrum
import random
random.shuffle(angle)
i = complex(0, 1)
spectrum = wave.make_spectrum()
spectrum.hs = magnitude * np.exp(i * angle)
wave2 = spectrum.make_wave()
wave2.normalize()
segment = wave2.segment(duration=0.005)

print("Plotting shuffled phase of 500 Hz sawtooth wave")
segment.plot()
pyplot.title('Shuffled Phase 500 Hz Sawtooth Wave')
pyplot.xlabel('Freq (Hz)')
pyplot.show()

print("Playing shuffled phase 500 Hz sawtooth wave...")
wave2.write('temp_2_1.wav')
thinkdsp.play_wave('temp_2_1.wav', 'afplay')

print("Exercise ",chapter,"-",exercise," complete\n")