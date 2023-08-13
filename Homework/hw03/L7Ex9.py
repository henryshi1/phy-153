# L7Ex9.py
# Henry Shi

from math import *;

def getMinAndMax(list):
    x=max(list);
    y=min(list);
    print(x,y);                         # should print (33, -10)
    return x,y;

xList = [10, 21, 33, 9, -10];
xListMax, xListMin = getMinAndMax(xList);
print(xListMin,xListMax);               # should print (-10, 33)
