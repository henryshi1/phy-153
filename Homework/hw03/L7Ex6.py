# L7Ex6.py
# Henry Shi

from math import *;

g = 9.80;                   # g=9.80 m/s^2

# d(t) = 0.5 * gt^2, where t in seconds, d in meters, g in m/s^2
def d(t):
    d = 0.5 * g * t**2;
    return d;
def sigma_d(t,sigma_t):
    sigma_d = g*t*sigma_t;
    return sigma_d;

# given parameters t=3.0 s and sigma_t = 0.5 s, calculate d(t) and sigma_d(t)
t = 3.0;
sigma_t = 0.5;

d = d(t);
sigma_d = sigma_d(t, sigma_t);
# print results
print("d = " + str(round(d,2)) + "+/-" + str(round(sigma_d,2)) + " m");
