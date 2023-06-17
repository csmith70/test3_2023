import numpy as np
import sympy as sy
from sympy import symbols, diff
# creates a function of x^2*sin(x)
x = np.linspace(-1, 1, 30)
x = symbols('x')
fx = (x ** 2) * sy.sin(x)
# Take the derivative of function w.r.t x
rslt = diff(fx ** 2, x)
print('The derivative of the function w.r.t x is: ', rslt)
