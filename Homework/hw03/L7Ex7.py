# L7Ex7.py
# Henry Shi

from math import *;

# Variable dictionary
L = 0.9295;             # length,                   meters
sigma_L = 0.0015;       # uncertainty of length,    meters
T = 1.936;              # period,                   seconds
sigma_T = 0.004;        # uncertainty of period,    seconds

# Note: T = 2pi* sqrt(L/g)
# therefore, g = (4pi^2 * L) / (T^2)
def g(L,T):
    g = (4*(pi**2)*L) / (T**2);
    return g;
def sigma_g(L,T,sigma_L,sigma_T):
    sigma_g = sqrt( ((4*pi**2)/(T**2))**2 * sigma_L**2 + ((8*(pi**2)*L)/(T**3))**2 * sigma_T**2);
    return sigma_g;

# print results
g = g(L,T);
sigma_g = sigma_g(L,T,sigma_L,sigma_T);
print("g = " + str(round(g,4)) + "+/-" + str(round(sigma_g,4)) + " m/s^2");
