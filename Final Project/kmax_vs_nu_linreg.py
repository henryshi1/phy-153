# ----------- Import statements ------------

import math;
import numpy as np;
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
def s_m(xlist, ylist, y_uncert, slope, yint):
    s_m = 0;
    for i in range(len(xlist)):
        s_m += (ylist[i] - slope*xlist[i] - yint)**2 / (y_uncert[i])**2;
    return s_m;

# average y-value
def avg(alist):
    avg = 0;
    for i in range(len(alist)):
        avg += ylist[i];
    return avg;

# coefficient of determination (r^2)
# r^2 = 1 - SE_ypredicted / SE_yavg (standard errors calculated with respect to y_i)
def r2(xlist, ylist, y_uncert, slope, yint, y_avg):
    r2 = 0;
    num = 0;
    denom = 0;
    se1 = 0;
    se2 = 0;
    for i in range(len(xlist)):
        se1 = (slope*xlist[i] + yint - ylist[i])
        num += se1*se1;
        se2 = (ylist[i] - y_avg)
        denom += se2*se2;
    r2 = 1.0 - num / denom;
    return r2;

# --------------------------------------------------------
#              Obtain data from CSV file
# --------------------------------------------------------

import csv

# Menu of options
print("Choose a metal:")
print("1: Sodium (Na)")
print("2: Platinum (Pt)")
print("3: Silver (Ag)")
print("4: Potassium (K)")
print("5: Cesium (Cs)")

option = int(input(""))
print("Option " + str(option) + " selected")

# open files of data
if (option == 1):
    metal_file = open("sodium_data.csv","r")
elif (option == 2):
    metal_file = open("platinum_data.csv", "r")
elif (option == 3):
    metal_file = open("silver_data.csv", "r")
elif (option == 4):
    metal_file = open("potassium_data.csv", "r")
elif (option == 5):
    metal_file = open("cesium_data.csv", "r")
else:
    exit("Invalid option. Please enter an integer from 1 to 5.\n")

# create arrays of values
nu = []                  # frequency nu (10^14 Hz)
kmax = []                # Kmax (eV)
sigma_kmax = []          # uncertainty in Kmax (eV)

nline = 0 # current line number
with metal_file as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for line in readCSV:
        if nline > 0:
            nu.append(float(line[0]))
            kmax.append(float(line[1]))
            sigma_kmax.append(float(line[2]))
        nline += 1
        
# trim the headers from each list
#del na_nu[:1]
#del na_kmax[:1]
#del na_sigma_kmax[:1]


metal_file.close()

# --------------------------------------------------------
#       Calculate and plot linear regression models
# --------------------------------------------------------

# assign the arrays of data to x- and y-coordinate lists
xlist = np.array(nu)
ylist = np.array(kmax)
y_uncert = np.array(sigma_kmax)

# Assign the A-F sum values to variables A-F
A = A(xlist, ylist, y_uncert);
B = B(xlist, ylist, y_uncert);
C = C(xlist, ylist, y_uncert);
D = D(xlist, ylist, y_uncert);
E = E(xlist, ylist, y_uncert);
F = F(xlist, ylist, y_uncert);

# y = ax + b
slope = (B*E - A*C) / (B*D - A*A)
yint = (C*D - A*E) / (B*D - A*A)
# Uncertainties in slope and y-intercept
sigma_slope2 = B / (B*D-A*A)
sigma_slope = math.sqrt(sigma_slope2)
sigma_yint2 = D / (B*D-A*A)
sigma_yint = math.sqrt(sigma_yint2)

# Calculate average y-value
y_avg = avg(ylist);

# Calculate chi-square
s_m = s_m(xlist, ylist, y_uncert, slope, yint);
# Calculate degrees of freedom
ndf = len(xlist) - 2;        # 2 parameters: a,b
# Calculate closeness of fit (should be as close to 1 as possible)
fit = s_m / ndf;

# Calculate coefficient of determination r^2 and r
r2 = r2(xlist, ylist, y_uncert, slope, yint, y_avg);
if (slope > 0):
    r = math.sqrt(r2);
else:
    r = -math.sqrt(r2);


# ------------ Plotting output -------------

# Set parameters for plot
print("range of x-values: [" + str(min(xlist)) + " , " + str(max(xlist)) + "]");
print("range of y-values: [" + str(min(ylist)) + " , " + str(max(ylist)) + "]");

# Range of plot
xmin = 0.0
xmax = 1.2*max(xlist)
ymin = 0.0
ymax = 1.2*max(ylist)

# Display the equation and r-value
ndec = 6;       # Number of decimal places to display
equation = ( "y = " + str(round(slope,ndec)) + "x" + " + " + str(round(yint,ndec))
            + "\n" + "h = " + str(round(slope,ndec)) + r"$\times 10^{-14}$ eV s"
            + "\n" + r"$\sigma_h = $" + str(round(sigma_slope,ndec+5)) + r"$\times 10^{-14}$ eV s"
            + "\n" + "W = " + str(round(-yint,ndec)) + " eV"
             + "\n" + r"$\sigma_W = $" + str(round(sigma_yint,ndec)) + " eV"
            + "\n" + r"$r^2 = $" + str(round(r2,ndec+5))
            + "\n" + "ndf = " + str(ndf)
            + "\n" + r"$\chi^2 = $" + str(round(s_m,ndec))
#            + "\n" + r"$\chi^2/ndf = $" + str(round(fit,ndec))
             )

print(equation)

# Annotate each point
#for x,y in zip(xlist,ylist):
#    label = "(" + "{:.3f}".format(x) + ", " + "{:.3f}".format(y/1e6) + "*10^6)"
#    plt.annotate(label, # this is the text
#                 (x,y), # this is the point to label
#                 textcoords="offset points", # how to position the text
#                 xytext=(0,8), # distance from text to points (x,y)
#                 ha='center') # horizontal alignment can be left, right or center

# Generate the title based on the option you picked
if (option == 1):
    plt.title(r"$K_{max}$ vs frequency $\nu$ (Sodium)")
elif (option == 2):
    plt.title(r"$K_{max}$ vs frequency $\nu$ (Platinum)")
elif (option == 3):
    plt.title(r"$K_{max}$ vs frequency $\nu$ (Silver)")
elif (option == 4):
    plt.title(r"$K_{max}$ vs frequency $\nu$ (Potassium)")
elif (option == 5):
    plt.title(r"$K_{max}$ vs frequency $\nu$ (Cesium)")

# Plot the axes and labels (need to hardcode xlabel and ylabel)
plt.xlabel(r"frequency $\nu$ $(10^{14} s^{-1})$");
plt.ylabel(r"$K_{max}$ (eV)");
plt.axis([xmin, xmax, ymin, ymax]);

# Plot the data points
plt.scatter(xlist, ylist, c='k');


#plt.errorbar(xlist, ylist, xerr=x_uncert, yerr=y_uncert, fmt='none', ecolor='black');

# Plot the best-fit line
x = np.linspace(xmin,xmax,100);
y = slope*x + yint;
plt.plot(x, y, 'black', label=equation);
plt.legend(loc='upper left');

plt.show();
