__author__ = 'Danny'
from scipy.integrate import odeint
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3


def romeo_juliet(state, t):
    x = state[0]
    y = state[1]
    a = 0.5
    b = -2
    c = 1
    d = -1
    dx = x*a + b*y
    dy = c*x + d*y
    return [dx, dy]

t = p.arange(0, 30, 0.01)
state0 = [0.1, 0.1]
state = odeint(romeo_juliet, state0, t)

p.figure()
p.plot(t, state)
p.ylim([-0.15, 0.15])
p.xlabel('Time')
p.ylabel('feelings')
p.legend(('Romeo', 'Juliet'))
p.title('Romeo and Juliet relations')
# p.savefig('XY(t).png', dpi=96)  #  uncomment to save plots
p.show()

p.figure()
p.plot(state[:, 0], state[:, 1])
p.ylim([-0.15, 0.15])
p.xlabel('Romeo')
p.ylabel('Juliet')
p.legend(('System state', ''))
p.title('Romeo and Juliet relations')

# ax = p.gca() #uncomment for arrows
# i = 0
# while i < len(t)-10-3.5*i:
#     arr = p.Arrow(state[:, 0][i], state[:, 1][i], state[:, 0][i+10+0.05*i] - state[:, 0][i], state[:, 1][i+10+0.05*i] - state[:, 1][i], edgecolor="white", width=0.015)
#     ax.add_patch(arr)
#     arr.set_facecolor('r')
#     i += 50 + 0.1*i

# p.savefig('XY_arr.png', dpi=96)  #  uncomment to save plots
p.show()

fig = p.figure()
ax = p3.Axes3D(fig)
ax.plot_wireframe(state[:, 0], state[:, 1], t)
ax.set_xlabel('Romeo')
ax.set_ylabel('Juliet')
ax.set_zlabel('Time')
p.title('Romeo and Juliet relations')
# p.savefig('XYT', dpi=96)  #  uncomment to save plots
p.show()