# ----------- Import statements ------------

import math;
import numpy;
import matplotlib.pyplot as plt;

# ------------ Custom functions ------------

# A-F sums
def A(xlist, ylist, y_uncert):
    A = 0;
    for i in range(len(xlist)):
        A += xlist[i] / (y_uncert[i])**2;
    return A;

def B(xlist, ylist, y_uncert):
    B = 0;
    for i in range(len(xlist)):
        B += 1.0 / (y_uncert[i])**2;
    return B;

def C(xlist, ylist, y_uncert):
    C = 0;
    for i in range(len(xlist)):
        C += ylist[i] / (y_uncert[i])**2;
    return C;

def D(xlist, ylist, y_uncert):
    D = 0;
    for i in range(len(xlist)):
        D += (xlist[i])**2 / (y_uncert[i])**2;
    return D;

def E(xlist, ylist, y_uncert):
    E = 0;
    for i in range(len(xlist)):
        E += (xlist[i]) * (ylist[i]) / (y_uncert[i])**2;
    return E;

def F(xlist, ylist, y_uncert):
    F = 0;
    for i in range(len(xlist)):
        F += (ylist[i])**2 / (y_uncert[i])**2;
    return F;

# chi-square
def s_m(xlist, ylist, y_uncert, a, b):
    s_m = 0;
    for i in range(len(xlist)):
        s_m += (ylist[i] - a*xlist[i] - b)**2 / (y_uncert[i])**2;
    return s_m;

# average y-value
def avg(alist):
    avg = 0;
    for i in range(len(alist)):
        avg += ylist[i];
    return avg;

# coefficient of determination (r^2)
def r2(xlist, ylist, y_uncert, a, b, y_avg):
    r2 = 0;
    num = 0;
    denom = 0;
    for i in range(len(xlist)):
        num += (a*xlist[i] + b - y_avg)**2;
        denom += (ylist[i] - y_avg)**2;
    r2 = num / denom;
    return r2;

# ------------ Hardcode section ------------

# Hardcode these values
xlist = [65, 75, 85, 95, 105];
x_uncert = [];

ylist = [-20, 17, 42, 94, 127];
y_uncert = [1, 1, 1, 1, 1];

# -------------- Main program --------------

# Calculate average y-value
y_avg = avg(ylist);

# Assign the A-F sum values to variables A-F
A = A(xlist, ylist, y_uncert);
B = B(xlist, ylist, y_uncert);
C = C(xlist, ylist, y_uncert);
D = D(xlist, ylist, y_uncert);
E = E(xlist, ylist, y_uncert);
F = F(xlist, ylist, y_uncert);

# y = ax + b is the best-fit line
a = (B*E - A*C) / (B*D - A*A)
b = (C*D - A*E) / (B*D - A*A)

# Calculate chi-square
s_m = s_m(xlist, ylist, y_uncert, a, b);
# Calculate degrees of freedom
ndf = len(xlist) - 2;        # 2 parameters: a,b
# Calculate closeness of fit (should be as close to 1 as possible)
fit = s_m / ndf;

# Calculate coefficient of determination r^2 and r
r2 = r2(xlist, ylist, y_uncert, a, b, y_avg);
if (a > 0):
    r = math.sqrt(r2);
else:
    r = -math.sqrt(r2);

# ------------ Console output  -------------

# Print the linear regression model
print('T = ' + str(b) + ' + ' + str(a) +'P');       # equation y=ax+b
print("A = " + str(b));                             # a-value
print("B = " + str(a));                             # b-value
print("S_m = " + str(s_m) + " (chi-square)");       # chi-square
print("ndf = " + str(ndf));                         # degrees of freedom
print("S_m/ndf = " + str(fit));                     # closeness of fit (chi-square)
print("p-value ~ 0 due to large S_m");              # p-value
print("coeff. of determ.: r^2 = " + str(r2));       # coefficient of determination
print("correlation coeff.: r = " + str(r));         # correlation coefficient
print("\n");
print("Absolute zero (accepted): -273.15 C");       # theoretical value of absolute zero
print("Absolute zero (fitted): " + str(b) + " C");  # experimental value of absolute zero

# ------------- File output  ---------------

f = open("shi_homework05_results.txt", "w+")

# Print the linear regression model
f.write('T = ' + str(b) + ' + ' + str(a) +'P' + "\n");       # equation y=ax+b
f.write("A = " + str(b) + "\n");                             # a-value
f.write("B = " + str(a) + "\n");                             # b-value
f.write("S_m = " + str(s_m) + " (chi-square)" + "\n");       # chi-square
f.write("ndf = " + str(ndf) + "\n");                         # degrees of freedom
f.write("S_m/ndf = " + str(fit) + "\n");                     # closeness of fit (chi-square)
f.write("p-value ~ 0 due to large S_m" + "\n");              # p-value
f.write("coeff. of determ.: r^2 = " + str(r2) + "\n");       # coefficient of determination
f.write("correlation coeff.: r = " + str(r) + "\n");         # correlation coefficient
f.write("\n");
f.write("Absolute zero (accepted): -273.15 C" + "\n");       # theoretical value of absolute zero
f.write("Absolute zero (fitted): " + str(b) + " C" + "\n");  # experimental value of absolute zero

f.close();

# ------------ Plotting output -------------

# Set parameters for plot
print("range of x-values: [" + str(min(xlist)) + " , " + str(max(xlist)) + "]");
print("range of y-values: [" + str(min(ylist)) + " , " + str(max(ylist)) + "]");

print("Enter min and max for axes of plot:");
xmin = float(input("xmin: "));
xmax = float(input("xmax: "));
ymin = float(input("ymin: "));
ymax = float(input("ymax: "));

equation = 'y=' + str(a) + 'x+' + str(b);

# Plot the axes and labels (need to hardcode xlabel and ylabel)
plt.title("Temperature vs Pressure");
plt.xlabel("P (mm Hg)");
plt.ylabel("T (degrees C)");
plt.axis([xmin, xmax, ymin, ymax]);
# Plot the data points
plt.plot(xlist, ylist, 'ro');
# Plot the best-fit line
x = numpy.linspace(xmin,xmax,100);
y = a*x+b;
plt.plot(x, y, '-r', label=equation);
plt.legend(loc='upper left');

plt.show();
