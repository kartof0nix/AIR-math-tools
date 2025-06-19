import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from math import * 
def animateVector(func, t0, tn):
    fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

    def draw(func, theta):
        r = func(theta)
        if(len(r) == 3):
            u, v, w = r
            return 0, 0, 0, u, v, w
        return r
    
    quiver = ax.quiver(*draw(func, 0))

    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)

    def update(theta):
        global quiver
        quiver.remove()
        quiver = ax.quiver(*draw(func, theta))


    ani = FuncAnimation(fig, update, frames=np.linspace(t0,tn,200), interval=50)
    plt.show()

def f(t):
    return [cos(t), sin(t), 0]
animateVector(f, 0, 4 * pi)
# a = [[1, 2, 3], [4, 5, 6]]
# print(a)
# X, Y, Z, U, V, W = zip(*a)
