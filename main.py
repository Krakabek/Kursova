__author__ = 'Danny'
from scipy.integrate import odeint
from pylab import * # for plotting commands

def romeo_juliet(state,t):
  x = state[0]
  y = state[1]
  a = 0.1
  b =  0.1
  c = 0.1
  d = 0.1
  dx = x*a + b*y
  dy = c*x + d*y
  return [dx,dy]

t = arange(0,500,1)
state0 = [0,0]

state = odeint(romeo_juliet,state0,t)

figure()
plot(t,state)
ylim([-8,8])
xlabel('Time')
ylabel('feelings')
legend(('Romeo','Juliet'))
title('Romeo and Juliet relations')
show()