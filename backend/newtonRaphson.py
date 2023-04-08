import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
from sympy import sympify, lambdify, symbols,diff

# Function to calculate the root using the Newton-Raphson method


def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    """
    Encuentra una raíz de la función `f` utilizando el método de Newton-Raphson, comenzando en `x0`.

    Args:
        f (callable): Una función que toma un número y devuelve un número.
        f_prime (callable): La derivada de `f`.
        x0 (float): El punto de partida para la iteración.
        tol (float): La tolerancia para la convergencia.
        max_iter (int): El número máximo de iteraciones permitidas.

    Returns:
        float: Un número que es una raíz de `f` cercana a `x0`.

    Raises:
        ValueError: Si el método no converge después de `max_iter` iteraciones.

    """

    iteraciones = []
    x = x0

    for i in range(max_iter):
        fx = f(x)
        fx_prime = f_prime(x)
        x_next = x - fx / fx_prime
        error = abs(x_next - x)
        iteraciones.append({"x0": x,  "raiz": x_next, "error": error})
        if abs(x_next - x) < tol:
            return x_next, iteraciones
        x = x_next

    raise ValueError(
        f"El método de Newton-Raphson no converge después de {max_iter} iteraciones")


# Function graficar
def graficar (f,a,b,x0, raiz):
    x = np.linspace(a, b, 1000)
    y = f(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name='f(x)'))
    fig.add_trace(go.Scatter(x=[x0], y=[f(x0)], mode='markers', name='x0'))
    fig.add_trace(go.Scatter(x=[raiz], y=[f(raiz)], mode='markers', name='raiz'))
    fig.update_layout(title='Método de Newton-Raphson', xaxis_title='x', yaxis_title='f(x)')
    
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


def main():
    try:
        # Title
        st.title("Método de Newton-Raphson")
        # Input equation // 588.6 * exp(-x/6) + 40 *x - 588.6 problema fisica
        equation_str = st.text_input("Ecuación", "(sin(x)/x) + cos(1+x**2) - 0.25")

        # Input a and b
        a = st.number_input("Valor inicial a", value=-10.0)
        b = st.number_input("Valor inicial b", value=10.0)

        # Input initial values
        x0 = st.number_input("Valor inicial x0", value=1.0)

        # Read equation
        f = read_equation(equation_str)

        # Calculate derivative
        x = symbols('x')
        f_prime = lambdify(x, diff(sympify(equation_str), x))

    except:
        # Print error message
        st.warning("Error: Incorrectos los datos a evaluar.")
        return

    # Create button to calculate the root
    if st.button("Calcular"):

        # Create try except to catch errors
        try:
            # Calculate root approximation
            raiz, iteraciones = newton_raphson(f, f_prime, x0=x0)

            # Print success message
            st.success("La raíz es {} después {} iteraciones.".format(
                raiz, len(iteraciones)))
        except:
            # Print error message
            st.warning("Error: Defina correctamente los datos a evaluar.")
            return

        # Create table with iterations
        columnas = ["Iteración", "x0", "raiz", "f(raiz)", "error"]
        datos = []

        for i, iteracion in enumerate(iteraciones):
            datos.append([i+1, iteracion["x0"], iteracion["raiz"],
                         f(iteracion["raiz"]), abs(iteracion["error"])])
        tabla_df = pd.DataFrame(datos, columns=columnas)

        # Graficar
        graficar(f,a,b,x0, raiz)
        # expander
        expander = st.expander("Tabla de iteraciones")

        # Show table
        expander.table(tabla_df)
