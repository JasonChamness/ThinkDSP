import sys
sys.path.insert(0, '..')
import thinkdsp
from matplotlib import pyplot

chapter = 2
exercise = 2

print("\nExercise ",chapter,"-",exercise)

import math
import numpy as np

class SawtoothSignal(thinkdsp.Sinusoid):
    def evaluate(self, ts):
        cycles = self.freq * ts + self.offset / thinkdsp.PI2
        frac, _ = np.modf(cycles)
        ys = thinkdsp.normalize(thinkdsp.unbias(frac), self.amp)
        return ys

print("Plotting 440 Hz sawtooth signal")
saw = SawtoothSignal()
saw.plot()
pyplot.title('440 Hz Sawtooth')
pyplot.xlabel('Time (s)')
pyplot.show()

wave = saw.make_wave()
spectrum = wave.make_spectrum()

print("Plotting 440 Hz sawtooth spectrum")
spectrum.plot()
pyplot.title('440 Hz Sawtooth Spectrum')
pyplot.xlabel('Freq (Hz)')
pyplot.show()

print("Exercise ",chapter,"-",exercise," complete\n")