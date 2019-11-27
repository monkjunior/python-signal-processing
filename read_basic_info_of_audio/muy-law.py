# Bai tap: https://husteduvn-my.sharepoint.com/:w:/r/personal/son_vn163580_sis_hust_edu_vn/_layouts/15/Doc.aspx?sourcedoc=%7B9DCC30FC-C2FC-4917-987D-CE40D6534B22%7D&file=LawMu.docx&action=edit&mobileredirect=true&wdNewAndOpenCt=1574156740293&wdPreviousSession=af6ba734-1a0f-4f61-8456-55b6b853d357&wdOrigin=OFFICECOM-WEB&START=&UPLOAD=

# numpy functions are used:
# https://pythontic.com/visualization/charts/sinewave
# https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.log.html
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.sign.html

import numpy as np
import matplotlib.pyplot as plot

x_max = 5
F = 10
Fs = 100


time        = np.arange(0,41,1/Fs) 
xn   = x_max*np.sin(2*np.pi*time*10/100) 

# Max value of signal xn
V = xn.max()
muy = 255
yn = (V*np.log(1+(250*(np.abs(xn)/V)))/np.log(1+muy))*np.sign(xn)

# xdn - decompress from yn
xdn = np.zeros(len(yn))
i = 0
for i in range(len(yn)):
    if yn[i] > 0:
        xdn[i] = (np.power((1+muy),(yn[i]/V))-1)*V/muy
    elif yn[i] < 0:
        xdn[i] = (1-np.power((1+muy),(-yn[i]/V)))*V/muy
    else:
        xdn[i] = 0
    print(f'{i}\t{xn[i]}\t{yn[i]}\t{xdn[i]}\t{xdn[i]-xn[i]}')

#DRAW XN
plot.subplot(3,1,1)
plot.plot(time, xn) 
plot.ylabel('x(n)') 
plot.grid(True, which='both')
plot.axhline(y=0, color='k')

# DRAW YN
plot.subplot(3,1,2)
plot.plot(time, yn) 
plot.ylabel('y(n)') 
plot.grid(True, which='both')
plot.axhline(y=0, color='k')

# DRAW XDN
plot.subplot(3,1,3)
plot.plot(time, xdn) 
plot.ylabel('xd(n)') 
plot.grid(True, which='both')
plot.axhline(y=0, color='k')

plot.show()

 

