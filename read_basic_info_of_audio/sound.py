import wave
import numpy as np
import matplotlib.pyplot as plt

def soundInfo(path):
    fp = wave.open(path, "r")
    print("\n\nPath \t\t\t:", path)
    if fp.getnchannels() == 1 :
        print("Channels \t\t: mono")
    elif fp.getnchannels() == 2 :
        print("Channels \t\t: stereo")
    else:
        print("Channels \t\t:", fp.getnchannels())
    print("Number of audio frame \t:", fp.getnframes())
    print("Sample width in bytes \t:", fp.getsampwidth())
    print("Sampling frequency \t:", fp.getframerate())

    duration = fp.getnframes()/fp.getframerate()
    print("Duration \t\t:", duration, "secs")

    fp.close()

def readSound(path):
    fp = wave.open(path, "r")
    
    channels = fp.getnchannels()
    nframes = fp.getnframes()
    sampleWidth = fp.getsampwidth()
    frameRate = fp.getframerate()

    #Read and return all audio's frames as byte objects 
    z_str = fp.readframes(nframes)
    fp.close()
    
    dtype_map = {1: np.int8, 2: np.int16, 3: "special", 4: np.int32}
    if sampleWidth not in dtype_map:
        raise ValueError("Sample width %d unknown" % sampleWidth)
    elif sampleWidth == 3:
        # xs is poor values read from audio
        xs = np.fromstring(z_str, dtype=np.int8).astype(np.int32)
        # ys is values based on sampleWidth that is calculated from xs
        ys = (xs[2::3] * 256 + xs[1::3]) * 256 + xs[0::3]
    else:
        ys = np.fromstring(z_str, dtype=dtype_map[sampleWidth])

    if channels == 2:
        ys = ys[::2]

    #Time series
    ts = np.arange(len(ys))/frameRate

    #Check the lenght of sample series and time series to compare with number of frames
    print("\nType ys \t:", type(ys))
    print("Lenght ys \t:", len(ys))
    print("Type ts \t:", type(ts))
    print("Lenght ts \t:", len(ts))

    #Simple plot
    plt.plot(ts, ys)
    plt.show()
