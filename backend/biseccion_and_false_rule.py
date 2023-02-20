import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
from sympy import sympify, lambdify, symbols

# Function to calculate the bisection method
def bisection(func, a, b, tolerance, max_iterations):
    # verificamos si los valores iniciales dan signos opuestos
    if func(a) * func(b) > 0:
        print("Error: Los valores de a y b deben tener signos opuestos.")
        return None, None, None, None
    
    # inicializamos las variables
    c = (a + b) / 2
    error = np.inf
    iterations = 0
    x_points = [a, b, c]
    y_points = [func(a), func(b), func(c)]
    
    # iteramos hasta que se cumpla la tolerancia o se alcance el máximo de iteraciones
    while error > tolerance and iterations < max_iterations:
        iterations += 1
        
        # elegimos el siguiente intervalo
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
        
        # actualizamos la aproximación
        c_prev = c
        c = (a + b) / 2
        
        # calculamos el error
        error = np.abs(c - c_prev)
        
        # guardamos los puntos para la tabla de iteraciones
        x_points.append(c)
        y_points.append(func(c))
    
    return c, error, iterations, x_points, y_points

# Function to calculate the false position method
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

# Function to calculate the root of an equation
def solve_equation(method, f, a, b, tolerance, max_iterations=100):
    if method == "bisection":
        return bisection(f, a, b, tolerance, max_iterations)
    elif method == "regula_falsi":
        return regula_falsi(f, a, b, tolerance, max_iterations)
    else:
        return None, None, None, None

# Function to read the equation
def read_equation(equation_str):
    """
    Parsea una cadena de texto con una ecuación y devuelve una función que la evalúa.
    """
    x = symbols('x')
    equation = sympify(equation_str)
    func = lambdify(x, equation)
    return func

# Function to display the app interface
def main():
    #title
    st.title("Root Finding Methods")

    #header
    st.header("Bisection and False Position Methods")

    # Inputs
    method = st.selectbox("Method", ["Bisection", "Regula Falsi"])
    equation_str = st.text_input("Equation", "sin(x)")
    a = st.number_input("a", value=-10.0, step=0.1)
    b = st.number_input("b", value=10.0, step=0.1)
    tolerance = st.text_input("Tolerance",value=0.0001)
    max_iterations = st.number_input("Max iterations", value=100, step=1)

    # tolerance 
    float_tolerance = float(tolerance)

    # Create button calcular
    if st.button("Calcular"):
        # page header
        st.header("Root Finding Method: {}".format(method))
        st.write("Find the root of the equation {} in the interval [a, b] using {} method.".format(equation_str, method))

        # read equation
        func = read_equation(equation_str)

        x = np.linspace(a, b, 1000)
        y = func(x)

        c, error, iterations, x_points, y_points = solve_equation(method.lower().replace(" ", "_"), func, a, b, float_tolerance, max_iterations)

        if c is None:
            st.warning("The method failed to converge.")
        else:
            st.success("The root is {:.6f} with an error of {:.6f} after {} iterations.".format(c, error, iterations))
            '''
            #matplotlib plot
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.plot(x_points, y_points, 'ro')
            ax.axhline(y=0, color='k')
            ax.axvline(x=c, color='k')
            st.pyplot(fig)
            '''
            # plotly plot
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, name="Function"))
            fig.add_trace(go.Scatter(x=x_points, y=y_points, mode="markers", name="Iterations"))
            fig.update_layout(title="Function and iterations", xaxis_title="x", yaxis_title="y")
            st.plotly_chart(fig)

            # Show iterations table
            expander = st.expander("Show iterations")
            # data table iterations,left,right,root,function value,error
            data = {'Left': x_points[:-1], 'Right': x_points[1:], 'Root': x_points[1:], 'Function Value': y_points[1:], 'Error': [np.nan] + [abs(x_points[i] - x_points[i-1]) for i in range(1, iterations)]}
            
            expander.write("The method uses the following formula to find the next approximation:")
            expander.table(pd.DataFrame.from_dict(data, orient='index').transpose())
    
if __name__ == '__main__':
    main()