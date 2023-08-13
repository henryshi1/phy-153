# L7Ex8.py
# Henry Shi

from math import *;

def average2(my_list):
    sum = 0.0;
    count = 0;
    for element in my_list:
        sum += element;
        count+=1;
    return sum/count;

xlist = [10.,12.,19,20.,56.,78.];
print(average2(xlist));                 # should print 32.5
