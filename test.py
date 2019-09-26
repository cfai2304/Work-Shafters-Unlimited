import numpy as np
import matplotlib
#matplotlib.use("TkAgg")
import matplotlib.pylab as plot
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import tkinter as tk
#from tkinter import ttk
#import time
#import datetime
#import csv
#import os
#import import
#import hashtags

### IMPORTANT: This code solves ONE specific type of problem. You'll need to change the functions to solve other problems!

## Set number of space steps: More steps = more accuracy but also takes longer to finish calculating
M = 50000

## Change this to True if you want A + B <-> C and False if you want A + B -> C
do_equilibrium = False

## Parameters and stuff - set these to whatever you need
# THe program goes from W=0 to this W
MaxW = 3.5 * 1e-6 
dw = MaxW / M
k = 0.004 #[m^6 mol-1 s-1 kg-1]
Keq = 0.4 * 1e-3
v0 = 2.83 * 1e-7 #[m^3 s^-1]
Fa0 = 2 * 1e-5 # [mol/s]
eps = -0.5
P0 = 8.2 #Atm
alpha = 3.55 * 1e5 #[kg^-1]

## Arrays (Don't touch these)
w = np.linspace(0, MaxW, M+1)
X = np.zeros(M+1)
P = np.zeros(M+1)

def dxdw(n):
    if do_equilibrium:
        return k* ((Fa0 / (v0*v0)) * ((1 - X[n-1]) ** 2 / (1 + eps * X[n-1]) ** 2) * (P[n-1] / P0) ** 2 - (1/(Keq * v0)) * (X[n-1] / (1 + eps * X[n-1])) * (P[n-1] / P0))

    else: return k* ((Fa0 / (v0*v0)) * ((1 - X[n-1]) ** 2 / (1 + eps * X[n-1]) ** 2) * (P[n-1] / P0) ** 2)

def dpdw(n):
    return (-alpha / 2) * ((P0 ** 2) / P[n-1]) * (1 + eps * X[n-1])

P[0] = 8.2
X[0] = 0

for n in range(1, M + 1):
    X[n] = X[n-1] + dw * dxdw(n)
    P[n] = P[n-1] + dw * dpdw(n)


plot.clf()
plot.figure(1)
plot.plot(w * 1e6, X)
plot.title("X(W)")
plot.xlabel("W * 10^6 [kg]")
plot.ylabel("Conversion")
print("Final conversion:{}".format(X[-1]))
plot.figure(2)
plot.plot(w * 1e6, P)
plot.title("P(W)")
plot.xlabel("W * 10^6 [kg]")
plot.ylabel("Pressure [atm]")
print("Final pressure:{}".format(P[-1]))

plot.figure(3)
plot.plot(w * 1e6, Fa0 * (1 - X) * 1e5)
plot.title("Fa, Fb(w)")
plot.xlabel("W * 10^6 [kg]")
plot.ylabel("F * 10^5 [mol/s]")
plot.figure(4)
plot.plot(w * 1e6, Fa0 * X * 1e5)
plot.title("Fc(w)")
plot.xlabel("W * 10^6 [kg]")
plot.ylabel("F * 10^5 [mol/s]")
plot.show()
