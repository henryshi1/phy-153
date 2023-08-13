# L7Ex4.py
# Henry Shi

from math import *;

a = 2.0;                    # a = 2 is a constant

def f(x):                   # f(x) = a*sqrt(x)
    y = a*sqrt(x);
    return y;

print(f(10.56));            # should both print 6.499
print(a*sqrt(10.56));
