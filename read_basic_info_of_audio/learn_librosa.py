import librosa
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal2

#    Load the audio as a waveform `signal`
#    Store the sampling rate as `fs`
signal, fs = librosa.load("./res/Xe.wav", sr=None)
#time = np.arange(len(signal))/fs
time = np.linspace(0, 1000*len(signal)/fs, len(signal))

# Raw file
plt.subplot(4,1,1)
plt.plot(time, signal)

start = 6000    #Demo frame start here
N = 256         #Frame samples
data = signal[start:start+N]

time_data = time[start:start+N]
# data is a frame from signal that has 256 samples
# draw data
plt.subplot(4,1,2)
plt.plot(time_data, data)

# Truoc khi cho qua cua so hamming can cho data qua bo loc hieu chinh thong cao
A = [1.0]
B = [1.0, -0.95]
data2 = signal2.lfilter(B, A, data, axis=-1, zi=None)


# So sanh dang bien do cua tuyen an trong 2 TH co bo loc va khong co bo loc hieu chinh
# draw data2
plt.subplot(4,1,2)
plt.plot(time_data, data2)

# Thay doi he so 0.95 xem co gi khac biet

# draw hamming overlay sample
plt.subplot(4,1,2)
plt.plot(time_data, np.hamming(256))

# Nhan voi cua so Hamming
data = data*np.hamming(256)
# draw data
plt.subplot(4,1,3)
plt.plot(time_data, data2)

p = 14
a = librosa.lpc(data,p)
# a includes ai, p, $(bac cua bo loc dao A(Z) :D)

# Sau khi co a them cac mau bang 0 vao cuoi
a = np.append(a, np.zeros(N-p))

# Compute spectrum enveloppe from fft of ai(LPC)
data_freq = np.fft.fft(a, 256)
magEnvelope = np.abs(data_freq)
magDb = -20.0*np.log10(magEnvelope/max(magEnvelope))

# Khac do truc tan so
frequency =  np.linspace(0, N // 2, num= N//2-1)

# Ve dap ung bien do cua tuyen am
plt.subplot(4,1,4)
#plt.plot(np.arange(127)*(fs/255),magDb[0:127])
plt.plot(frequency,magDb[0:127])

# Bay gio ta tim cac dao ham cuc bo - local formant ?!!
# Su dung phuong phap dao ham

plt.show()
