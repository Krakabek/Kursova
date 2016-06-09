__author__ = 'Danny'
from scipy.integrate import odeint
import numpy
import pylab as p
import math
import mpl_toolkits.mplot3d.axes3d as p3


def F_Drugs(t):
    if t < 5 and 0.3 < math.modf(t)[0] < 0.5:
        return 1
    else:
        return 0


def emotionsDrugs(state, t):
    R = state[0]
    H = state[1]
    b = 2
    return [H, -b * H - R + F_Drugs(t)]


t = p.arange(0, 15, 0.01)
state0 = [0.001, 0.001]
drugsSol = odeint(emotionsDrugs, state0, t)

p.figure()
p.subplot(211)
p.plot([0.4, 1.4, 2.4, 3.4, 4.4], [1, 1, 1, 1, 1], 'ro')
p.axis([0, 15, 0, 2])
p.legend('F')
p.title('Positive event')
p.subplot(212)
p.plot(t, drugsSol)
p.axhline(0, color='black')
p.axis([0, 15, -0.5, 0.5])
p.xlabel('Time')
p.legend(('Reaction', 'Happiness'))
p.title('Reaction to a repetative positive event')
p.savefig('Repetative PositiveEvent.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(drugsSol[:, 0], drugsSol[:, 1])
p.axis([-0.1, 0.3, -0.2, 0.2])
p.axhline(0, color='black')
p.axvline(0, color='black')
p.xlabel('Reaction')
p.ylabel('Happiness')
p.savefig('Repetative PositiveEvent Parametric.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(drugsSol[:, 0], drugsSol[:, 1])
p.axis([-0.1, 0.3, -0.2, 0.2])
p.axhline(0, color='black')
p.axvline(0, color='black')
p.xlabel('Reaction')
p.ylabel('Happiness')
ax = p.gca() #uncomment for arrows
i = 0
while i < len(t)-20:
    arr = p.Arrow(drugsSol[:, 0][i], drugsSol[:, 1][i], drugsSol[:, 0][i+10] - drugsSol[:, 0][i], drugsSol[:, 1][i+10] - drugsSol[:, 1][i], edgecolor="white", width=0.02)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 20
p.savefig('Repetative PositiveEvent Parametric Arrow.png', dpi=300)  #  uncomment to save plots
p.show()


t = p.arange(0, 15, 0.01)
state0 = [-1, 1]
state1 = [1, 1]
state2 = [1, -1]
state3 = [-1, -1]
drugsSol0 = odeint(emotionsDrugs, state0, t)
drugsSol1 = odeint(emotionsDrugs, state1, t)
drugsSol2 = odeint(emotionsDrugs, state2, t)
drugsSol3 = odeint(emotionsDrugs, state3, t)


p.figure()
p.plot(drugsSol0[:, 0], drugsSol0[:, 1])
p.plot(drugsSol1[:, 0], drugsSol1[:, 1])
p.plot(drugsSol2[:, 0], drugsSol2[:, 1])
p.plot(drugsSol3[:, 0], drugsSol3[:, 1])
p.axis([-1.5, 1.5, -1.5, 1.5])
p.axhline(0, color='black')
p.axvline(0, color='black')
p.xlabel('Reaction')
p.ylabel('Happiness')
ax = p.gca() #uncomment for arrows
i = 0
while i < len(t)-20:
    arr = p.Arrow(drugsSol0[:, 0][i], drugsSol0[:, 1][i], drugsSol0[:, 0][i +10] - drugsSol0[:, 0][i], drugsSol0[:, 1][i +10] - drugsSol0[:, 1][i], edgecolor="white", width=0.2)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 20
ax = p.gca() #uncomment for arrows
i = 0
while i < len(t)-20:
    arr = p.Arrow(drugsSol1[:, 0][i], drugsSol1[:, 1][i], drugsSol1[:, 0][i +10] - drugsSol1[:, 0][i], drugsSol1[:, 1][i +10] - drugsSol1[:, 1][i], edgecolor="white", width=0.2)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 20
i = 0
while i < len(t)-20:
    arr = p.Arrow(drugsSol2[:, 0][i], drugsSol2[:, 1][i], drugsSol2[:, 0][i +10] - drugsSol2[:, 0][i], drugsSol2[:, 1][i +10] - drugsSol2[:, 1][i], edgecolor="white", width=0.2)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 20
i = 0
while i < len(t)-20:
    arr = p.Arrow(drugsSol3[:, 0][i], drugsSol3[:, 1][i], drugsSol3[:, 0][i +10] - drugsSol3[:, 0][i], drugsSol3[:, 1][i +10] - drugsSol3[:, 1][i], edgecolor="white", width=0.2)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 20
p.savefig('Repetative PositiveEvent Parametric Arrow Multiple.png', dpi=300)  #  uncomment to save plots
p.show()