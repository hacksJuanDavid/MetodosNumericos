import numpy as np
import streamlit as st
from sympy import *
import plotly.graph_objects as go

# Create a function read the equation


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

# Function to calculate the integral using Simpson 3/8


def simpson38(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            s += 2 * f(a + i * h)
        else:
            s += 3 * f(a + i * h)
    return (3 * h / 8) * s

# Function to calculate the integral


def calcular_integral(f, a, b, n):
    # Comprobación de número de particiones par
    if n % 3 != 0:
        n += 1
        st.warning(
            "El número de particiones debe ser un número par. Se ajustó a {}.".format(n))

    # Cálculo de la integral
    integral = simpson38(f, a, b, n)
    return integral

# Function to calculate the error


def calcular_error(f, a, b, n):
    # Cálculo del error
    h = (b - a) / n
    cuarta_derivada = np.max(np.abs(np.gradient(np.gradient(
        np.gradient(np.gradient(f(np.linspace(a, b, 1000))))))))
    # Cálculo del error
    # error = (-3/80) * (h**5) * cuarta_derivada * a + (b - a) * np.random.rand()
    error = (-3/80) * (h**5) * cuarta_derivada * (b - a)
    return error


# Function to plot


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

    # Configuración del gráfico
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
    fig.update_layout(
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='white',
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='white',
        )
    )
    # Configurar el tamaño del gráfico
    fig.update_layout(width=800, height=600)
    # Configurar el layout de la figura
    y_range = [np.min(y), np.max(y)]
    fig.update_layout(
        xaxis=dict(range=[-10, 10]),
        yaxis=dict(range=y_range)
    )

    return fig

# Function to plot 2


def graficar2(f, a, b, n):
    # Crear el arreglo de puntos en el intervalo de integración
    x = np.linspace(a, b, 1000)
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

# Create main function


def main():
    # try and except
    try:
        # Instrucciones de uso
        instrucciones_simpson38 = """
            <h1>Instrucciones de uso: Integración Simpson 3/8</h1>

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
        st.sidebar.markdown(instrucciones_simpson38, unsafe_allow_html=True)

        # Title
        st.title("Método de Simpson 3/8")
        # Equation
        equation_str = st.text_input(
            "Ecuación", "pi*((exp(x) - pi ) / (exp(x)) + pi * cos(x/2))**2")
        # Limits
        a = st.number_input("Extremo izquierdo", value=0.0)
        b = st.number_input("Extremo derecho", value=1.0)
        # Partitions
        n = st.number_input("Número de particiones MAX(999)", value=6)
        # Read the equation
        f = read_equation(equation_str)

        # parse the equation to latex
        equation_str = latex(sympify(equation_str))

        # Print integral in LaTeX format
        st.markdown("## Integral")
        st.markdown(
            f"La integral es :${a}$ to ${b}$ a ${equation_str}$ es:")
        st.markdown(f"$$\\int_{{{a}}}^{{{b}}} {equation_str} \\, dx$$")

        # n => 999
        if n > 999:
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

    except:
        st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                }
                </style>
                """, unsafe_allow_html=True)
        st.markdown(
            f'<h1 class="big-font">Error: La ecuación no es válida</h1>', unsafe_allow_html=True)
        return

    # Create a button to calculate the integral
    if st.button("Calcular"):
        # try and except
        try:
            # Calculate the integral
            integral = calcular_integral(f, a, b, n)
            # Calculate the error
            error = calcular_error(f, a, b, n)

            # Plot the function
            fig = graficar(f, a, b, n)
            st.plotly_chart(fig, use_container_width=True)

            # Plot the function 2
            # fig2 = graficar2(f, a, b, n)
            # st.plotly_chart(fig2, use_container_width=True)

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


# Run the main function
if __name__ == "__main__":
    main()
