# L7Ex10.py
# Henry Shi

from math import *;

def getMaxAndMin(my_list):
    low = min(my_list);
    high = max(my_list);
    return low,high;

def getN(my_list):
    count = 0;
    for entry in my_list:
        count += 1;
    return count;

def avg(my_list):
    total = 0.0;
    count = 0;
    for entry in my_list:
        total += entry;
        count += 1;
    avg = total / count;
    return avg;

def stdev(my_list):
    average = avg(my_list);
    n = getN(my_list);
    s2 = 0.0;
    for entry in my_list:
        s2 += (entry - average)**2
    s2 /= (n-1);
    return sqrt(s2);
def uncertainty(my_list):
    u = stdev(my_list) / sqrt(getN(my_list));
    return u;

xList = [168.4,165.7,166.8,170.1,169.8,169.2,168.8,
166.2,169.0,160.5,168.8,169.1,168.1,168.0,
166.7,168.8,169.9,170.9,169.6,168.2,167.4,
167.6,167.6,167.8,167.9,168.2,169.0,169.8,
170.6,170.8,169.3,167.6,166.2,163.6,163.8];
print("range: " + str(getMaxAndMin(xList)));
print("mean: " + str(avg(xList)));
print("uncertainty: " + str(uncertainty(xList)));
print("standard deviation: " + str(stdev(xList)));

print("\n" + "The uncertainty and standard deviation are low compared to the range, indicating the values are concentrated around the mean.");
