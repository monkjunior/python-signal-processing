import wave

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

