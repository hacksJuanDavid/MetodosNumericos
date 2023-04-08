import numpy as np
import streamlit as st
import plotly.graph_objects as go
from sympy import *

# Function to simpson 1/3


def simpson13(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            s += 2 * f(a + i * h)
        else:
            s += 4 * f(a + i * h)

    return (h / 3) * s 

# Function to calculate the integral


def calcular_integral(f, a, b, n):
    # Comprobación de número de particiones par
    if n % 2 != 0:
        n += 1
        st.warning(
            "El número de particiones debe ser un número par. Se ajustó a {}.".format(n))

    # Cálculo de la integral
    integral = simpson13(f, a, b, n)
    return integral

# Function to calculate the error


def calcular_error(f, a, b, n):
    # Cálculo del error
    h = (b - a) / n
    cuarta_derivada = np.max(np.abs(np.gradient(np.gradient(
        np.gradient(np.gradient(f(np.linspace(a, b, 1000))))))))
    # Cálculo del error
    #error = (-h**5 / 90) * cuarta_derivada * a + (b - a) * np.random.rand()
    error = (-h**5 / 90) * cuarta_derivada * (b - a)
    
    return error

# Function to plot the function


def graficar(f, a, b, n):
    # Graficar la función y los rectángulos
    x = np.linspace(a, b, 1000)
    y = f(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name="Función"))

    # Graficar los rectángulos
    h = (b - a) / n
    for i in range(n):
        x_rect = [a + i * h, a + i * h,
                  a + (i + 1) * h, a + (i + 1) * h]
        y_rect = [0, f(a + i * h), f(a + (i + 1) * h), 0]
        fig.add_trace(go.Scatter(x=x_rect, y=y_rect, name="Rectángulo {}".format(
            i), fill="toself", fillcolor="rgba(0,0,255,0.2)"))

    # Configuración del gráfico y grid de fondo
    fig.update_layout(
        title="Gráfica de la función y los rectángulos",
        xaxis_title="x",
        yaxis_title="y",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        )
    )
    # Configurar el grid de fondo
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='white')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='white')

    # Configurar el layout de la figura
    y_range = [np.min(y), np.max(y)]
    fig.update_layout(
        xaxis=dict(range=[-10, 10]),
        yaxis=dict(range=y_range)
    )

    return fig

# Function to plot the function 2


def graficar2(f, a, b, n):
    # Crear el arreglo de puntos en el intervalo de integración
    x = np.linspace(-10, 10, 1000)
    y = f(x)
    # Crear el arreglo de puntos para los rectángulos
    h = (b - a) / n
    x_rect = np.linspace(a, b - h, n)
    y_rect = f(x_rect)

    # Crear la figura y agregar las curvas y los rectángulos
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name="Función"))
    for i in range(n):
        fig.add_shape(type="rect",
                      xref="x", yref="y",
                      x0=x_rect[i], y0=0,
                      x1=x_rect[i]+h, y1=y_rect[i],
                      line=dict(color="RoyalBlue", width=1),
                      fillcolor="LightSkyBlue", opacity=0.5)
    # Add points rectangles
    fig.add_trace(go.Scatter(x=x_rect, y=y_rect, name="Puntos",
                             mode="markers", marker=dict(color="red", size=10)))

    # Configurar el título y los ejes
    fig.update_layout(
        title="Gráfica de la función y los rectángulos",
        xaxis_title="x",
        yaxis_title="y",
        font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"))

    # Configurar el grid de fondo
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='white')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='white')

    # Configurar el layout de la figura
    y_range = [np.min(y), np.max(y)]
    fig.update_layout(
        xaxis=dict(range=[-10, 10]),
        yaxis=dict(range=y_range)
    )

    return fig


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

# Function to run the app in streamlit


def main():
    try:
        # Title
        st.title("Método de Simpson 1/3")
        # Equation
        equation_str = st.text_input("Ecuación", "x**2")
        # Limits
        a = st.number_input("Extremo izquierdo", value=0.0)
        b = st.number_input("Extremo derecho", value=1.0)
        # Partitions
        n = st.number_input("Número de particiones MAX(999)", value=6)
        # Read the equation
        f = read_equation(equation_str)

        # n > 1000
        if n > 1000:
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

        # parse the equation to latex
        equation_str = latex(sympify(equation_str))

        # Print integral in LaTeX format
        st.markdown("## Integral")
        st.markdown(
            f"La integral es :${a}$ to ${b}$ a ${equation_str}$ es:")
        st.markdown(f"$$\\int_{{{a}}}^{{{b}}} {equation_str} \\, dx$$")

    except Exception as e:
        error_type = type(e).__name__
        error_msg = str(e)
        print(
            f"Error: La ecuación no es válida. {error_type}: {error_msg}")

    # Create button to calculate the integral
    if st.button("Calcular"):
        # Calculate the integral
        try:
            # Calculate the integral
            integral = calcular_integral(f, a, b, n)

            # Calculate the error
            error = calcular_error(f, a, b, n)

            # Plot the function
            fig = graficar(f, a, b, n)
            st.plotly_chart(fig)

            # fig2 = graficar2(f, a, b, n)
            # st.plotly_chart(fig2)

            # Show the result in LaTeX format
            st.markdown("## Resultado")
            st.markdown(
                f"$$\\int_{{{a}}}^{{{b}}} {equation_str} \\, dx = {integral}$$")
            st.markdown(f"$$Error = {error}$$")

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


if __name__ == "__main__":
    main()
