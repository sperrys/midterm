#
# fft.py
#

from scipy.signal.windows import flattop

import numpy as np

import wave
import argparse
import struct
import os
import sys

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

fs = 40000

def plot_fft(data, num_samples):

    (mag, freq) = get_fft(data, num_samples)

    # Plot the reference spectrum
    plt.plot(freq, mag)

    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.title('Clarinet Harmonic')
    plt.xlim(0, 1500)  # set the xlim to left, right

    plt.show()



def get_fft(data, num_samples):


    # Get the signal length
    n = num_samples

    w = np.hanning(n)
    w = flattop(n, False)

    # Get time resolution
    dt = 1 / float(fs)

    # Perform real fft
    fft_output = np.fft.rfft(data)

    # Calculate frequency bins
    rfreqs = np.fft.rfftfreq(n, dt)

    # Take only magnitude of spectrum
    fft_mag = np.abs(fft_output)

    # Double everything because of alias at Nyquist
    fft_mag = fft_mag * 2 / n

    # Scale magnitudes to log scale
    MAG_dB = 20 * np.log10(fft_mag/max(fft_mag))

    return np.array([np.array(MAG_dB), np.array(rfreqs)])


if __name__ == '__main__':

    fp = wave.open("Midterm_Makeup_export/clarinetharmonic.wav", 'r')

    n = fp.getnframes()
    frames = fp.readframes(n)

    data = struct.unpack('{n}h'.format(n=n), frames)
    data = np.array([abs(d / n) for d in data])
    plot_fft(data, n)
