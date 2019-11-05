import librosa
import numpy as np
import matplotlib.pyplot as plt
#    Load the audio as a waveform `signal`
#    Store the sampling rate as `fs`
signal, fs = librosa.load("./res/Xe.wav", sr=None)
#time = np.arange(len(signal))/fs
time = np.linspace(0, 1000*len(signal)/fs, len(signal))

# Raw file
plt.subplot(3,1,1)
plt.plot(time, signal)

start = 6000    #Demo frame start here
N = 256         #Frame samples
data = signal[start:start+N]
time_data = time[start:start+N]
# data is a frame from signal that has 256 samples
# draw data
plt.subplot(3,1,2)
plt.plot(time_data, data)

p = 14
a = librosa.lpc(data,p)
# a includes ai, p, $(bac cua bo loc dao A(Z) :D)

# Sau khi co a them cac mau bang 0 vao cuoi
a = np.append(a, np.zeros(N-p))

# Compute spectrum enveloppe from fft of ai(LPC)
data_freq = np.fft.fft(a, 256)
magEnvelope = np.abs(data_freq)
magDb = -20.0*np.log10(magEnvelope/max(magEnvelope))

# Ve dap ung bien do cua tuyen am
plt.subplot(3,1,3)
plt.plot(np.arange(127)*(fs/255),magDb[0:127])

# Bay gio ta tim cac dao ham cuc bo - local formant ?!!
# Su dung phuong phap dao ham

plt.show()
