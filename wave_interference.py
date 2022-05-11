import matplotlib.pyplot as plt
import numpy
from time import sleep

# waveLength = float(input('파장 : '))
# amplitude = float(input('진폭 : '))
waveLength = 100
x = []
y = []
for i in numpy.arange(0, 2*waveLength, 0.1):
 x.append(i)
 y.append(0)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-10, 210)
ax.set_ylim(-2, 2)
line1, = ax.plot(x, y, color='red', lw=3)
ax.plot([-10, 210],[0,0], color='black', lw=3)

num=0
while(True):
 for i in range(0, 20*waveLength):
  y[i] += numpy.sin(-1*numpy.pi/500*i+num)
 for i in range(0, 20*waveLength):
  y[i] += numpy.sin(1*numpy.pi/500*i+num)
  line1.set_ydata(y)
 fig.canvas.draw()
 fig.canvas.flush_events()
 for i in range(0, 20*waveLength):
  y[i] -= numpy.sin(-1*numpy.pi/500*i+num)
 for i in range(0, 20*waveLength):
  y[i] -= numpy.sin(1*numpy.pi/500*i+num)
 num += 0.05