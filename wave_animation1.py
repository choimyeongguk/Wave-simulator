import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

t = np.arange(0.0, 2*np.pi, 0.001)
s = np.sin(t)
l = plt.plot(t, s)

ax = plt.axis([0,2*np.pi,-1,1])

redDot, = plt.plot([0], [np.sin(0)], 'ro')

def animate(i):
    redDot.set_data(i, np.sin(i))
    return redDot,

Animation = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, 2*np.pi, 0.1), interval=15, blit=True, repeat=True)

plt.show()