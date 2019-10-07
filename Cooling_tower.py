h = 0.98 # humidity as defined in the theory
H_g_out = 2 # enthalpy of air leaving
H_g_in 3 # enthalpy of air entering
T_l_out = 4 # temperature of the water out
H_0 = 234 # reference enthalpy
T_0 = 234 # reference temp


def dH_g (N): # eq 2.23
	return (H_g_out - H_g_in)/(N-1)

def _T_l(H_g_z): # eq 2.26 (for T_l(z))
	# enthalpy at height z
	return  T_l_out -( G* ( H_g_in - H_g_z )/( C_l * L ) )

def _H_star (T)# eq 2.6 (for H*)
	C_g = 1.005 + 1.88 * h # units of h = [kg water vapor / kg dry air ] # eq 2.7
	return (H_0)


def f_H_g(H_star, _H_g):
	return (1/(H_star - _H_g))



H_g = []
T_l = []
H_start = []

H_g[0] = H_g_in
T_l =



