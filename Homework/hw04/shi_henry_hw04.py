import numpy;
import math;

# List of values
xlist = [-10, -0.01, 20, 30, 45, 101, 0.5]; # x-values
ylist = [];                                 # y-values
uncertainties_f = [];                       # uncertainties in y-values
variance_ylist = [];                        # list of variances in y-values

# ------------------ Part 1 ------------------

s_f2 = 0;                   # Variance in f
s_f = 0;                    # Uncertainty in f

# Define a few custom functions
def f(x):
    return 2.0 * math.exp(-x/2.0)

def df_dx(x):               # df/dx where f(x) = 2exp(-x/2)
    return -math.exp(-x/2.0);

def s_x(x):                 # uncertainty of x where s_x/x = 0.10
    return 0.10*x;

# Calculate variance in f
for i in range(len(xlist)):
    x = xlist[i];                           # current x-value

    # Append the corresponding f(x) value
    ylist.append(f(x));

    # Calculate and append variance
    sigma_f2 = (df_dx(x))**2 * (s_x(x))**2; # variance of current f(x), (sigma_f)^2
    variance_ylist.append(sigma_f2);        # append to the variance list

    # Calculate uncertainty
    sigma_f = math.sqrt(sigma_f2);          # uncertainty of current f, sigma_f

    # Append to the list of uncertainties, rounding digits accordingly
    if (sigma_f > 0.001):
        uncertainties_f.append(round(sigma_f,4));
    elif (sigma_f > 1.0e-5):
        uncertainties_f.append(round(sigma_f,9));
    elif (sigma_f > 1.0e-7):
        uncertainties_f.append(round(sigma_f,11));
    elif (sigma_f > 1.0e-10):
        uncertainties_f.append(round(sigma_f,14));
    elif (sigma_f > 1.0e-21):
        uncertainties_f.append(round(sigma_f,25));
    else:
        uncertainties_f.append(sigma_f);

print("Uncertainties on f: " + str(uncertainties_f));

# ------------------ Part 2 ------------------

# Convert original lists into arrays
xarray = numpy.array(xlist);
yarray = numpy.array(ylist);                    # values of f
variance_yarray = numpy.array(variance_ylist);  # variances in f

# Find the numerator of average
num_array = numpy.divide(yarray, variance_yarray);
avg_num = numpy.sum(num_array);

# Find the denominator of average
denom_array = numpy.reciprocal(variance_yarray);
avg_denom = numpy.sum(denom_array);

# Calculate average
average = avg_num / avg_denom

# Calculate overall uncertainty
variance = 1.0 / avg_denom
uncertainty = math.sqrt(variance)

# Print results for part 2
print("Average: " + str(round(average,26)) + " +/- " + str(round(uncertainty, 25)));
