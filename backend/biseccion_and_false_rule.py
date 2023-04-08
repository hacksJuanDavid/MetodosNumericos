import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
from sympy import sympify, lambdify, symbols

# Function to read the equation


def read_equation(equation_str):
    """
    Parsea una cadena de texto con una ecuación y devuelve una función que la evalúa.
    """
    try:
        x = symbols('x')
        equation = sympify(equation_str)
        func = lambdify(x, equation)
        return func
    except Exception as e:
        error_type = type(e).__name__
        error_msg = str(e)
        print(f"Error: La ecuación no es válida. {error_type}: {error_msg}")
        st.markdown("""
            <style>
            .big-font {
                font-size:20px !important;
                text-align: left;
            }
            </style>
            """, unsafe_allow_html=True)
        st.markdown(
            f'<h1 class="big-font">Error: La ecuación no es válida. {error_type}: {error_msg}</h1>', unsafe_allow_html=True)
        return None

# Function to calculate the bisection method


def bisection(f, a, b, tolerance=1e-6, max_iterations=100, safety_factor=1.5):
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

        # Convergence condition
        if error <= tolerance:
            break
        # Stop condition
        if iterations >= 2:
            last_error = abs(x[-1] - x[-2])
            if last_error <= tolerance * safety_factor:
                break

    return c, error, iterations, x, y

# Function to calculate the false rule method


def regula_falsi(f, a, b, tolerance=1e-6, max_iterations=100, safety_factor=1.5):
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

        # Convergence condition
        if error <= tolerance:
            break

        # Stop condition
        if iterations >= 2:
            last_error = abs(x[-1] - x[-2])
            if last_error <= tolerance * safety_factor:
                break

    return c, error, iterations, x, y

# Function to calculate the root of an equation


def solve_equation(method, f, a, b, tolerance, max_iterations=100):
    if method == "bisection":
        return bisection(f, a, b, tolerance, max_iterations)
    elif method == "regula_falsi":
        return regula_falsi(f, a, b, tolerance, max_iterations)
    else:
        return None, None, None, None


# Function graficar
def graficar(f, x_points, y_points, c , method):
    # plotly plot
    x = np.linspace(-10, 10, 1000)
    y = f(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name="f(x)"))
    fig.add_trace(go.Scatter(x=x_points, y=y_points,
                  mode="markers", name="iteraciones"))
    # point root
    fig.add_trace(go.Scatter(x=[c], y=[0], mode="markers", name="Raíz"))

    fig.update_layout(title=f"Método de {method}",
                      xaxis_title="x", yaxis_title="y")

    # Configurar el grid de fondo
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='white')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='white')

    # Configurar el layout de la figura
    y_range = [np.min(y), np.max(y)]
    fig.update_layout(
        xaxis=dict(range=[-10, 10]),
        yaxis=dict(range=y_range)
    )
    st.plotly_chart(fig)

# Function to display the app interface


def main():
    # title
    st.title("Métodos de búsqueda de raíces")

    # header
    st.header("Métodos de bisección y falsa posición")

    # subheader
    st.subheader(
        "Para tener en cuenta antes de usar la aplicación: \n 1. La ecuación debe ser una función de una variable. \n 2. El intervalo [a, b] debe contener una raíz. \n 3. La tolerancia debe ser un número positivo. \n 4. El número máximo de iteraciones debe ser un número entero positivo. \n 5. El método de bisección solo funciona para funciones continuas. \n 6. El método de falsa posición funciona para funciones continuas y discontinuas. \n 7. El método de falsa posición funciona mejor para funciones con raíces múltiples.")

    # Inputs
    method = st.selectbox("Método", ["Bisection", "Regula Falsi"])
    equation_str = st.text_input(
        "Ecuación", "sin(x)**2 - exp(-x**2) + 6*x**2 - 4")
    a = st.number_input("a", value=-10.0, step=0.1)
    b = st.number_input("b", value=10.0, step=0.1)
    tolerance = st.text_input("Tolerancia", value=0.0001)
    # max_iterations = st.number_input("Iteraciones máximas", value=100, step=1)

    # tolerance
    float_tolerance = float(tolerance)

    # Create button calcular
    if st.button("Calcular"):
        # Create try except equation validation
        try:
            # page header
            st.header("Método de búsqueda de raíces: {}".format(method))
            st.write("Encuentra la raíz de la ecuación {} en el intervalo [a, b] usando {} Método.".format(
                equation_str, method))

            # read equation
            func = read_equation(equation_str)

        except:
            st.warning("Error: La ecuación no es válida.")
            return

        # Create try except method solve_equation validation
        try:
            # calculate root
            c, error, iterations, x_points, y_points = solve_equation(
                method.lower().replace(" ", "_"), func, a, b, float_tolerance)
        except:
            st.warning("Error: El método no pudo converger.")
            return

        # display results and plot
        if c is None:
            st.warning("El método no pudo converger.")
        else:
            st.success("La raíz es {:.6f} con un error de {:.6f}  después {} iteraciones.".format(
                c, error, iterations))
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
            graficar(func, x_points, y_points, c, method)

            # Show iterations table
            expander = st.expander("Ver iteraciones")

            # data table iterations,a,b,f(a),f(b),root,f(r),error
            data = {'a': x_points[:-1], 'b': x_points[1:], 'f(a)': y_points[:-1], 'f(b)': y_points[1:], 'Root': x_points[1:], 'f(r)': y_points[1:], 'Error': [
                np.nan] + [abs(x_points[i] - x_points[i-1]) for i in range(1, iterations)]}

            expander.write(
                "El método utiliza la siguiente fórmula para encontrar la siguiente aproximación:")
            expander.table(pd.DataFrame.from_dict(
                data, orient='index').transpose())


if __name__ == '__main__':
    main()
