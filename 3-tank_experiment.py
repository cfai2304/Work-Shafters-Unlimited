"""
You should be able to open the data in excel if you pipe the data to a file. Here is how to do it.
use this command in your command prompt:
python solve_3_tank.py > outputdata.csv
If you get the error "python is not an internal or external command", add python to your environmental variables (search how to do this)
Im not sure if these diameters are exactly correct, we can change them later.
	Large tank internal diameter : 12.75 in
	Small tank internal diameter : 10.75 in
	pipe diameter = 0.75 in
"""

PI = 3.1416
k = 6.3    # frictional loss constant (k = 125 gives numbers close to our experiments) this has to be changed to account for the skin friction or whatever


#converts gallons to height IN INCHES of fluid in a tank given diameter IN INCHES
def galToH(gallons, diameter):
	diameterInFeet = diameter/12.0    # diameter in feet
	area = PI*(diameterInFeet/2.0)**2    # area in feet
	cubicFeetPerGal = 0.133681
	height = (gallons*cubicFeetPerGal/area)*12.0    #height in inches
	return height

#converts height IN INCHES to gallons of fluid given a diameter IN INCHES
def HtoGal(height, diameter):
	heightInFeet = height/12.0    # height in feet
	diameterInFeet = diameter/12.0    # diameter in feet
	area = PI*(diameterInFeet/2.0)**2    # area in feet
	volume = heightInFeet*area
	cubicFeetPerGal = 0.133681
	gal = volume/cubicFeetPerGal
	return gal

#returns the velocity in inches per second (eq 6 in theory)
def velocity_ij(h_i, h_j):
	g = 386.09    # acceleration of gravity in inches per second
	tmp = (2*g*abs(h_i-h_j)/k)**(1/2)    # the square root
	return abs(h_i-h_j)/(h_i-h_j)*tmp    # incorporating the sign function



# Diameters defined
D_large = 12.75
D_small = 10.75
D_pipe  = 0.75

# areas defined
A_pipe  = PI*(D_pipe/2.0)**2     # cross sectional area of pipe
A_large = PI*(D_large/2.0)**2    # cross sectional area of large tank
A_small = PI*(D_small/2.0)**2    # cross sectional area of large tank

# initial heights defined
H_0   = galToH(0.5, D_small)    #represents initial height of tank 2 or tank 3 (the smaller tanks)
H_1_0 = galToH(7.2, D_large)

# set up initial values
H_1 = H_1_0
H_2 = H_0
H_3 = H_0


t = 0.0    # time
dt = 0.5    # timestep
finalTime = 80    #  seconds until done doing calculations

# Add a header for our data
print(" time, gallons tank 1 , gallons tank 2 , gallons tank 3")

while t <= finalTime:

	# firstly determine the velocities
	v_12 = velocity_ij(H_1, H_2)    # velocity from tanks 1 to 2
	v_13 = velocity_ij(H_1, H_3)    # velocity from tanks 1 to 3

	# now lets determine the heights
	H_1 = H_1 - A_pipe/A_large*(v_12 + v_13)*dt
	H_2 = H_2 + A_pipe/A_small*(v_12)*dt
	H_3 = H_3 + A_pipe/A_small*(v_13)*dt

	# now lets print them in csv style, I formatted it such that it can be open in excel, just convert it to excel document when you open it in excel.
	print( t, ",", HtoGal(H_1, D_large),",", HtoGal(H_2, D_small),",", HtoGal(H_3, D_small))

	t += dt
