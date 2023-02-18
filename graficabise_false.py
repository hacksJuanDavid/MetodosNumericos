import numpy as np
import matplotlib.pyplot as plt

def f(x, equation):
    return eval(equation)

def bisection_method(f, a, b, tolerance, max_iterations):
    if f(a) * f(b) > 0:
        return None, None, None, None

    iterations = 0
    error = tolerance + 1
    x = []
    y = []
    while error > tolerance and iterations < max_iterations:
        c = (a + b) / 2
        error = abs(b - a)
        x.append(c)
        y.append(f(c))

        if f(c) == 0:
            error = 0
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1

    return c, error, iterations, x, y

def false_position_method(f, a, b, tolerance, max_iterations):
    if f(a) * f(b) > 0:
        return None, None, None, None

    iterations = 0
    error = tolerance + 1
    x = []
    y = []
    while error > tolerance and iterations < max_iterations:
        c = b - ((f(b) * (b - a)) / (f(b) - f(a)))
        error = abs(c - b)
        x.append(c)
        y.append(f(c))

        if f(c) == 0:
            error = 0
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1

    return c, error, iterations, x, y

def solve_equation(method, equation, a, b, tolerance, max_iterations=100):
    if method == 'Bisection':
        root, error, iterations, x, y = bisection_method(lambda x: f(x, equation), a, b, tolerance, max_iterations)
    elif method == 'False Position':
        root, error, iterations, x, y = false_position_method(lambda x: f(x, equation), a, b, tolerance, max_iterations)
    else:
        raise ValueError('Invalid method name')

    table_data = np.vstack((x[:iterations], y[:iterations], [error] * iterations)).T
    table_header = ['x', 'f(x)', 'Error']
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.set_title(method + ' Method')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    table = ax.table(cellText=table_data, colLabels=table_header, loc='bottom')

    return root, error, iterations, fig, table
