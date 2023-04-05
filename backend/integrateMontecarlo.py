import numpy as np
import plotly.graph_objects as go
import streamlit as st
from sympy import *
# INTEGRACIÓN POR EL MÉTODO DE MONTECARLO


# Create function integrate montecarlo
def integrate_montecarlo(f, a, b, n):
    """
    Calculate the integral of a function f in the interval [a, b] using the Monte Carlo method.
    """
    x = np.random.uniform(a, b, n)
    y = f(x)
    return (b - a) * np.mean(y)


# Create function plot


def plot(f, a, b, n):
    # Plot the function and the rectangles
    x = np.linspace(-10, 10, 100)
    y = f(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name="Function"))

    # Generate points that are below the function
    x_points = []
    y_points = []
    for i in range(n):
        xi = np.random.uniform(a, b)
        yi = np.random.uniform(0, f(xi))
        if yi <= f(xi):
            x_points.append(xi)
            y_points.append(yi)
        elif yi > f(xi):
            x_points.append(xi)
            y_points.append(yi)

    # Plot the points 1
    fig.add_trace(go.Scatter(x=x_points, y=y_points,
                  name="Points In", mode="markers"))

    # Plot the rectangles
    x_rect = [a, a, b, b]
    y_rect = [0, f(a), f(b), 0]
    fig.add_trace(go.Scatter(x=x_rect, y=y_rect, name="Rectangles",
                  fill="toself", fillcolor="rgba(0, 0, 255, 0.2)"))

    # Configure the background grid
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='white')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='white')

    return fig

# Create function read equation


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

# Create function main


def main():
    try:
        # Title
        st.title("Integración por el método de Montecarlo")
        # Equation
        equation_str = st.text_input("Ecuación", "x**2")
        # Limits
        a = st.number_input("Extremo izquierdo", value=0.0)
        b = st.number_input("Extremo derecho", value=1.0)
        # Partitions
        n = st.number_input("Número de particiones MAX(10000)", value=6)
        # Read the equation
        f = read_equation(equation_str)

        # parse the equation to latex
        equation_str = latex(sympify(equation_str))

        # Print integral in LaTeX format
        st.markdown("## Integral")
        st.markdown(
            f"La integral es :${a}$ to ${b}$ a ${equation_str}$ es:")
        st.markdown(f"$$\\int_{{{a}}}^{{{b}}} {equation_str} \\, dx$$")

        # n => 10000
        if n > 10000:
            st.markdown("""
                    <style>
                    .big-font {
                        font-size:20px !important;
                        text-align: left;
                    }
                    </style>
                    """, unsafe_allow_html=True)
            st.markdown(
                f'<h1 class="big-font">Error: El numero de rectangulos no puede ser mayor a 999</h1>', unsafe_allow_html=True)
            return

    except Exception as e:
        error_type = type(e).__name__
        error_msg = str(e)
        print(f"Error: La ecuación no es válida. {error_type}: {error_msg}")

    # Calculate the integral
     # Create a button to calculate the integral
    if st.button("Calcular"):
        try:
            # Calculate the integral
            integral = integrate_montecarlo(f, a, b, n)

            # Plot the function
            fig = plot(f, a, b, n)
            st.plotly_chart(fig)

            # Print the result in LaTeX format
            st.markdown("## Resultado")
            st.markdown(
                f"$$\\int_{{{a}}}^{{{b}}} {equation_str} \\, dx = {integral:.8f}$$")

        except Exception as e:
            error_type = type(e).__name__
            error_msg = str(e)
            print(
                f"Error: La ecuación no es válida. {error_type}: {error_msg}")
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
            return


# Run the main function
if __name__ == "__main__":
    main()
