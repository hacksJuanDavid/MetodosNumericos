import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import numexpr as ne
from sympy import sympify, lambdify, symbols
def bisection(f, a, b, tolerance, max_iterations):
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

def regula_falsi(f, a, b, tolerance, max_iterations):
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

def solve_equation(method, f, a, b, tolerance, max_iterations=100):
    if method == "bisection":
        return bisection(f, a, b, tolerance, max_iterations)
    elif method == "regula_falsi":
        return regula_falsi(f, a, b, tolerance, max_iterations)
    else:
        return None, None, None, None

def read_equation(equation_str):
    """
    Parsea una cadena de texto con una ecuación y devuelve una función que la evalúa.
    """
    x = symbols('x')
    equation = sympify(equation_str)
    func = lambdify(x, equation)
    return func

def main():
    st.title("Root Finding Methods")

    # Sidebar
    st.sidebar.title("Settings")
    method = st.sidebar.selectbox("Method", ["Bisection", "Regula Falsi"])
    equation_str = st.sidebar.text_input("Equation", "sin(x)")
    a = st.sidebar.number_input("a", value=-10.0, step=0.1)
    b = st.sidebar.number_input("b", value=10.0, step=0.1)
    tolerance = st.sidebar.number_input("Tolerance", value=1e-6, step=1e-7)
    max_iterations = st.sidebar.number_input("Max iterations", value=100, step=1)

    # Main page
    st.header("Root Finding Method: {}".format(method))
    st.write("Find the root of the equation {} in the interval [a, b] using {} method.".format(equation_str, method))

    func = read_equation(equation_str)

    x = np.linspace(a, b, 1000)
    y = func(x)

    c, error, iterations, x_points, y_points = solve_equation(method.lower().replace(" ", "_"), func, a, b, tolerance, max_iterations)

    if c is None:
        st.warning("The method failed to converge.")
    else:
        st.success("The root is {:.6f} with an error of {:.6f} after {} iterations.".format(c, error, iterations))
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.plot(x_points, y_points, 'ro')
        ax.axhline(y=0, color='k')
        ax.axvline(x=c, color='k')
        st.pyplot(fig)
if __name__ == '__main__':
    main()
