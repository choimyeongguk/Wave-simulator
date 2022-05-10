from matplotlib import pyplot as plt
import numpy
import math

def sin(x):
 return math.sin(2*math.pi*x)

x = []
y = []

for i in numpy.arange(-2, 2, 0.01):  # 정의역 : -2~2까지 0.1 간격으로
 x.append(i)
 y.append(sin(i))

plt.figure(figsize=(7,7))  # 그래프 창 크기
plt.axis([-2.5,2.5,-1.5,1.5])  # 그래프 숫자 범위
plt.grid(True)  # 그래프 격자 표시
plt.title('sin')  # 그래프 제목
plt.plot([-50,50],[0,0], color='black')  # x축 그리기
plt.plot([0,0],[-50,50], color='black')  # y축 그리기

plt.scatter(x, y, color='blue')  # 그래프 그리기
plt.show()