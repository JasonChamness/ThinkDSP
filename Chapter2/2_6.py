import sys
sys.path.insert(0, '..')
import thinkdsp
from matplotlib import pyplot

chapter = 2
exercise = 6

print("\nExercise ",chapter,"-",exercise)

def SpectrumModifier(spectrum):
    spectrum.hs[0] = 0
    spectrum.hs[1:] /= spectrum.fs[1:]
    return spectrum

print("Playing sawtooth wave...")
saw = thinkdsp.SawtoothSignal()
wave = saw.make_wave()
spectrum = wave.make_spectrum()
wave.normalize()
wave.write('temp_2_6.wav')
thinkdsp.play_wave('temp_2_6.wav', 'afplay')

print("Plotting modified sawtooth wave")
spectrum = SpectrumModifier(spectrum)
wave = spectrum.make_wave()
wave.plot()
pyplot.show()

print("Playing modified sawtooth wave...")
wave.normalize()
wave.write('temp_2_6.wav')
thinkdsp.play_wave('temp_2_6.wav', 'afplay')

print("Exercise ",chapter,"-",exercise," complete\n")