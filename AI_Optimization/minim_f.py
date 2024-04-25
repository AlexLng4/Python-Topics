import numpy as np
from matplotlib import pyplot as plt


def gradient_descent(fnc, der_fnc, learning_rate, initial_guess, iterations):
    x = initial_guess

    for i in range(iterations):
        gradient = der_fnc(x)
        x = x - learning_rate * gradient

    return x


def fnc(x):
    return 5*x*x - x + 2


def der_fnc(x):
    return 10*x - 1

learning_rate = 0.1
initial_guess = 0.0
iterations = 1000
x = np.linspace(-10, 10, 100)
plt.plot(x, fnc(x), color='red')

minimum = gradient_descent(fnc, der_fnc, learning_rate, initial_guess, iterations)
min_value = fnc(minimum)

print(f"The minimum value of the function is {min_value} at x = {minimum}")
plt.plot(minimum,min_value,'o')

plt.show()


