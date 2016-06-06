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
t1 = p.arange(0, 10, 0.01)
state0 = [0.001, 0.001]
lotterySol = odeint(emotionsLottery, state0, t)
drugsSol = odeint(emotionsDrugs, state0, t)

normal = numpy.random.normal(0, 1, 1000)


def F_Real(t):
    return normal[t * 100]


def emotionsReal(state, t):
    R = state[0]
    H = state[1]
    b = 2
    return [H, -b * H - R + F_Real(t)]


realSol = odeint(emotionsReal, state0, t1)

p.figure()
p.subplot(211)
p.plot([0.35], [1], 'ro')
p.axis([0, 15, 0, 2])
p.legend('F')
p.title('Positive event')
p.subplot(212)
p.plot(t, lotterySol)
p.axhline(0, color='black')
p.axis([0, 15, -0.2, 0.2])
p.xlabel('Time')
p.legend(('R', 'H'))
p.title('Reaction to a single positive event')
# p.savefig('Single PositiveEvent.png', dpi=96)  #  uncomment to save plots
p.show()

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
p.legend(('R', 'H'))
p.title('Reaction to a repetative positive event')
# p.savefig('Repetative PositiveEvent.png', dpi=96)  #  uncomment to save plots
p.show()

p.figure()
p.subplot(211)
p.plot(normal)
p.legend('F')
p.title('Events in life')
p.subplot(212)
p.plot(t1, realSol)
p.axhline(0, color='black')
p.ylim([-0.5, 0.5])
p.xlabel('Time')
p.legend(('R', 'H'))
p.title('Real life')
# p.savefig('Real Life.png', dpi=96)  #  uncomment to save plots
p.show()

