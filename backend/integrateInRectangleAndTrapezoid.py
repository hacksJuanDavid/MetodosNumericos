import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sympy import *
from scipy.integrate import quad

# integrate in rectangle


def integrateInRectangle(f, a, b, n):
    # Calculate the integral using left endpoint rule
    h = (b - a) / n
    left_sum = 0
    for i in range(n):
        left_sum += f(a + i * h)

    # Calculate the integral using right endpoint rule
    right_sum = 0
    for i in range(1, n+1):
        right_sum += f(a + i * h)

    # Calculate the integral using midpoint rule
    midpoint_sum = 0
    for i in range(n):
        midpoint_sum += f(a + (i+0.5) * h)

    # Calculate the integral using default left endpoint rule
    default_sum = 0
    for i in range(1, n):
        default_sum += f(a + i * h)

    # Create list of rectangles coordinates
    rectangles = []
    for i in range(n):
        xa = a + i * h
        xb = xa + h
        ya_left = f(xa)
        ya_right = f(xb)
        ya_midpoint = f(xa + 0.5 * h)
        # Add rectangles to list
        rectangles.append(
            dict(
                type="rect",
                x0=xa, y0=0, x1=xb, y1=ya_left,
                line=dict(color="royalblue", width=2),
                fillcolor="rgba(65, 105, 225, 0.7)",
                opacity=1.0,
                name="Rectangulo izquierdo",
            )
        )
        rectangles.append(
            dict(
                type="rect",
                x0=xa, y0=0, x1=xb, y1=ya_right,
                line=dict(color="green", width=2),
                fillcolor="rgba(0, 128, 0, 0.7)",
                opacity=1.0,
                name="Rectangulo derecho"
            )
        )
        rectangles.append(
            dict(
                type="rect",
                x0=xa, y0=0, x1=xb, y1=ya_midpoint,
                line=dict(color="purple", width=2),
                fillcolor="rgba(147, 112, 219, 0.5)",
                opacity=0.7,
                name="Rectangulo medio"
            )
        )

    # Graficate the function and rectangles
    x = np.linspace(a, b, 1000)
    y = f(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name="f(x)"))
    fig.add_trace(go.Scatter(x=[a, b], y=[0, 0], name="Base"))
    fig.add_trace(go.Scatter(x=[a, a], y=[0, f(a)], name="Altura"))
    fig.add_trace(go.Scatter(x=[b, b], y=[0, f(b)], name="Altura"))

    # Add rectangles to figure
    fig.update_layout(shapes=rectangles)

    # Add title and axis names
    fig.update_layout(
        title="Gráfica de integracion rectangulo",
        xaxis_title="x",
        yaxis_title="y",
    )

    # Configurar el grid de fondo
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='white')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='white')

    # Configurar el tamaño del gráfico
    fig.update_layout(width=800, height=600)
    # Configurar el layout de la figura
    y_range = [np.min(y), np.max(y)]
    fig.update_layout(
        xaxis=dict(range=[-10, 10]),
        yaxis=dict(range=y_range)
    )

    # Configurar el color de fondo
    # fig.update_layout(plot_bgcolor='rgb(230, 230, 230)')

    # Create text box showing
    st.markdown("### Colores de los rectangulos:")
    st.markdown("#### Left endpoint rule: royalblue")
    st.markdown("#### Right endpoint rule: green")
    st.markdown("#### Midpoint rule : purple")

    # Show plot
    st.plotly_chart(fig,use_container_width=True)

    return h * left_sum, h * right_sum, h * midpoint_sum, h * default_sum


# integrate in trapezoid


def integrateInTrapezoid(f, a, b, n):
    # Calculate the integral using trapezoid rule
    h = (b - a) / n
    integral = (f(a) + f(b))/2.0
    for i in range(1, n):
        xi = a + i*h
        integral += f(xi)

    # Calculate the error
    error = abs(quad(f, a, b)[0] - integral * h)

    # Create plot of trapezoids
    trapezoids = []
    # Create list of trapezoids coordinates
    for i in range(n):
        xa = a + i * h
        xb = xa + h
        ya = f(xa)
        yb = f(xb)
        # Add trapezoid to list
        trapezoids.append(
            dict(
                type="path",
                path=f"M {xa} {ya} L {xb} {yb} L {xb} 0 L {xa} 0 Z",
                line=dict(color="royalblue", width=2),
                fillcolor="lightskyblue",
                opacity=0.5,
            )
        )

    # Graficate the function and trapezoids
    x = np.linspace(a, b, 1000)
    y = f(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name="f(x)"))
    fig.add_trace(go.Scatter(x=[a, b], y=[0, 0], name="Base"))
    fig.add_trace(go.Scatter(x=[a, a], y=[0, f(a)], name="Altura"))
    fig.add_trace(go.Scatter(x=[b, b], y=[0, f(b)], name="Altura"))

    # Add trapezoids to figure
    fig.update_layout(shapes=trapezoids)

    # Add title and axis names
    fig.update_layout(
        title="Gráfica de integracion trapecio",
        xaxis_title="x",
        yaxis_title="y",
    )

    # Configurar el grid de fondo
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='white')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='white')
    # Configurar el tamaño del gráfico
    fig.update_layout(width=800, height=600)
    # Configurar el layout de la figura
    y_range = [np.min(y), np.max(y)]
    fig.update_layout(
        xaxis=dict(range=[-10, 10]),
        yaxis=dict(range=y_range)
    )

    # Show plot
    st.plotly_chart(fig,use_container_width=True)

    return integral * h, error

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

# the main function


def main():
    try:

        # Instrucciones de uso
        instrucciones_rectangulo_trapecio = """
            <h1>Instrucciones de uso: Integración trapecio y rectangulo</h1>

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
        st.sidebar.markdown(instrucciones_rectangulo_trapecio, unsafe_allow_html=True)





        # Title
        st.title("Integracion en rectangulo y trapecio")
        st.markdown(
            "Esta calculadora integra en rectangulo y trapecio una ecuación dada.")
        st.markdown("")

        # Equation
        equation_str = st.text_input("Ecuación", "x**2")

        # Read the equation
        f = read_equation(equation_str)
        if f is None:
            return

        # Limits
        a = st.number_input("Limite izquierdo", value=0.0)
        b = st.number_input("Limite derecho", value=1.0)

        # Number of rectangles
        n = st.number_input("Número de particiones MAX(1000):", value=100)

        # n => 1000
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
                f'<h1 class="big-font">Error: El numero de rectangulos no puede ser mayor a 1000</h1>', unsafe_allow_html=True)
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
        print(f"Error: La ecuación no es válida. {error_type}: {error_msg}")

    # Create a button
    if st.button("Calcular"):
        try:
            # Integrate in rectangle
            st.markdown("## Integración por rectangulo")
            # Calculate the integral in rectangle
            integrate_left, integrate_right, integrate_midpoint, integrate_default = integrateInRectangle(
                f, a, b, n)
            st.markdown("### Resultados")
            st.latex(
                f"Integrate: \\int_{{{a}}}^{{{b}}} {equation_str} dx = {integrate_default}")
            st.latex(
                f"LeftEndPoint:\\int_{{{a}}}^{{{b}}} {equation_str} dx = {integrate_left}")
            st.latex(
                f"RightEndPoint:\\int_{{{a}}}^{{{b}}} {equation_str} dx = {integrate_right}")
            st.latex(
                f"MidPoint:\\int_{{{a}}}^{{{b}}} {equation_str} dx = {integrate_midpoint}")

            # Integrate in trapezoid
            st.markdown("## Integración por trapecio")
            # Calculate the integral in trapezoid
            integrate_trapezoid, error = integrateInTrapezoid(f, a, b, n)
            # Result
            st.markdown("### Resultados")
            st.latex(
                f"TrapezoidRule:\\int_{{{a}}}^{{{b}}} {equation_str} dx = {integrate_trapezoid}")
            # Calculate the error of the trapezoid rule
            st.latex(f"ErrorAbs:{error}")

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
