
'''
PROBLEM 2:
SOLVE   x' = x+y
	y' = 4x-2y
'''
import numpy as np
import matplotlib.pyplot as plt
import math_tool as mt
x0 = 10
y0 = 1
tf = 10.
c = np.array((-1,1,4,-2))
u = np.array((x0,y0))
n_step = 1000
h = tf/n_step
x_plot = np.zeros(n_step)
y_plot = np.zeros(n_step)
t_plot = np.zeros(n_step)
t = 0
def slope_func(t,u,c):
	u_dot = np.zeros(2)
	u_dot[0] = c[0]*u[0]+c[1]*u[1]
	u_dot[1] = c[2]*u[0]+c[3]*u[1]
#	print u_dot
	return u_dot



for i in range(n_step):
	x_plot[i] = u[0]
	y_plot[i] = u[1]
	t_plot[i] = t+h*i
	u = mt.rk4(t,u,c,slope_func,h)
	print h

plt.plot(t_plot,x_plot,t_plot,y_plot)
plt.show()


