specific_humidity = 14.4
h = specific_humidity/1000 # humidity as defined in the theory
H_g_out = 60 # enthalpy of air leaving
H_g_in = 38 # enthalpy of air entering
T_l_out = 28 # temperature of the water out
H_0 = 67 # reference enthalpy
T_0 = 25 # reference temp
latent_heat = 2401 #latent heat of evapo of water
N = 100
G = 0.42 # gas flow rate
C_l = 4.18 # heat capacity of liquid water
L = 0.004877 # water flow rate


def dH_g (N): # eq 2.23
	return (H_g_out - H_g_in)/(N-1)

def _T_l(H_g_z): # eq 2.26 (for T_l(z))
	# enthalpy at height z
	return  T_l_out -( G* ( H_g_in - H_g_z )/( C_l * L ) )

def _H_star (T): # eq 2.6 (for H*)
	C_g = 1.005 + 1.88 * h # units of h = [kg water vapor / kg dry air ] # eq 2.7
	return (H_0 + C_g *(T - T_0)) + latent_heat * h


def f_H_g(H_star, _H_g):
	return (1/(H_star - _H_g))


H_g = [None]*N
T_l = [None]*N
H_star = [None]*N

H_g[0] = H_g_in
T_l[0] = T_l_out
H_star[0] = _H_star(T_l[0])



# create the table
for n in range (1,N): # [1,99]
	H_g[n] = H_g[n-1] + dH_g(N)
	T_l[n] = _T_l(H_g[n])
	H_star[n] = _H_star(T_l[n])
	print(H_g[n], "," , T_l[n],",", H_star[n])

# apply the trapezoidal rule to determine the integral eq2.20
sum = 0
for k in range(1, N-1):
	fun_H_g_k = (1/(H_star[k] - H_g[k]))
	fun_H_g_k_plus1 = (1/(H_star[k+1] - H_g[k+1]))
	trap = ( fun_H_g_k + fun_H_g_k_plus1 )/2.0 * dH_g(N)
	sum += trap


print("Sum = n_OG: " , sum)




