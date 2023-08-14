# phy-153
PHY 153 (Fall 2019 - Spring 2020), Stony Brook University

Python scripts submitted for 4 Homework assignments and 1 Final project. Homework assignments in the **Homework** folder and final project in the **Final Project** folder.

# Homework 1

No code submitted for this assignment. Data given by `PHY153hw01data.csv` or `PHY153hw01data.xlsx` in folder `Homework/hw01`.

# Homework 2

Implemented Lecture 4 examples 1-6 in Python. `See Homework/hw02` for assignment description, Lecture 4 slides, and Python code files. Created the following files:

* `L4ex1.py` - Creating and Manipulating Lists, List Arithmetic, Accessing List Elements

* `L4ex2.py` - List and Loops, Accessing List Elements

* `L4ex3.py` - Lists and Loops, Code Tracing

* `L4ex4.py` - Lists and Loops, Appending to Lists

* `L4ex5.py` - Lists and Loops, Appending to Lists, Accessing List Elements

* `L4ex6.py` - Write a python code (a script) that does the following:

  * Create a list containing the given data:

    \[38.0, 34.5, 29.9, 28.6, 35.1, 37.3, 29.7, 32.5, 27.9, 36.5, 37.5, 40.9, 31.3, 24.7, 27.5, 39.9, 33.6, 31.3, 33.9, 40.0, 32.2, 30.5, 37.5, 25.6, 36.3, 35.7, 34.9, 41.4, 37.4, 29.5, 32.3, 34.1\]

  * Create a loop that goes over all values and calculates corresponding values in C degrees. 

$$C = \frac{5}{9} (F-32)$$

# Homework 3

Implemented Lecture 7 examples 1-7 in Python. `See Homework/hw03` for assignment description, Lecture 7 slides, and Python code files. Created the following files:

* `L7ex1.py` - Math.py Module, Trigonometry, Exponents, Square Root, Math Constants

* `L7ex2.py` - Module Import, Trigonometry

* `L7ex3.py` - Write a code that calculates sin(x)+2cos(x) for x of 10 degrees and of 20 degrees, in a user defined function with argument x.

* `L7ex4.py` - $A=2$ is a constant. Write a code to calculate values of a function $f(x)$ for $x=10.56$ in 2 ways: with a user-defined function and without.

$$f(x) = A\sqrt{x}$$

* `L7ex5.py` - $A=2$ is a constant. Write a code to calculate values of a function $f(x)$ for $x=10.56$ in 2 ways: with a user-defined function and without. Add uncertainty calculation, assuming $\sigma_x / x = 0.10$.

$$f(x) = A\sqrt{x}$$

* `L7ex6.py` - **Lecture 5**, textbook problem **3.14**.

    A visitor to a castle measures the depth of a well by dropping a stone and
timing its fall. She finds the time to fall is $t=3.0 \pm 0.5$ s and calculates
depth $d=gt^2/2$. What is her conclusion (numerical value of $d$ and its uncertainty), if she takes
  * a) $g=9.80\ m/s^2$ with negligible uncertainty
  * b) $g=9.81 \pm 0.2\ m/s^2$

* `L7ex7.py` - **Lecture 5**, textbook problem **3.9**

    Pendulum experiment. Find $g$ and its uncertainty (error propagation):
$$l = 92.95 \pm 0.15\ cm$$
$$T = 1.936 \pm 0.004\ s$$
$$T = 2\pi\sqrt{\frac{l}{g}}$$

  * Use error propagation formula:
$$\sigma_f^2 = \left( \frac{\partial f}{\partial x_1} \right)^2 \sigma_{x1}^2 + \left( \frac{\partial f}{\partial x_2} \right)^2 \sigma_{x2}^2 + \dots + \left( \frac{\partial f}{\partial x_n} \right)^2 \sigma_{xn}^2$$

# Homework 4

Use the numpy module functions: exp and divide define functions f given below and their uncertainties sf (using error propagation method). Formulae for sf should be derived on paper, and its final form should be coded in python. x values should be used as a list.

1. Calculate uncertainties sf on f (x) = 2 exp(-x/2) for the following x values:
$$-10, -0.01, 20, 30, 45, 101, 0.5$$
Assume 10% uncertainty i.e. $\sigma_x/x = 0.10$.

2. Calculate a weighted average (using numpy and its functions instead of loops) of f(x) for x values given in 1) 
