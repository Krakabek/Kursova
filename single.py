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
state0 = [0.001, 0.001]
lotterySol = odeint(emotionsLottery, state0, t)

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
p.legend(('Reaction', 'Happiness'))
p.title('Reaction to a single positive event')
# p.savefig('Single PositiveEvent.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(lotterySol[:, 0], lotterySol[:, 1])
p.axis([-0.1, 0.2, -0.2, 0.2])
p.axhline(0, color='black')
p.axvline(0, color='black')
p.xlabel('Reaction')
p.ylabel('Happiness')
# p.savefig('Single PossitiveEvent Parametric.png', dpi=300)  #  uncomment to save plots
p.show()

p.figure()
p.plot(lotterySol[:, 0], lotterySol[:, 1])
p.axis([-0.1, 0.2, -0.2, 0.2])
p.axhline(0, color='black')
p.axvline(0, color='black')
p.xlabel('Reaction')
p.ylabel('Happiness')
ax = p.gca() #uncomment for arrows
i = 0
while i < len(t)*4/5:
    arr = p.Arrow(lotterySol[:, 0][i], lotterySol[:, 1][i], lotterySol[:, 0][i+0.2*i] - lotterySol[:, 0][i], lotterySol[:, 1][i+0.2*i] - lotterySol[:, 1][i], edgecolor="white", width=0.02)
    ax.add_patch(arr)
    arr.set_facecolor('r')
    i += 1 + 0.25*i
p.savefig('Single PositiveEvent Parametric Arrow.png', dpi=300)  #  uncomment to save plots
p.show()