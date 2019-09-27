import sound_class
import sound_home

#FILES
path1 = "./res/484484__nowism__techno-x-otherkick.wav"
path2 = "./res/190704__ofabra__supermercado-mono.wav"
path3 = "./res/ma.wav"
path4 = "./res/Xe.wav"
path5 = "./res/khoosoothunhus.wav"

#Code from home
#sound_home.soundInfo(path1)
#sound_home.soundInfo(path2)
#sound_home.soundInfo(path3)
#sound_home.readSound(path3)

#Code on class

sound_class.plotSound2(path5)

import numpy as np
a = np.array([-1, 2, 3, -4, -5, 6])
print(np.nonzero(np.diff(a > 0)))