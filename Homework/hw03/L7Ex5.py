# L7Ex5.py
# Henry Shi

from math import *;

# define constants A, B, C
a = 2.0;
b = 1.0;
c = 0.5;

def sigma_x(x):
    return 0.10 * x;
def sigma_y(y):
    return 0.25 * y;
def sigma_z(z):
    return 0.05 * z;

# Part a): f(x) and sigma_f(x)
def fx(x):                  # f(x) = Asqrt(x)
    fx = a * sqrt(x);
    return fx;
def sigma_fx(x):            # sigma_f(x) = (A*sigma_x) / (2sqrt(x))
    sigma_fx = abs(a * (sigma_x(x)) / (2*sqrt(x)));
    return sigma_fx;

# Part b): f(y) and sigma_f(y)
def fy(y):                  # f(y) = Be^(2Cy^2)
    fy = b * exp(2*c*y**2);
    return fy;
def sigma_fy(y):            # sigma_f(y) = Be^(2Cy^2) * 4Cy * sigma_y
    sigma_fy = fy(y) * 4.0 * c * y * sigma_y(y);
    return sigma_fy;

# Part c): f(x,y) and sigma_f(x,y)
def fxy(x,y):               # f(x,y) = (x-y)/(x+y)
    fxy = (x-y) / (x+y);
    return fxy;
def sigma_fxy(x,y):         # sigma_f(x,y) = 2*sqrt( (y*sigma_x)^2 + (x*sigma_y)^2 ) / (x+y)^2
    sigma_fxy = 2.0 * sqrt( (y * sigma_x(x))**2 + (x * sigma_y(y))**2 ) / (x+y)**2;
    return sigma_fxy;

# Part d): f(x,y,z) and sigma_f(x,y,z)
def fxyz(x,y,z):            # f(x,y,z) = (x+y+z)/sqrt(2)
    fxyz = (x+y+z) / sqrt(2.0);
    return fxyz;
def sigma_fxyz(x,y,z):      # sigma_f(x,y,z) = sqrt(sigma_x^2 + sigma_y^2 + sigma_z^2) / sqrt(2)
    sigma_fxyz = sqrt(sigma_x(x)**2 + sigma_y(y)**2 + sigma_z(z)**2) / sqrt(2.0);
    return sigma_fxyz;

# Part e): g(x) = 2sin(x) + 1
def gx(x):
    gx = 2.0*sin(x) + 1;    # g(x) = 2sin(x)+1
    return gx;
def sigma_gx(x):
    sigma_gx = abs(2.0*cos(x))*sigma_x(x);  # sigma_g(x) = |2cos(x)| * sigma_x
    return sigma_gx;

print("Constants: A=" + str(a) + ", B=" + str(b) + ", C=" + str(c) + "\n");

print("a) f(x) = Asqrt(x)");
x1 = 10.56;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) +
      ",\t\tf(x)=" + str(fx(x1)) + "+/-" + str(sigma_fx(x1)));
x1 = 30.0;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) +
      ",\t\tf(x)=" + str(fx(x1)) + "+/-" + str(sigma_fx(x1)));
x1 = 45.0;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) +
      ",\t\tf(x)=" + str(fx(x1)) + "+/-" + str(sigma_fx(x1)));
print("\n");

print("b) f(y) = Be^(2Cy^2)");
y1 = 0.0987;
print("For y=" + str(y1) + "+/-" + str(sigma_y(y1))
      + ",\tf(y)=" + str(fy(y1)) + "+/-" + str(sigma_fy(y1)));
y1 = 0.045;
print("For y=" + str(y1) + "+/-" + str(sigma_y(y1))
      + ",\t\tf(y)=" + str(fy(y1)) + "+/-" + str(sigma_fy(y1)));
y1 = 0.31;
print("For y=" + str(y1) + "+/-" + str(sigma_y(y1))
      + ",\t\tf(y)=" + str(fy(y1)) + "+/-" + str(sigma_fy(y1)));
print("\n");

print("c) f(x,y) = (x-y)/(x+y)");
x1 = 10.56; y1 = 0.0987;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) + " and y=" + str(y1) + "+/-" + str(sigma_y(y1))
      + ",\tf(x,y)=" + str(fxy(x1,y1)) + "+/-" + str(sigma_fxy(x1,y1)));
x1 = 10.56; y1 = 0.045;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) + " and y=" + str(y1) + "+/-" + str(sigma_y(y1))
      + ",\tf(x,y)=" + str(fxy(x1,y1)) + "+/-" + str(sigma_fxy(x1,y1)));
x1 = 10.56; y1 = 0.31;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) + " and y=" + str(y1) + "+/-" + str(sigma_y(y1))
      + ",\tf(x,y)=" + str(fxy(x1,y1)) + "+/-" + str(sigma_fxy(x1,y1)));
x1 = 30.0; y1 = 0.0987;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) + " and y=" + str(y1) + "+/-" + str(sigma_y(y1))
      + ",\tf(x,y)=" + str(fxy(x1,y1)) + "+/-" + str(sigma_fxy(x1,y1)));
x1 = 30.0; y1 = 0.045;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) + " and y=" + str(y1) + "+/-" + str(sigma_y(y1))
      + ",\t\tf(x,y)=" + str(fxy(x1,y1)) + "+/-" + str(sigma_fxy(x1,y1)));
x1 = 30.0; y1 = 0.31;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) + " and y=" + str(y1) + "+/-" + str(sigma_y(y1))
      + ",\t\tf(x,y)=" + str(fxy(x1,y1)) + "+/-" + str(sigma_fxy(x1,y1)));
x1 = 45.0; y1 = 0.0987;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) + " and y=" + str(y1) + "+/-" + str(sigma_y(y1))
      + ",\tf(x,y)=" + str(fxy(x1,y1)) + "+/-" + str(sigma_fxy(x1,y1)));
x1 = 45.0; y1 = 0.045;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) + " and y=" + str(y1) + "+/-" + str(sigma_y(y1))
      + ",\t\tf(x,y)=" + str(fxy(x1,y1)) + "+/-" + str(sigma_fxy(x1,y1)));
x1 = 45.0; y1 = 0.31;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) + " and y=" + str(y1) + "+/-" + str(sigma_y(y1))
      + ",\t\tf(x,y)=" + str(fxy(x1,y1)) + "+/-" + str(sigma_fxy(x1,y1)));
print("\n");

print("d) f(x,y,z) = (x+y+z)/sqrt(2)");
x1 = 10.56; y1 = 0.0987; z1 = 3.2 * 10.0**3;
print("For (" + str(x1) + "+/-" + str(sigma_x(x1)) + ", " + str(y1) + "+/-" + str(sigma_y(y1)) + ", " + str(z1) + "+/-" + str(sigma_z(z1))
      + "),\tf(x,y,z)=" + str(fxyz(x1,y1,z1)) + "+/-" + str(sigma_fxyz(x1,y1,z1)));
x1 = 30.0; y1 = 0.045; z1 = 54000.0;
print("For (" + str(x1) + "+/-" + str(sigma_x(x1)) + ", " + str(y1) + "+/-" + str(sigma_y(y1)) + ", " + str(z1) + "+/-" + str(sigma_z(z1))
      + "),\tf(x,y,z)=" + str(fxyz(x1,y1,z1)) + "+/-" + str(sigma_fxyz(x1,y1,z1)));
x1 = 45.0; y1 = 0.31; z1 = 65.789;
print("For (" + str(x1) + "+/-" + str(sigma_x(x1)) + ", " + str(y1) + "+/-" + str(sigma_y(y1)) + ", " + str(z1) + "+/-" + str(sigma_z(z1))
      + "),\tf(x,y,z)=" + str(fxyz(x1,y1,z1)) + "+/-" + str(sigma_fxyz(x1,y1,z1)));
print("\n");

print("e) g(x) = 2sin(x)+1");
x1 = 10.56;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) +
      ",\t\tg(x)=" + str(gx(x1)) + "+/-" + str(sigma_gx(x1)));
x1 = 30.0;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) +
      ",\t\tg(x)=" + str(gx(x1)) + "+/-" + str(sigma_gx(x1)));
x1 = 45.0;
print("For x=" + str(x1) + "+/-" + str(sigma_x(x1)) +
      ",\t\tg(x)=" + str(gx(x1)) + "+/-" + str(sigma_gx(x1)));
