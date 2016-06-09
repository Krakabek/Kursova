__author__ = 'Danny'
from scipy.integrate import odeint
import numpy
import pylab as p
import math
import mpl_toolkits.mplot3d.axes3d as p3



def F_Lottery(t):
    if 0.3 < t < 0.4:
        return 1
    else:
        return 0


def emotionsLottery(state, t):
    R = state[0]
    H = state[1]
    b = 2
    return [H, -b * H - R + F_Lottery(t)]


t = p.arange(0, 15, 0.01)
state0 = [-1, 1]
state1 = [1, 1]
state2 = [1, -1]
state3 = [-1, -1]
lotterySol0 = odeint(emotionsLottery, state0, t)
lotterySol1 = odeint(emotionsLottery, state1, t)
lotterySol2 = odeint(emotionsLottery, state2, t)
lotterySol3 = odeint(emotionsLottery, state3, t)


p.figure()
p.plot(lotterySol0[:, 0], lotterySol0[:, 1])
p.plot(lotterySol1[:, 0], lotterySol1[:, 1])
p.plot(lotterySol2[:, 0], lotterySol2[:, 1])
p.plot(lotterySol3[:, 0], lotterySol3[:, 1])
p.axis([-2, 2, -2, 2])
p.axhline(0, color='black')
p.axvline(0, color='black')
p.xlabel('Reaction')
p.ylabel('Happiness')
ax = p.gca() #uncomment for arrows
i = 0
while i < len(t)*4/5:
    arr = p.Arrow(lotterySol0[:, 0][i], lotterySol0[:, 1][i], lotterySol0[:, 0][i+0.2*i] - lotterySol0[:, 0][i], lotterySol0[:, 1][i+0.2*i] - lotterySol0[:, 1][i], edgecolor="white", width=0.2)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 1 + 0.25*i
ax = p.gca() #uncomment for arrows
i = 0
while i < len(t)*4/5:
    arr = p.Arrow(lotterySol1[:, 0][i], lotterySol1[:, 1][i], lotterySol1[:, 0][i+0.2*i] - lotterySol1[:, 0][i], lotterySol1[:, 1][i+0.2*i] - lotterySol1[:, 1][i], edgecolor="white", width=0.2)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 1 + 0.25*i
i = 0
while i < len(t)*4/5:
    arr = p.Arrow(lotterySol2[:, 0][i], lotterySol2[:, 1][i], lotterySol2[:, 0][i+0.2*i] - lotterySol2[:, 0][i], lotterySol2[:, 1][i+0.2*i] - lotterySol2[:, 1][i], edgecolor="white", width=0.2)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 1 + 0.25*i
i = 0
while i < len(t)*4/5:
    arr = p.Arrow(lotterySol3[:, 0][i], lotterySol3[:, 1][i], lotterySol3[:, 0][i+0.2*i] - lotterySol3[:, 0][i], lotterySol3[:, 1][i+0.2*i] - lotterySol3[:, 1][i], edgecolor="white", width=0.2)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 1 + 0.25*i
p.savefig('Single PositiveEvent Parametric Arrow Multiple.png', dpi=300)  #  uncomment to save plots
p.show()