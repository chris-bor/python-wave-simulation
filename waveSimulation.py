import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
w, h = 1024, 1024

def f(x, y, t):
    global w, h
    fx = x - w/2.
    fy = y - h/2.
    d = np.sqrt(fx*fx + fy*fy)
    return (128.0 + 127.0*np.cos(d/10.0 - t/7.0) / (d/10.0 + 5.0))
    
x = np.linspace(0, w-1, w)
y = np.linspace(0, h-1, h).reshape(-1, 1)

t = 0
dt = 1

im = plt.imshow(f(x, y, t), animated=True)

def updatefig(*args):
    global x, y, t
    t += dt
    im.set_array(f(x, y, t))
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=1, blit=True)
plt.show()