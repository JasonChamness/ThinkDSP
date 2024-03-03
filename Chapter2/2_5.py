import sys
sys.path.insert(0, '..')
import thinkdsp
from matplotlib import pyplot

chapter = 2
exercise = 5

print("\nExercise ",chapter,"-",exercise)

def SpectrumModifier(spectrum):
    spectrum.hs[0] = 0
    spectrum.hs[1:] /= spectrum.fs[1:]
    return spectrum

print("Plotting triangle wave spectrum")
triangle = thinkdsp.TriangleSignal()
wave = triangle.make_wave()
spectrum = wave.make_spectrum()
spectrum.plot()
pyplot.title('triangle Wave Spectrum')
pyplot.xlabel('Freq (Hz)')
pyplot.show()

print("Playing triangle wave...")
wave.normalize()
wave.write('temp_2_5.wav')
thinkdsp.play_wave('temp_2_5.wav', 'afplay')

print("Plotting modified triangle wave spectrum")
spectrum = SpectrumModifier(spectrum)
spectrum.plot()
pyplot.title('triangle Wave Spectrum')
pyplot.xlabel('Freq (Hz)')
pyplot.show()

print("Playing modified triangle wave...")
wave = spectrum.make_wave()
wave.normalize()
wave.write('temp_2_5.wav')
thinkdsp.play_wave('temp_2_5.wav', 'afplay')

print("Exercise ",chapter,"-",exercise," complete\n")