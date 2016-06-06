__author__ = 'Danny'
from scipy.integrate import odeint
import pylab as p
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
    return [H, -b*H-R+F_Lottery(t)]

t = p.arange(0, 10, 0.01)
state0 = [0.001, 0.001]
state = odeint(emotionsLottery, state0, t)

p.figure()
p.plot(t, state)
p.ylim([-0.2, 0.2])
p.xlabel('Time')
p.legend(('H', 'R'))
p.title('Reaction to a single positive event')
p.savefig('Single PositiveEvent.png', dpi=96)  #  uncomment to save plots
p.show()
#
# p.figure()
# p.plot(state[:, 0], state[:, 1])
# p.ylim([-10, 1000])
# p.xlabel('Romeo')
# p.ylabel('Juliet')
# p.legend(('System state', ''))
# p.title('Romeo and Juliet relations')
#
# ax = p.gca() #uncomment for arrows
# i = 0
# while i < len(t)-10:
#     arr = p.Arrow(state[:, 0][i], state[:, 1][i], state[:, 0][i+1+0.05*i] - state[:, 0][i], state[:, 1][i+1+0.05*i] - state[:, 1][i], edgecolor="white", width=0.15)
#     ax.add_patch(arr)
#     arr.set_facecolor('r')
#     i += 1 + 0.1*i
#
# # p.savefig('XY_arr.png', dpi=96)  #  uncomment to save plots
# p.show()