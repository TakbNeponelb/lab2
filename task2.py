import numpy as np
import scipy.optimize as opt

# Define function f(x)
def f(x):
    return x**4 - 10/3 * x**2 + 1
# Define function g(x)
def g(x):
    return x**4 - 6 * x**2 + 9

# Realise bissection method
def bisection_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        return None
    c = a
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c

# Find roots of f(x)=0 by  bissection's method
a = 0
b = 1
root1 = bisection_method(f, a, 0.4, tol=1e-10)  # first root from a to 0.4
root2 = bisection_method(f, 0.45, b, tol=1e-10)  # second root from 0.45 to b
print("First root f(x)=0 by bissection's method:", root1)
print("Second root f(x)=0 by bissection's method:", root2)

result = opt.root(f, [a,b])
# Display answer
print("Roots f(x)=0 by scipy.optimize.root():", result.x)

root1_g = bisection_method(g, a, b, tol=1e-10)  # first root from a to 0.4
print("Root g(x)=0 by bissection's method:", root1_g)

result_g = opt.root(g, [a,b])
# Display answer
print("Roots f(x)=0 by scipy.optimize.root():", result_g.x)
