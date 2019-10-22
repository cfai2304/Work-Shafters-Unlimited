# initial conditions and parameters
dt = 0.001		# time n interval
C_eg_init = 2.0	# initial concentration of alcohol in the gastro tract
C_eb_init = 0.0	# initial concentration of alcohol in the bloodstream 
t_final = 11	# Time in hours 
k_1 = 10.0
k_2 = 0.192

N = int(t_final/dt)
import numpy as np
import matplotlib.pyplot as plt
C_eg = np.zeros(N)	
C_eb = np.zeros(N)	
# setup the initial conditions
C_eg[0] = C_eg_init
C_eb[0] = C_eb_init
t = np.zeros(N)

# equation to calculate the concentration of ethanol in the gastrointestinal tract
def C_ethanol_gastro(t, C_eg, C_eb): 
	return -1.0 * k_1*C_eg
# equation to calculate the concentration of ethanol in the bloodstream 
def C_ethanol_blood(t, C_eg, C_eb):
	return k_1*C_eg-k_2

_t = 0.0	# initial step is at t=0 
for n in range(1,N):	# g through each step n = [1,N-1]
	C_eg[n] = C_eg[n-1] + dt * C_ethanol_gastro(t[n-1],C_eg[n-1],C_eb[n-1])
	C_eb[n] = C_eb[n-1] + dt * C_ethanol_blood(t[n-1],C_eg[n-1],C_eb[n-1])

	_t = _t + dt; 
	t[n] = _t;

plt.plot(t, C_eg) 
plt.plot(t, C_eb) 
plt.xlabel('t')
plt.ylabel('C')
plt.show()
print(y)
print(t)

