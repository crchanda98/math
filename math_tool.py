#	SELF DEFINED MATH FUNCTIONS


#	RK FOR DE SOLVE
def rk4(x,y,c,func,h):	
	k1 = h*func(x,y,c)
	k2 = h*func(x+h/2,y+k1/2,c)
	k3 = h*func(x+h/2,y+k2/2,c)
	k4 = h*func(x+h,y+k3,c)
	ynext = y+(k1+2*k2+2*k3+k4)/6
	return ynext
def rk1(x,y,c,func,h):	
	k1 = h*func(x,y,c)
	ynext = y+k1
	return ynext

# 	TRAPIZOIDAL RULE FOR INTEGRATION
def trapiz(x,y):
	m = x.size
	n = y.size
	if m==n:
		area = 0
		for i in range(m-1):
			area = area+0.5*(x[m+1]-x[m])*(y[m+1]+y[m])

