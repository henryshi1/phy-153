import numpy as np
import csv

# arrays of planck's constant and uncertainty
h_list = []            # planck's constant, in 10^-14 eV s
sigma_list = []        # uncertainty of planck's constant, in 10^-14 eV s

# -----------------------------------------------------------------------
#                        read in CSV file of data
# -----------------------------------------------------------------------

# open the csv file
hfile = open("h_data.csv", "r")

nline = 0              # current line number
with hfile as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # read each line of CSV file, append h and sigma values to arrays accordingly
    for line in readCSV:
        if nline > 0:  # only read in the lines after the header line
            h_list.append(float(line[1]))
            sigma_list.append(float(line[2]))
        nline += 1

# close file
hfile.close()

print(h_list)
print(sigma_list)

# -----------------------------------------------------------------------
#                      calculate the true value of h
# -----------------------------------------------------------------------

# initialize numerator and denominator of h, as well as variance
hnum = 0.0
hdenom = 0.0          # note: hdenom is the denominator of both h and sigma^2
h = 0.0
sigma2 = 0.0          # sigma^2 (variance)

# increment the numerator and denominator of h
for i in range(len(h_list)):
    hnum += h_list[i] / sigma_list[i]**2
    hdenom += 1.0 / sigma_list[i]**2

# calculate h
h = hnum / hdenom

# calculate sigma^2 and sigma
sigma2 = 1.0 / hdenom
sigma = np.sqrt(sigma2)

# -----------------------------------------------------------------------
#                        calculate f and p values
# -----------------------------------------------------------------------

# true value for planck's constant (10^-14 eV s)
htrue = 0.4134667696
sigmatrue = 0.0

f = (h - htrue) / (np.sqrt(sigma2 + sigmatrue**2))

# -----------------------------------------------------------------------
#                             print results
# -----------------------------------------------------------------------

print("hbest = (" + str(h) + "+/-"+ str(sigma) + ")*10^-14 eV*s")
print("f = " + str(f))
