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
    x = np.linspace(a, b, 100)
    y = f(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name="Function"))

    # Add title
    fig.update_layout(title_text="Integración por el método de Montecarlo")

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
    # Configurar el tamaño del gráfico
    fig.update_layout(width=800, height=600)

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

        # Instrucciones de uso
        instrucciones_montecarlo = """
            <h1>Instrucciones de uso: Integración Montecarlo</h1>

            <h2>Descripción</h2>
            <p>La integración es un concepto fundamental en el cálculo y se utiliza para calcular el área bajo una curva o la acumulación de una cantidad a lo largo de un intervalo. La integración permite encontrar el valor exacto o una aproximación de la integral de una función.</p>

            <h2>Procedimiento</h2>
            <p>A continuación se detalla el procedimiento general para realizar la integración:</p>
            <ol>
                <li>Las funciones disponibles son: +, -, *, /, ^, **,sin(x),cos(x),tan(x),sqrt(x),exp(x),log(x)</li>
                <li>Identifica la función para la cual deseas calcular la integral ingresala en el input correspodiente.</li>
                <li>Define los limites de integracion inferio y superio.</li>
                <li>Define el numero de particiones.</li>
                <li>Presiona el boton "Calcular" y te arrojara los resultados.</li>
            </ol>

            <h2>Consideraciones adicionales</h2>
            <p>El cálculo de integrales puede variar en complejidad dependiendo de la función y el método utilizado. Algunas funciones pueden requerir técnicas avanzadas, como la integración numérica o el uso de software especializado. Además, ten en cuenta las propiedades de las integrales, como la linealidad y la regla del valor medio del cálculo integral.</p>
        """
        st.sidebar.markdown(instrucciones_montecarlo, unsafe_allow_html=True)

        # Title
        st.title("Integración por el método de Montecarlo")
        # Equation
        equation_str = st.text_input("Ecuación", "log(x) + 12 / cos(x)")
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
            st.plotly_chart(fig, use_container_width=True)

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
