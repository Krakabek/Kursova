__author__ = 'Danny'
from scipy.integrate import odeint
import numpy
import pylab as p
import math


#increasing love
def emotionsPair1(state, t):
    R = state[0]
    Hr = state[1]
    J = state[2]
    Hj = state[3]
    b = 1.5
    a = 2
    alpha = 1.2
    beta = 1.2
    return [Hr, -a * Hr - R + alpha * J, Hj, -b * Hj - J + beta * R]


#decreasing love
def emotionsPair2(state, t):
    R = state[0]
    Hr = state[1]
    J = state[2]
    Hj = state[3]
    b = 1.5
    a = 2
    alpha = 1.1
    beta = 1.2
    return [Hr, -a * Hr - R + numpy.exp(-alpha * t) * J, Hj, -b * Hj - J + numpy.exp(-beta * t) * R]


#standart love
def emotionsPair3(state, t):
    R = state[0]
    Hr = state[1]
    J = state[2]
    Hj = state[3]
    b = 2
    a = 0.5
    alpha = 0.1
    beta = 0.02
    return [Hr, -a * Hr - R + numpy.exp(-alpha * t) * J, Hj, -b * Hj - J + numpy.exp(-beta * t) * R]


#ignore love
def emotionsPair4(state, t):
    R = state[0]
    Hr = state[1]
    J = state[2]
    Hj = state[3]
    b = 4
    a = 2
    alpha = 0.01
    beta = 2
    return [Hr, -a * Hr - R + numpy.exp(-alpha * t) * J, Hj, -b * Hj - J + beta * R]


#ignore love flegmatic
def emotionsPair5(state, t):
    R = state[0]
    Hr = state[1]
    J = state[2]
    Hj = state[3]
    b = 4
    a = 2
    alpha = 2
    beta = 2
    return [Hr, -a * Hr - R + numpy.exp(-alpha * t) * J, Hj, -b * Hj - J + beta * R]


t = p.arange(0, 100, 0.01)
t1 = p.arange(0, 300, 0.01)
state0 = [0.1, 0, 0.1, 0]
state3 = [0.2, 0, 0.1, 0]
state4 = [0, 0, 0.2, 0]
emotionsSol1 = odeint(emotionsPair1, state0, t)
emotionsSol2 = odeint(emotionsPair2, state0, t)
emotionsSol3 = odeint(emotionsPair3, state3, t)
emotionsSol4 = odeint(emotionsPair4, state4, t1)
emotionsSol5 = odeint(emotionsPair5, state4, t)

p.figure()
p.plot(t, emotionsSol1)
p.axhline(0, color='black')
p.axis([0, 10, -0.2, 0.5])
p.xlabel('Time')
p.legend(('ReactionRomeo', 'HappinessRomeo', 'ReactionJulliet', 'HappinessJulliet'))
p.savefig('Increasing Love.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(emotionsSol1[:, 0], emotionsSol1[:, 2])
p.axis([-1, 1, -1, 1])
p.axhline(0, color='black')
p.axvline(0, color='black')
p.xlabel('Romeo')
p.ylabel('Julliet')
ax = p.gca()  # uncomment for arrows
i = 0
while i < len(t) - 300:
    arr = p.Arrow(emotionsSol1[:, 0][i], emotionsSol1[:, 2][i], emotionsSol1[:, 0][i + 100] - emotionsSol1[:, 0][i],
                  emotionsSol1[:, 2][i + 100] - emotionsSol1[:, 2][i], edgecolor="white", width=0.15)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 250 + 50 / (1 + i)
p.savefig('Increasing Love Parametric Arrow.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(t, emotionsSol2)
p.axhline(0, color='black')
p.axis([0, 10, -0.2, 0.2])
p.xlabel('Time')
p.legend(('ReactionRomeo', 'HappinessRomeo', 'ReactionJulliet', 'HappinessJulliet'))
p.savefig('Decreasing Love.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(emotionsSol2[:, 0], emotionsSol2[:, 2])
p.axis([-0.2, 0.2, -0.2, 0.2])
p.axhline(0, color='black')
p.axvline(0, color='black')
p.xlabel('Romeo')
p.ylabel('Julliet')
ax = p.gca()  # uncomment for arrows
i = 0
while i < len(t) - 120:
    arr = p.Arrow(emotionsSol2[:, 0][i], emotionsSol2[:, 2][i], emotionsSol2[:, 0][i + 50] - emotionsSol2[:, 0][i],
                  emotionsSol2[:, 2][i + 50] - emotionsSol2[:, 2][i], edgecolor="white", width=0.03)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 120
p.savefig('Decreasing Parametric Arrow.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(t, emotionsSol3)
p.axhline(0, color='black')
p.axis([0, 20, -0.1, 0.4])
p.xlabel('Time')
p.legend(('ReactionRomeo', 'HappinessRomeo', 'ReactionJulliet', 'HappinessJulliet'))
p.savefig('Standart Love.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(emotionsSol3[:, 0], emotionsSol3[:, 2])
p.axis([-0.3, 0.3, -0.3, 0.3])
p.axhline(0, color='black')
p.axvline(0, color='black')
p.xlabel('Romeo')
p.ylabel('Julliet')
ax = p.gca()  # uncomment for arrows
i = 0
while i < len(t) - 120:
    arr = p.Arrow(emotionsSol3[:, 0][i], emotionsSol3[:, 2][i], emotionsSol3[:, 0][i + 100] - emotionsSol3[:, 0][i],
                  emotionsSol3[:, 2][i + 100] - emotionsSol3[:, 2][i], edgecolor="white", width=0.05)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 120 + 0.5 * i
p.savefig('Standart Love Parametric.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(t1, emotionsSol4)
p.axhline(0, color='black')
p.axis([0, 200, -1, 20])
p.xlabel('Time')
p.legend(('ReactionRomeo', 'HappinessRomeo', 'ReactionJulliet', 'HappinessJulliet'))
p.savefig('Ignore Love Long Term.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(t1, emotionsSol4)
p.axhline(0, color='black')
p.axis([0, 10, -0.1, 0.24])
p.xlabel('Time')
p.legend(('ReactionRomeo', 'HappinessRomeo', 'ReactionJulliet', 'HappinessJulliet'))
p.savefig('Ignore Love Short Term.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(emotionsSol4[:, 0], emotionsSol4[:, 2])
p.axis([-1, 10, -1, 15])
p.axhline(0, color='black')
p.axvline(0, color='black')
p.xlabel('Romeo')
p.ylabel('Julliet')
ax = p.gca()  # uncomment for arrows
i = 1000
while i < len(t1) - 4000:
    arr = p.Arrow(emotionsSol4[:, 0][i], emotionsSol4[:, 2][i], emotionsSol4[:, 0][i + 300] - emotionsSol4[:, 0][i],
                  emotionsSol4[:, 2][i + 300] - emotionsSol4[:, 2][i], edgecolor="white", width=1)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 350
p.savefig('Ignore Love Parametric.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(t, emotionsSol5)
p.axhline(0, color='black')
p.axis([0, 20, -0.1, 0.24])
p.xlabel('Time')
p.legend(('ReactionRomeo', 'HappinessRomeo', 'ReactionJulliet', 'HappinessJulliet'))
p.savefig('Ignore Love Flegmatic.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(emotionsSol5[:, 0], emotionsSol5[:, 2])
p.axis([-0.1, 0.1, -0.1, 0.25])
p.axhline(0, color='black')
p.axvline(0, color='black')
p.xlabel('Romeo')
p.ylabel('Julliet')
ax = p.gca()  # uncomment for arrows
i = 0
while i < len(t) - 8000:
    arr = p.Arrow(emotionsSol5[:, 0][i], emotionsSol5[:, 2][i], emotionsSol5[:, 0][i + 50] - emotionsSol5[:, 0][i],
                  emotionsSol5[:, 2][i + 50] - emotionsSol5[:, 2][i], edgecolor="white", width=0.02)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 60 + (1 + 0.1 * i)
p.savefig('Ignore Love Flegmatic Parametric.png', dpi=300)  #  uncomment to save plots
p.show()
