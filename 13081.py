'''
PROBLEM 1
SOLVE MSD PROBLEM WITH VARIOUS BOUNDARY CONDITIONS

'''
import math_tool as mt
import numpy as np
import matplotlib.pyplot as plt
m =1.
b = 1.
k = 1.
c1 = 1.
x0 = 0.
v0 = 1.
tf = 10.
c = np.array((m,b,k,c1))
# BOUNDARY CONDITIONS
vel0 = np.linspace(-5,5,11)
dis0 = np.linspace(-5,5,11)
#def rk4(x,y,c,func,h):	
#	k1 = h*func(x,y,c)
#	ynext = y+k1
#	return ynext
def slope_func(t,u,c):
	slope = np.zeros(2)
	slope[0] = u[1]
	slope[1] = -b/m*u[1]-k/m*u[0]
	return slope


n_step = 100
t_span = np.linspace(0,tf,n_step)
h = t_span[1]-t_span[0]
dis_plot = np.zeros(n_step)
vel_plot = np.array(dis_plot)#np.zeros(n_step)
t_plot = np.array(dis_plot)
t = 0
for j in range(11):
	for k in range(11):
		u = np.array([dis0[j],vel0[i]])
		for i in range(n_step):
			u = mt.rk4(t,u,c,slope_func,h)
			dis_plot[i] = u[0]
			vel_plot[i] = u[1]
			t_plot[i] = t
			t = t+i*h

plt.plot(t_plot,x_plot)
plt.show()
