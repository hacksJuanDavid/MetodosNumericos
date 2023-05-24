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

# Function to calculate the secant method


def secant_method(f, x0, x1, tolerance=1e-6, max_iter=100):
    """
    Encuentra la raíz de la función f usando el método de la secante.

    Args:
        f (function): Función a la que se le buscará su raíz.
        x0 (float): Valor inicial para la iteración.
        x1 (float): Otro valor inicial para la iteración.
        tol (float, optional): Tolerancia para la convergencia. Por defecto es 1e-6.
        max_iter (int, optional): Número máximo de iteraciones. Por defecto es 100.

    Returns:
        float: Aproximación de la raíz de la función f.
    """
    iteraciones = []
    i = 0
    while i < max_iter:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        error = abs(x2 - x1)
        iteraciones.append({"x0": x0, "x1": x1, "raiz": x2, "error": error})
        if error < tolerance:
            return x2, iteraciones
        x0 = x1
        x1 = x2
        i += 1
    raise ValueError("La función no converge.")


# Function to plot the function
def plot_function(f, a, b, x0, x1, raiz):
    x = np.linspace(a, b, 1000)
    y = f(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name="Función"))
    fig.add_trace(go.Scatter(x=[x0], y=[f(x0)], mode="markers",
                             name="x0", marker=dict(size=10)))
    fig.add_trace(go.Scatter(x=[x1], y=[f(x1)], mode="markers",
                             name="x1", marker=dict(size=10)))
    fig.add_trace(go.Scatter(x=[raiz], y=[f(raiz)], mode="markers",
                             name="Raíz", marker=dict(size=10)))
    # Configurar el tamaño del gráfico
    fig.update_layout(width=800, height=600)

    fig.update_layout(
        title="Gráfica de la función",
        xaxis_title="x",
        yaxis_title="y",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        )
    )
    st.plotly_chart(fig, use_container_width=True)


def main():
    # Instructions de uso
    instructiones_metodo_secante = """
        <h1>Instrucciones de uso: Método de la Secante</h1>

        <h2>Descripción</h2>
        <p>El método de la secante es un algoritmo numérico utilizado para encontrar las raíces de una función no lineal. En lugar de utilizar una única recta tangente como en el método de Newton, el método de la secante utiliza una secante, es decir, una línea que pasa por dos puntos cercanos a la raíz deseada.</p>

        <h2>Procedimiento</h2>
        <p>A continuación se detalla el procedimiento para aplicar el método de la secante:</p>
        <ol>
            <li>Las funciones disponibles son: +, -, *, /, ^, **,sin(x),cos(x),tan(x),sqrt(x),exp(x),log(x)</li>
            <li>Elige dos puntos iniciales cercanos a la raíz deseada que serian x0 y x1.</li>
            <li>El intervalo [a, b] son valores de ajuste para la grafica</li>
            <li>La tolerancia debe ser un número positivo.</li>
            <li>Presiona el botón "Calcular".</li>
        </ol>

        <h2>Criterios de Convergencia</h2>
        <p>El método de la secante puede utilizar diferentes criterios de convergencia para determinar cuándo se ha alcanzado una solución satisfactoria. Algunos de los criterios comunes incluyen:</p>
        <ul>
            <li>Alcanzar una tolerancia o diferencia mínima entre dos aproximaciones sucesivas.</li>
            <li>Alcanzar un número máximo de iteraciones predefinidas.</li>
            <li>Comprobar si la función evaluada en la aproximación actual es suficientemente cercana a cero.</li>
        </ul>

        <h2>Consideraciones adicionales</h2>
        <p>El método de la secante puede requerir un número variable de iteraciones para converger a una solución, dependiendo de la función y los puntos iniciales seleccionados. Además, es posible que el método no converja si los puntos iniciales están demasiado lejos de la raíz o si hay singularidades en la función.</p>
    """
    st.sidebar.markdown(instructiones_metodo_secante, unsafe_allow_html=True)

    # Title
    st.title("Método de la Secante")
    # Input equation
    equation_str = st.text_input("Ecuación", "exp(-0.5*x) + 3.5*log(x) - 5.25")
    # Input initial a and b
    a = st.number_input("Valor inicial a", value=-10.0)
    b = st.number_input("Valor inicial b", value=10.0)
    # Input initial values
    x0 = st.number_input("Valor inicial x0", value=1.0)
    # Input initial values
    x1 = st.number_input("Valor inicial x1", value=3.0)
    # Input tolerance
    tolerance = st.text_input("Tolerancia", 0.0001)
    # Input max iterations
    # max_iter = st.number_input("Número máximo de iteraciones", 100)

    # Convert tolerance to float
    tolerance = float(tolerance)

    # Read equation
    f = read_equation(equation_str)

    # Create button to calculate the root
    if st.button("Calcular"):

        # Create try except to catch errors
        try:
            # Calculate root approximation
            raiz, iteraciones = secant_method(f, x0, x1, tolerance)

            # Print success message
            st.success("La raíz es {} después {} iteraciones.".format(
                raiz, len(iteraciones)))
        except:
            # Print error message
            st.warning("Error: Defina correctamente los datos a evaluar.")
            return

        # Create table with iterations
        columnas = ["Iteración", "x0", "x1", "raiz", "f(raiz)", "error"]
        datos = []
        for i, iteracion in enumerate(iteraciones):
            datos.append([i+1, iteracion["x0"], iteracion["x1"],
                         iteracion["raiz"], f(iteracion["raiz"]), abs(iteracion["error"])])
        tabla_df = pd.DataFrame(datos, columns=columnas)

        # Plot function
        plot_function(f, a, b, x0, x1, raiz)

        # expander
        expander = st.expander("Tabla de iteraciones")

        # Show table
        expander.table(tabla_df)


# Run main function
if __name__ == "__main__":
    main()
