# 5.9x^3 + 22x^2 - 8x - 1 = 0
# eps = 10^-9

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
# Define function
def f(x):
    return 5.9 * x**3 + 22 * x**2 - 8 * x - 1

# Define derivative
def df(x):
    return 17.7 * x**2 + 44 * x - 8

x0 = -5
# Find root without derivative
root_no_derivative = opt.newton(f, x0, tol=1e-9, full_output= True)
print("Root without derivative x_0 = -5:", root_no_derivative)


# FInd root with derivative
root_with_corrected_derivative = opt.newton(f, x0, tol=1e-9, full_output= True, fprime=df)
print("Root with derivative x_0 = -5:", root_with_corrected_derivative)

print("==========================================================================")

x0 = -0.5
# Find root without derivative
root_no_derivative = opt.newton(f, x0, tol=1e-9, full_output= True)
print("Root without derivative x_0 = -0.5:", root_no_derivative)


# FInd root with derivative
root_with_corrected_derivative = opt.newton(f, x0, tol=1e-9, full_output= True, fprime=df)
print("Root with derivative x_0 = -0.5:", root_with_corrected_derivative)

print("==========================================================================")

x0 = 0.5
# Find root without derivative
root_no_derivative = opt.newton(f, x0, tol=1e-9, full_output= True)
print("Root without derivative x_0 = 0.5:", root_no_derivative)


# FInd root with derivative
root_with_corrected_derivative = opt.newton(f, x0, tol=1e-9, full_output= True, fprime=df)
print("Root with derivative x_0 = 0.5:", root_with_corrected_derivative)


# Create array X
x = np.linspace(-5, 2, 100)  # Choose segment by loсalization

# Create array Y
y = f(x)

# Plot figure
plt.plot(x, y, label='f(x) =  5.9x^3 + 22x^2 - 8x - 1')
plt.axhline(0, color='black', lw=0.5)  # Add Ox
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('curve f(x)')
plt.show()