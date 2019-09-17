import numpy as np
import scipy.io.wavfile as wf
import matplotlib.pyplot as plt

def plotSound(path1, path2):
    data1 = wf.read(path1)

    ys1 = data1[1]
    ts1 = np.arange(len(ys1))/data1[0]


    sampleRate1 = data1[0]
    time1 = data1[1].shape[0]/sampleRate1
    #We can also specify channels form shape of data
    #Bit per sample = Total bits / number of samples

    plt1 = plt.subplot(3, 1, 1) #Mattrix 3 rows 1 column, element 1st
    #plt1.set_ylim(-1,1)
    plt.plot(ts1, ys1, '-', lw=2)
    plt.xlabel('time (s)')
    plt.ylabel('amplitude')
    plt.title("Name: Xe.wav | Sample-rate = {} | Time = {}".format(sampleRate1, time1))
    plt.grid(True)
    print("Sample rate: ", data1[0])
    print("\nSample values: ", data1[1])



    data2 = wf.read(path2)
    ys2 = data2[1]
    ts2 = np.arange(len(ys2))/data2[0]

    sampleRate2 = data2[0]
    time2 = data2[1].shape[0]/sampleRate2

    plt2 = plt.subplot(3, 1, 3) #Mattrix 3 rows 1 column, element 3rd
    #plt2.set_ylim(-1,1)
    plt.plot(ts2, ys2, '-', lw=2)
    plt.xlabel('time (s)')
    plt.ylabel('amplitude')
    plt.title('Name: khoosoothunhus.wav | Sample-rate = {} | Time = {}'.format(sampleRate2, time2))
    plt.grid(True)
    print("Sample rate: ", data2[0])
    print("\nSample values: ", data2[1])


    plt.tight_layout()
    plt.show()

