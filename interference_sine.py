import matplotlib.pyplot as plt
import numpy
from time import sleep

print("파동1")
waveLength_1 = int(input('파장 : '))
amplitude_1 = int(input('진폭 : '))
print("파동2")
waveLength_2 = int(input('파장 : '))
amplitude_2 = int(input('진폭 : '))

x_1 = [];y_1 = []
x_2 = [];y_2 = []
X = [];Y = []
for i in range(0, 4*waveLength_1):
 x_1.append(i)
 x_2.append(i)
 X.append(i)
 y_1.append(0)
 y_2.append(0)
 Y.append(0)

plt.ion()
fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)
ax.set_title('Interference of Sine', fontsize=20)
ax.set_xlim(-(4*waveLength_1*0.1), 4*waveLength_1*1.1)
y_max = abs(amplitude_1)+abs(amplitude_2)
ax.set_ylim(-y_max*1.1, y_max*1.1)
ax.plot([-4*waveLength_1*0.1, 4*waveLength_1*1.1],[0,0], color='black', lw=3)
wave1, = ax.plot(x_1, y_1, color='blue', lw=2)
wave2, = ax.plot(x_2, y_2, color='blue', lw=2)
wave3, = ax.plot(X, Y, color='red', lw=3.5)


num=0
while(True):
 for i in range(0, 4*waveLength_1):
  y_1[i] += amplitude_1*numpy.sin(-2*numpy.pi/waveLength_1*i+num)
 for i in range(0, 4*waveLength_1):
  y_2[i] += amplitude_2*numpy.sin(-2*numpy.pi/waveLength_2*i+num)
 for i in range(0, 4*waveLength_1):
  Y[i] += amplitude_1*numpy.sin(-2*numpy.pi/waveLength_1*i+num)+amplitude_2*numpy.sin(-2*numpy.pi/waveLength_2*i+num)
 wave1.set_ydata(y_1)
 wave2.set_ydata(y_2)
 wave3.set_ydata(Y)
 fig.canvas.draw()
 fig.canvas.flush_events()
 for i in range(0, 4*waveLength_1):
  y_1[i] -= amplitude_1*numpy.sin(-2*numpy.pi/waveLength_1*i+num)
 for i in range(0, 4*waveLength_1):
  y_2[i] -= amplitude_2*numpy.sin(-2*numpy.pi/waveLength_2*i+num)
 for i in range(0, 4*waveLength_1):
  Y[i] -= amplitude_1*numpy.sin(-2*numpy.pi/waveLength_1*i+num)+amplitude_2*numpy.sin(-2*numpy.pi/waveLength_2*i+num)
 num += 0.1