from sympy import symbols, Eq, solve

# Define the variable
x = symbols('x')


from scipy.optimize import fsolve
import numpy as np

def equation_to_solve(x):
    return 1.13665 - (19.653 / 2.71828182845905**(19.653/x) + 3.08 / 2.71828182845905**(3.08/x)) / (2.71828182845905**(-19.653/x) + 2.71828182845905**(-3.08/x))

# Initial guess for the root
initial_guess = 1.0

# Solve the equation numerically
result = fsolve(equation_to_solve, initial_guess)

print("The solution for x is:", result)