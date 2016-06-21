__author__ = 'Danny'
from scipy.integrate import odeint
import numpy
import pylab as p
import math

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


t = p.arange(0, 100, 0.01)
state0 = [0.1, 0, 0.1, 0]
emotionsSol1 = odeint(emotionsPair1, state0, t)
emotionsSol2 = odeint(emotionsPair2, state0, t)

p.figure()
p.plot(t, emotionsSol1)
p.axhline(0, color='black')
p.axis([0, 10, -0.2, 0.5])
p.xlabel('Time')
p.legend(('ReactionRomeo', 'HappinessRomeo', 'ReactionJulliet', 'HappinessJulliet'))
p.savefig('Increasing Love.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(t, emotionsSol2)
p.axhline(0, color='black')
p.axis([0, 10, -0.2, 0.2])
p.xlabel('Time')
p.legend(('ReactionRomeo', 'HappinessRomeo', 'ReactionJulliet', 'HappinessJulliet'))
p.savefig('Decreasing Love.png', dpi=300)  #  uncomment to save plots
p.show()

# p.figure()
# p.plot(lotterySol[:, 0], lotterySol[:, 1])
# p.axis([-0.1, 0.2, -0.2, 0.2])
# p.axhline(0, color='black')
# p.axvline(0, color='black')
# p.xlabel('Reaction')
# p.ylabel('Happiness')
# p.savefig('Single PositiveEvent Parametric.png', dpi=300)  #  uncomment to save plots
# p.show()
#
# p.figure()
# p.plot(lotterySol[:, 0], lotterySol[:, 1])
# p.axis([-0.1, 0.2, -0.2, 0.2])
# p.axhline(0, color='black')
# p.axvline(0, color='black')
# p.xlabel('Reaction')
# p.ylabel('Happiness')
# ax = p.gca() #uncomment for arrows
# i = 0
# while i < len(t)*4/5:
#     arr = p.Arrow(lotterySol[:, 0][i], lotterySol[:, 1][i], lotterySol[:, 0][i+0.2*i] - lotterySol[:, 0][i], lotterySol[:, 1][i+0.2*i] - lotterySol[:, 1][i], edgecolor="white", width=0.02)
#     ax.add_patch(arr)
#     arr.set_facecolor('r')
#     i += 1 + 0.25*i
# p.savefig('Single PositiveEvent Parametric Arrow.png', dpi=300)  #  uncomment to save plots
# p.show()
