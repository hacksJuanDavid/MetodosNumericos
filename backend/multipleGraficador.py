import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import streamlit as st
from sympy import *
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

# Function multipleGraficador


def multipleGraficador(f, g, h, j, a, b):
    # Crear un objeto de subplots
    fig = make_subplots(rows=1, cols=1)

    # Crear los trazos para cada función
    x = np.linspace(a, b, 1000)
    traces = []
    for func, name in zip([f, g, h, j], ['Función f(x)', 'Función g(x)', 'Función h(x)', 'Función j(x)']):
        if func:
            traces.append(go.Scatter(x=x, y=func(x), mode='lines', name=name))
    # Agregar los trazos al objeto de subplots
    for trace in traces:
        fig.add_trace(trace)

    # Configurar el diseño del gráfico
    fig.update_layout(title='Multiple graficador de funciones',
                      xaxis_title='x',
                      yaxis_title='y')

    # Congifurar el diseño de los ejes
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='white')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='white')
    # Configurar el tamaño del gráfico
    fig.update_layout(width=800, height=600)

    # Mostrar el gráfico st
    st.plotly_chart(fig, use_container_width=True)
# Function main


def main():
    st.title("Multiple graficador de funciones")
    st.markdown("""
        Este es un ejemplo de un gráfico de múltiples funciones.
        """)
    st.subheader(
        "Deben ser minimo 2 funciones para que se pueda usar el graficador multiple.")
    st.text("Por el momento solo se pueden graficar 4 funciones.")
    st.error("Tener en cuenta que va salir un error pero es mientras lo arreglo que es para manejar los vacios en los inputs.")

    # Leer las ecuaciones
    f_str = st.text_input("Ecuación f(x)", "x**2")
    g_str = st.text_input("Ecuación g(x)", "x**3")
    h_str = st.text_input("Ecuación h(x)", "sin(x)")
    j_str = st.text_input("Ecuación j(x)", "cos(x)")

    # Convertir las ecuaciones en funciones
    f = read_equation(f_str)
    g = read_equation(g_str)
    h = read_equation(h_str)
    j = read_equation(j_str)

    # Leer los límites del eje x
    a = st.number_input("Límite inferior de a", value=-10.0)
    b = st.number_input("Límite superior de b", value=10.0)

    # Create a button graficar
    if st.button("Graficar"):
        # Verificar si se han proporcionado al menos dos funciones
        if f and g:
            multipleGraficador(f, g, h, j, a, b)
        else:
            st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                }
                </style>
                """, unsafe_allow_html=True)
            st.markdown(
                '<h1 class="big-font">Error: Se deben proporcionar al menos dos funciones</h1>', unsafe_allow_html=True)


if __name__ == '__main__':
    main()
