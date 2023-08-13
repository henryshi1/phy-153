# L7Ex3.py
# Henry Shi
# Calculates sin(x)+2cos(x) for x of 10 degrees, 20 degrees

from math import sin, cos, radians;

def sin_plus_2_cos(x):
    y = sin(x) + 2.0*cos(x);
    return y;

x1 = radians(10.);
print(sin_plus_2_cos(x1));      # calculate for 10 degrees
x2 = radians(20.);
print(sin_plus_2_cos(x2));      # calculate for 20 degrees
