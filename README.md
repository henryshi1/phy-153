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

Implemented Lecture 7 examples 1-7 in Python. `See Homework/hw03` for assignment description `PHY153_HW03.pdf`, Lecture 5 slides `PHY153_Lecture05.pdf`, Lecture 7 slides `PHY153_Lecture07.pdf`, and Python code files. Created the following files:

* `L7Ex1.py` - Math.py Module, Trigonometry, Exponents, Square Root, Math Constants

* `L7Ex2.py` - Module Import, Trigonometry

* `L7Ex3.py` - Write a code that calculates sin(x)+2cos(x) for x of 10 degrees and of 20 degrees, in a user defined function with argument x.

* `L7Ex4.py` - $A=2$ is a constant. Write a code to calculate values of a function $f(x)$ for $x=10.56$ in 2 ways: with a user-defined function and without.

$$f(x) = A\sqrt{x}$$

* `L7Ex5.py` - $A=2$ is a constant. Write a code to calculate values of a function $f(x)$ for $x=10.56$ in 2 ways: with a user-defined function and without. Add uncertainty calculation, assuming $\sigma_x / x = 0.10$.

$$f(x) = A\sqrt{x}$$

* `L7Ex6.py` - **Lecture 5**, textbook problem **3.14**.

    A visitor to a castle measures the depth of a well by dropping a stone and
timing its fall. She finds the time to fall is $t=3.0 \pm 0.5$ s and calculates
depth $d=gt^2/2$. What is her conclusion (numerical value of $d$ and its uncertainty), if she takes
  * a) $g=9.80\ m/s^2$ with negligible uncertainty
  * b) $g=9.81 \pm 0.2\ m/s^2$

* `L7Ex7.py` - **Lecture 5**, textbook problem **3.9**

    Pendulum experiment. Find $g$ and its uncertainty (error propagation):
$$l = 92.95 \pm 0.15\ cm$$
$$T = 1.936 \pm 0.004\ s$$
$$T = 2\pi\sqrt{\frac{l}{g}}$$

  * Use error propagation formula:
$$\sigma_f^2 = \left( \frac{\partial f}{\partial x_1} \right)^2 \sigma_{x1}^2 + \left( \frac{\partial f}{\partial x_2} \right)^2 \sigma_{x2}^2 + \dots + \left( \frac{\partial f}{\partial x_n} \right)^2 \sigma_{xn}^2$$

* `L7Ex8.py` - In Python define a function that calculates an average of numbers from a given list. Call this function in the main part of your code for the following list of numbers: 10, 12, 19. Code trace it.

* `L7Ex9.py` - For a given list of numbers: 10, 21, 33, 9, -10

    Write a function that takes this list as an argument and returns two values from that list: monimal and maximal. Code trace it.

* `L7Ex10.py` - Consider the following height measurement results for a selected group of 35 people. (see `PHY153_Lecture07.pdf` in `Homework/hw03`)

Write a Python code (with 2 functions) to calculate (**and print**):

1. the range of the height values (max and min),
2. the mean height, its uncertainty (correctly round the result), and the value of standard deviation
What do these quantities (from 1 and 2) tell us about this group of people? (Give an answer in a print statement)

**Helpful formulae:**

$$\overline{x} = \frac{1}{n} \sum^n_{i=1} x_i \qquad s^2$$

# Homework 4

See `Homework/hw04` for assignment description `PHY153_HW04.pdf` and Python code. Implemented solutions in file `shi_henry_hw04.py`.

Use the `numpy` module functions `exp` and `divide`, define functions $f$ given below and their uncertainties $\sigma_f$ (using error propagation method). Formulae for $\sigma_f$ should be derived on paper, and its final form should be coded in python. $x$ values should be used as a list.

1. Calculate uncertainties $\sigma_f$ on $f(x) = 2 \exp(-x/2)$ for the following x values:
$$-10, -0.01, 20, 30, 45, 101, 0.5$$
Assume 10% uncertainty i.e. $\sigma_x/x = 0.10$.

2. Calculate a weighted average (using `numpy` and its functions instead of loops) of $f(x)$ for $x$ values given in part 1.

# Homework 5

See `Homework/hw05` for assignment description `PHY153_HW05.pdf`, Lecture 15 slides `PHY153_Lecture15.pdf`, and Python code. Implemented solutions in file `shi_homework05.py`. Results are given in `shi_homework05_results.txt`.

* Data

|   P \[mm Hg\]    | 65  | 75 | 85 | 95 | 105 |
|       ---        | --- | ---| ---| ---| --- |
| T \[$^\circ C$\] | -20 | 17 | 42 | 94 | 127 |
|     $\sigma$     |  1  | 1  | 1  | 1  |  1  |

* Functional form
$$T = A+BP$$

* Find:
  * $A, B$ (fit parameters and their uncertainties)
  * $s_m$, ndf, $s_m/ndf$, p-value
  * Give interpretation of a p-value
* Compare the known value for the absolute zero temperature ($-273.15 ^\circ C$) with the fitted parameter. How good is the agreement (or disagreement)? Quantify your answer by giving the corresponding p-value and its interpretation.

# Final Project

See `Final Project` for files.
* Data Files: `*.csv`
* Data Plots generated with Python: `*.png`
* Lab Report - LaTeX source file: `shi_phy153_final_project.tex`
* Lab Report - LaTeX compiled PDF: `shi_phy153_final_project.pdf`
