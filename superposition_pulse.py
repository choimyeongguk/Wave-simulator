from matplotlib import pyplot as plt
from time import sleep
import numpy

def pulse_left(x):
 for i in range(101):
  Y[i+x-51] = Y[i+x-51] - k1*numpy.sin(numpy.pi*i/100)
 for i in range(101):
  Y[i+x-50] = Y[i+x-50] + k1*numpy.sin(numpy.pi*i/100)

def pulse_right(x):
 for i in range(101):
  Y[500-i-x+51] = Y[500-i-x+51] - k2*numpy.sin(numpy.pi*i/100)
 for i in range(101):
  Y[500-i-x+50] = Y[500-i-x+50] + k2*numpy.sin(numpy.pi*i/100)

X = []
Y = []
k1 = float(input('좌측 파동의 높이 : '))
k2 = float(input('우측 파동의 높이 : '))
for i in range(0, 501):
 X.append(i)
 Y.append(0)

plt.ion()
fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
ax.set_title('superposition of pulse wave')
ax.set_xlim(-10, 510)
if(k1>0.0 and k2>0.0):
  ax.set_ylim(-(k1+k2)*0.2, (k1+k2)*1.2)
elif(k1<0.0 and k2>0.0):
  ax.set_ylim(k1*1.2, k2*1.2)
elif(k2<0.0 and k1>0.0):
  ax.set_ylim(k2*1.2, k1*1.2)
else:
  ax.set_ylim((k1+k2)*1.2, -(k1+k2)*0.2)
ax.grid(True)
wave, = ax.plot(X, Y, color='red', lw=5, zorder=3)

while(1):
 for i in range(101):
  Y[i] = k1*numpy.sin(numpy.pi*i/100)
 for i in range(101):
  Y[500-i] = k2*numpy.sin(numpy.pi*i/100)

 for i in range(51, 451):
  pulse_left(i) 
  pulse_right(i)
  wave.set_ydata(Y)
  fig.canvas.draw()
  fig.canvas.flush_events()
 sleep(1)