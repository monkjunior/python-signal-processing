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
A = 87.56

yn = np.zeros(len(xn))
i = 0

for i in range(len(xn)):
    if np.abs(xn[i]) <= V/A:
        yn[i] = ((A*np.abs(xn[i]))/(1+np.log(A)))*np.sign(xn[i])
    if np.abs(xn[i]) > V/A and np.abs(xn[i]) <= V:
        yn[i] = (V*(1+np.log(A*np.abs(xn[i])/(V)))/(1 + np.log(A)))*np.sign(xn[i])

# xdn
xdn = np.zeros(len(yn))
i = 0

for i in range(len(yn)):
    if yn[i] < V/(1 + np.log(A)) and yn[i] > -V/(1 + np.log(A)):
        xdn[i]=yn[i]*(1 + np.log(A))/A
    else:
        if yn[i] < 0:
            xdn[i] = -(np.power(np.e,-1.0+(-yn[i]/V)*(1+np.log(A))))*V/A
        elif yn[i] > 0:
            xdn[i] = (np.power(np.e,-1.0+(yn[i]/V)*(1+np.log(A))))*V/A
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

 

