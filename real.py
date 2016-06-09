__author__ = 'Danny'
from scipy.integrate import odeint
import numpy
import pylab as p
import math
import mpl_toolkits.mplot3d.axes3d as p3


normal = numpy.random.normal(0, 1, 1000)


def F_Real(t):
    return normal[t * 100]


def emotionsReal(state, t):
    R = state[0]
    H = state[1]
    b = 2
    return [H, -b * H - R + F_Real(t)]

t1 = p.arange(0, 10, 0.01)
state0 = [0.001, 0.001]
realSol = odeint(emotionsReal, state0, t1)

p.figure()
p.subplot(211)
p.plot(normal)
p.subplot(212)
p.plot(t1, realSol)
p.axhline(0, color='black')
p.ylim([-0.5, 0.5])
p.xlabel('Time')
p.legend(('R', 'H'))
p.title('Real life')
# p.savefig('Real Life.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(realSol[:, 0], realSol[:, 1])
p.axis([-0.1, 0.2, -0.2, 0.2])
p.axhline(0, color='black')
p.axvline(0, color='black')
p.xlabel('Reaction')
p.ylabel('Happiness')
p.legend(('System state', ''))
p.title('Parametric plot')
# p.savefig('Real Life Parametric.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(realSol[:, 0], realSol[:, 1])
p.axis([-0.1, 0.2, -0.2, 0.2])
p.axhline(0, color='black')
p.axvline(0, color='black')
p.xlabel('Reaction')
p.ylabel('Hapiness')
ax = p.gca() #uncomment for arrows
i = 0
while i < len(t1)-20:
    arr = p.Arrow(realSol[:, 0][i], realSol[:, 1][i], realSol[:, 0][i+10] - realSol[:, 0][i], realSol[:, 1][i+10] - realSol[:, 1][i], edgecolor="white", width=0.02)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 20
p.savefig('Real Life Parametric Arrow.png', dpi=300)  #  uncomment to save plots
p.show()