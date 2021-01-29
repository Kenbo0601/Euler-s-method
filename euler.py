#testing branch

# Numerical Solutions to 1st-Order ODE via Euler's Method

# Importing External Libraries
import numpy as np
from matplotlib import pyplot as plt
import math
from Equation import Expression

# Defining Basic Data
eq = input("Enter the equation (dy/dt) : ")
x0 = float(input('Enter the initial t-value: '))
y0 = float(input('Enter the initial y-value: '))
xf = float(input('Enter the final t-value: '))
k = int(input('Number of steps: '))

# Step size
deltax = (xf - x0) / k

# Define t-values
x = np.linspace(x0, xf, k+1)
# For loop for the updated t-value
for i in range(k+1):
    x[i] = x0 + i * deltax

# Initializing array for the slope (dy/dt = m) and y-values
m = np.zeros([k+1])
y = np.zeros([k+1])

# python equation interpreter
fn = Expression(eq, ["x", "y"])

# For loop for the updated y-value
y[0] = y0
print('-----------------------')
print('t\ty\tf(t,y)')
print('-----------------------')
for i in range(1, k+1):
    m[i-1] = fn(x[i-1], y[i-1])
    y[i] = y[i-1] + m[i-1] * deltax  # y_new = y_old + (slope)*(step size)

# Printing the data
for i in range(k+1):
    print('%.4f\t%.4f\t%0.4f' % (x[i], y[i], m[i]))
    print('-----------------------')

# Plotting the solution
plt.plot(x, y, linestyle='-', marker='o')
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Approximate solution with Euler's Method")
plt.show()
