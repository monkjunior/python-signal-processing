import numpy as np
import scipy.io.wavfile as wf
import matplotlib.pyplot as plt


from scipy.fftpack import fft, ifft  
#https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html


def magnitudeSeries(dataSeries, timeSeries):
    #Raw data
    ys = dataSeries
    ts = timeSeries
    #Framing
    ts2 =  ts[159::160]
    ys2 = np.ones((len(ts2), 1))

    #ElementsWise with Hamming window
    i = 0
    c = 0
    while (i+320)<len(ys) :
        frame = np.absolute(ys[i:i+320])
        frame = frame*np.hamming(320)
        ys2[c] = frame.sum()
        c = c + 1
        i = i + 160

    return ys2

def energySeries(dataSeries, timeSeries):
    #Raw data
    ys = dataSeries
    ts = timeSeries
    #Framing
    ts2 =  ts[159::160]
    ys2 = np.ones((len(ts2), 1))

    #ElementsWise with Hamming window
    i = 0
    c = 0
    while (i+320)<len(ys) :
        frame = ys[i:i+320]*np.hamming(320)
        frame = np.square(frame)
        ys2[c] = frame.sum()
        c = c + 1
        i = i + 160
    return ys2

def zcrSeries(dataSeries, timeSeries):
    #Raw data
    ys = dataSeries
    ts = timeSeries
    #Framing
    ts2 =  ts[159::160]
    ys2 = np.ones((len(ts2), 1))

    #ElementsWise with Hamming window
    i = 0
    c = 0
    while (i+320)<len(ys) :
        frame = ys[i:i+320]
        zero_crosses = np.nonzero(np.diff(frame>0))[0]
        #frame is data input. Example [-1, 2, 3, -4, -5, 6]
        #(frame > 0) return a boolean array. Example [False, True, True, False, False, True]
        #np.diff(frame > 0) --> [1, 0, -1, 0, 1] --> [True, False, True, False, True]
        #np.nonzero(np.diff(frame > 0)) --> (array([0, 2, 4]),) This is index of element != 0
        #np.nonzero(np.diff(frame > 0))[0] --> [0, 2, 4]
        ys2[c] = zero_crosses.size
        c = c + 1
        i = i + 160

    return ys2


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

#Plot spectrum, short-time magnitude, zero crossing rate
def plotSound2(path):
    #Raw data series and time series
    data = wf.read(path)
    ys = data[1]
    ts = np.arange(len(ys))/data[0]

    #Time series for plot, 320samples/window, 160samples/shift  
    ts2 =  ts[159::160]
    #Energy data series
    ys1 = energySeries(ys, ts)
    #Magniture data series
    ys2 = magnitudeSeries(ys, ts)
    #Zero cross rate data series
    ys3 = zcrSeries(ys, ts)

    sampleRate = data[0]
    time = data[1].shape[0]/sampleRate
    frameWidth = 0.02 #ms
    frameNumber = time/frameWidth
    samplePerFrame = len(ys)/frameNumber
    #We can also specify channels form shape of data
    #Bit per sample = Total bits / number of samples
    
    #PLOT TIME :D

    #amplitude
    plt1 = plt.subplot(4, 1, 1) #Mattrix 4 rows 1 column, element 1rd
    plt.plot(ts, ys, '-', lw=1)
    plt.grid(True)


    #short-time energy
    plt2 = plt.subplot(4, 1, 2) #Mattrix 4 rows 1 column, element 2nd
    plt.plot(ts2, ys1, '-', lw=1)
    plt.grid(True)


    #short-time magnitude
    plt3 = plt.subplot(4, 1, 3) #Mattrix 4 rows 1 column, element 3rd
    plt.plot(ts2, ys2, '-', lw=1)
    plt.grid(True)
    
    #zero crossing rate
    plt4 = plt.subplot(4, 1, 4) #Mattrix 4 rows 1 column, element 4th
    plt.plot(ts2, ys3, '-', lw=1)
    plt.xlabel("Time(ms)")
    plt.grid(True)

    plt.tight_layout()
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()

# Add fourier transform
def plotSound3(path):
    #Raw data series and time series
    data = wf.read(path)
    ys = data[1]
    fft_ys = fft(ys)
    ts = np.arange(len(ys))/data[0]

    #Time series for plot, 320samples/window, 160samples/shift  
    ts2 =  ts[159::160]
    #Energy data series
    ys1 = energySeries(ys, ts)
    fft_ys1 = fft(ys1)
    #Magniture data series
    ys2 = magnitudeSeries(ys, ts)
    fft_ys2 = fft(ys2)
    #Zero cross rate data series
    ys3 = zcrSeries(ys, ts)
    fft_ys3 = fft(ys3)  

    sampleRate = data[0]
    time = data[1].shape[0]/sampleRate
    frameWidth = 0.02 #ms
    frameNumber = time/frameWidth
    samplePerFrame = len(ys)/frameNumber
    #We can also specify channels form shape of data
    #Bit per sample = Total bits / number of samples
    
    #PLOT TIME :D

    #amplitude
    plt1 = plt.subplot(4, 1, 1) #Mattrix 4 rows 1 column, element 1rd
    plt.plot(ts, ys, '-', lw=1)
    plt.grid(True)


    #short-time energy
    plt2 = plt.subplot(4, 1, 2) #Mattrix 4 rows 1 column, element 2nd
    plt.plot(ts2, ys1, '-', lw=1)
    plt.grid(True)


    #short-time magnitude
    plt3 = plt.subplot(4, 1, 3) #Mattrix 4 rows 1 column, element 3rd
    plt.plot(ts2, ys2, '-', lw=1)
    plt.grid(True)
    
    #zero crossing rate
    plt4 = plt.subplot(4, 1, 4) #Mattrix 4 rows 1 column, element 4th
    plt.plot(ts2, ys3, '-', lw=1)
    plt.xlabel("Time(ms)")
    plt.grid(True)

    plt.tight_layout()
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()


def hamTuTuongQuan(path):
    #Raw data series and time series
    data = wf.read(path)
    ys = data[1]
    ts = np.arange(len(ys))/data[0]

    #Time series for plot, 320samples/window, 160samples/shift  
    ts2 =  ts[159::160]
    #Energy data series
    ys1 = energySeries(ys, ts)
    #Zero cross rate data series
    ys3 = zcrSeries(ys, ts)

    sampleRate = data[0]
    time = data[1].shape[0]/sampleRate
    frameWidth = 0.02 #ms
    frameNumber = time/frameWidth
    samplePerFrame = len(ys)/frameNumber

    N = 320
    k = 160
    start = 9500    #Demo frame start here
    #Demo frame
    example = ys[start:start+N]
    example_ts = ts[start:start+N]

    r = np.zeros(k)
    ts_r = (np.arange(k) + 9500)/sampleRate

    #Tinh ham tu tuong quan
    for i in range(0, k-1):
        r[i] = sum((1.0*example[n]*example[n+i]) for n in range(0, N-i-1)) #1.0*x --> float --> chong tran

    #Tinh T0 cho cua so
    _max = 0
    _index_max = 0
    for j in range(1, len(r)): #Run loop without first value
        if r[j] > r[j-1] and r[j]>r[j-1] and r[j] > _max  : 
            _max = r[j]
            _index_max = j
            #break
    print("T0", _index_max)
    print("T0", _index_max/sampleRate*1000)
    print("F0", 1/(_index_max/sampleRate) )

    #We can also specify channels form shape of data
    #Bit per sample = Total bits / number of samples
    
    #PLOT TIME :D

    #amplitude
    plt1 = plt.subplot(4, 1, 1) #Mattrix 4 rows 1 column, element 1rd
    plt.plot(ts, ys, '-', lw=1)
    plt.grid(True)


    #example frame
    plt2 = plt.subplot(4, 1, 2) #Mattrix 4 rows 1 column, element 2nd
    plt.plot(example_ts, example, '-', lw=1)
    plt.grid(True)


    #ham tu tuong quan cho frame
    plt3 = plt.subplot(4, 1, 3) #Mattrix 4 rows 1 column, element 3rd
    plt.plot(ts_r, r, '-', lw=1)
    plt.grid(True)
    
    #zero crossing rate
    plt4 = plt.subplot(4, 1, 4) #Mattrix 4 rows 1 column, element 4th
    plt.plot(ts2, ys3, '-', lw=1)
    plt.xlabel("Time(ms)")
    plt.grid(True)

    plt.tight_layout()
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()
