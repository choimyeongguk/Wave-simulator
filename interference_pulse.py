from matplotlib import pyplot as plt
from time import sleep
import numpy

def pulse_left(x):  # 좌측에서 시작하는 파동 이동
 for i in range(101):
  Y[i+x-51] = Y[i+x-51] - k1*numpy.sin(numpy.pi*i/100)
 for i in range(101):
  Y[i+x-50] = Y[i+x-50] + k1*numpy.sin(numpy.pi*i/100)

def pulse_right(x):  # 우측에서 시작하는 파동 이동
 for i in range(101):
  Y[300-i-x+51] = Y[300-i-x+51] - k2*numpy.sin(numpy.pi*i/100)
 for i in range(101):
  Y[300-i-x+50] = Y[300-i-x+50] + k2*numpy.sin(numpy.pi*i/100)

def pulse2_left(x):  # 좌측에서 시작하는 파동 이동
 for i in range(101):
  y_l[i+x-51] = y_l[i+x-51] - k1*numpy.sin(numpy.pi*i/100)
 for i in range(101):
  y_l[i+x-50] = y_l[i+x-50] + k1*numpy.sin(numpy.pi*i/100)

def pulse2_right(x):  # 우측에서 시작하는 파동 이동
 for i in range(101):
  y_r[300-i-x+51] = y_r[300-i-x+51] - k2*numpy.sin(numpy.pi*i/100)
 for i in range(101):
  y_r[300-i-x+50] = y_r[300-i-x+50] + k2*numpy.sin(numpy.pi*i/100)

X = [];Y = []
x_l = [];y_l = []
x_r = [];y_r = []
k1 = float(input('좌측 파동의 높이 : '))
k2 = float(input('우측 파동의 높이 : '))
for i in range(0, 301):
 X.append(i)
 x_l.append(i)
 x_r.append(i)
 Y.append(0)
 y_l.append(0)
 y_r.append(0)

plt.ion()
plt.style.use('bmh')
fig = plt.figure(figsize=(6.4, 4))
ax = fig.add_subplot(111)
ax.set_title('Interference of Pulse', fontsize=20)
ax.set_xlim(-10, 310)
if(k1>0.0 and k2>0.0):  # 그래프 y축 범위 설정
  ax.set_ylim(-(k1+k2)*0.2, (k1+k2)*1.2)
elif(k1<0.0 and k2>0.0):
  ax.set_ylim(k1*1.2, k2*1.2)
elif(k2<0.0 and k1>0.0):
  ax.set_ylim(k2*1.2, k1*1.2)
else:
  ax.set_ylim((k1+k2)*1.2, -(k1+k2)*0.2)
ax.grid(True)
wave1, = ax.plot(X, Y, color='red', lw=5, zorder=3)
wave2, = ax.plot(x_l, y_l, color='black', lw=1, zorder=2)
wave3, = ax.plot(x_r, y_r, color='black', lw=1, zorder=1)

while(1):
 for i in range(101):  # 그래프 초기화
  Y[i] = k1*numpy.sin(numpy.pi*i/100)
 for i in range(101):
  Y[300-i] = k2*numpy.sin(numpy.pi*i/100)

 for i in range(101):
  y_l[i] = k1*numpy.sin(numpy.pi*i/100)
  y_l[300-i] = 0
 for i in range(101):
  y_r[i] = 0
  y_r[300-i] = k2*numpy.sin(numpy.pi*i/100)

 for i in range(51, 251):  # 파동 이동 및 이미지 출력
  pulse_left(i) 
  pulse_right(i)
  pulse2_left(i) 
  pulse2_right(i)
  wave1.set_ydata(Y)
  wave2.set_ydata(y_l)
  wave3.set_ydata(y_r)
  fig.canvas.draw()
  fig.canvas.flush_events()
 sleep(1)