from matplotlib import pyplot as plt
import numpy

x = []
y = []
opacity1 = []
opacity2 = []
distance = 0
num = 0
for i in range(50):
  x.append(i)
  y.append(i)
for i in range(2500):
  opacity1.append(0)
  opacity2.append(0)

  # 주기 및 파동 시작점 좌표 입력
cycle = int(input('주기 : '))
print("좌표 입력(정수, 띄어쓰기로 구분)")
spot1_x, spot1_y = map(int, input('spot1 좌표 : ').split())
spot2_x, spot2_y = map(int, input('spot2 좌표 : ').split())

  # 그래프 설정
plt.figure(figsize=(7,7))
plt.title('Interference of Water Wave', fontsize=20)
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.scatter(spot1_x, spot1_y, c='red',s=50, zorder=2)
plt.scatter(spot2_x, spot2_y, c='red',s=50, zorder=2)

  # 시작점으로 부터의 거리 계산 후, 파동 높이 만큼의 투명도 계산
for i in range(50):
  for j in range(50):
    distance = ((spot1_x-i)**2+(spot1_y-j)**2)**.5
    opacity1[num] = 0.5+numpy.sin(2/cycle*numpy.pi*distance)/2
    num += 1

distance = 0
num = 0
for i in range(50):
  for j in range(50):
    distance = ((spot2_x-i)**2+(spot2_y-j)**2)**.5
    opacity2[num] = 0.5+numpy.sin(2/cycle*numpy.pi*distance)/2
    num += 1

  # 그래프 출력
num = 0
for i in range(50):
  for j in range(50):
    plt.scatter(x[i], y[j], color='#0000ff',s=50, alpha=(opacity1[num]+opacity2[num])/2)
    num += 1
plt.show()