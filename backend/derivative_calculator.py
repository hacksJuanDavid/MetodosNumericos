import streamlit as st
import sympy as sp
import plotly.graph_objects as go
import numpy as np

# function to calculate the derivates 2


def calcular_derivadas2(funcion, n=1, xO=2.5):
    # try to convert the function to a sympy function
    try:
        # Define la variable simbólica x
        x = sp.symbols('x')
        # Calcular la derivada n veces
        derivada = funcion
        for i in range(n):
            derivada = sp.diff(derivada, x)

        # Simplificar la derivada
        derivada_simplificada = sp.simplify(derivada)

        # Evaluar la derivada en un punto
        valor_derivada = derivada_simplificada.subs(x, xO)

        # Save the results in a dictionary
        resultados = {
            'funcion': funcion,
            'derivada0': derivada,
            'derivada': derivada_simplificada,
            'valor_derivada': valor_derivada,
            'x': x
        }

        # Return the results
        return resultados

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

    # Instrucciones de uso
    instrucciones_derivadas = """
        <h1>Instrucciones de uso: Cálculo de Derivadas</h1>

        <h2>Descripción</h2>
        <p>El cálculo de derivadas es una técnica fundamental en el análisis matemático que permite determinar la tasa de cambio instantánea de una función en un punto dado. La derivada de una función representa su pendiente en cada punto y puede proporcionar información sobre su crecimiento, mínimos y máximos, y concavidad.</p>

        <h2>Procedimiento</h2>
        <p>A continuación se detalla el procedimiento para calcular la derivada de una función:</p>
        <ol>
            <li>Las funciones disponibles son: +, -, *, /, ^, **,sin(x),cos(x),tan(x),sqrt(x),exp(x),log(x)</li>
            <li>Identifica la función para la cual deseas calcular la derivada.</li>
            <li>Determina el tipo de derivada que deseas calcular: derivada de primer orden (primera derivada) o derivada de orden superior (derivadas sucesivas).</li>
            <li>Inserta la funcion de la que deseas derivar en el input correspondiente.</li>
            <li>Inserta el valor de x en el que deseas evaluar la derivada.</li>
            <li>El intervalo [a, b] son valores de ajuste para la grafica</li>
            <li>Selecciona el número de derivadas que deseas calcular.</li>
            <li>Presiona el botón "Calcular" y obtenedras los resultados.</li>
        </ol>

        <h2>Consideraciones adicionales</h2>
        <p>Es importante tener en cuenta que el cálculo de derivadas puede variar dependiendo del tipo de función y la técnica utilizada. Algunas funciones pueden requerir métodos más avanzados, como la derivación numérica o el uso de software especializado. Además, ten en cuenta las reglas y propiedades de las derivadas, como la regla de la cadena y la derivada de una constante.</p>
    """
    st.sidebar.markdown(instrucciones_derivadas, unsafe_allow_html=True)

    st.title("Calculadora de Derivadas")

    # Ask the user for the function and the value of Xo
    funcion = st.text_input("Introduce la función:",
                            value="((sin(x)+pi)/(sin(x)-pi))-pi*sin(x)")
    xO = st.number_input("Introduce el valor de Xo:", value=0.0)
    # Introduce el valor de a y b
    a = st.number_input("Introduce el valor de a:", value=0.0)
    b = st.number_input("Introduce el valor de b:", value=10.0)
    # Ask the user for the number of derivatives to calculate
    n = st.slider("Número de derivadas a calcular:",
                  min_value=1, max_value=10, value=1, step=1)

    # Calculate the derivatives
    resultados = calcular_derivadas2(funcion, n, xO)

    if st.button("Calcular"):
        # Show the results in LaTeX
        st.latex(r"\text{La función original es: } f(x) = " +
                 sp.latex(resultados['funcion']))
        st.latex(r"\text{La primera derivada sin simplificar es: } f^{(1)}(x) = " +
                 sp.latex(resultados['derivada0']))
        st.latex(r"\text{La primera derivada simplificada es: } f^{(1)}(x) = " +
                 sp.latex(resultados['derivada']))
        st.latex(r"\text{El valor de la primera derivada en } xO=2.5 \text{ es: } f^{(1)}(" +
                 str(resultados['x']) + r") = " + sp.latex(resultados['valor_derivada']))

        # Define los valores de x para graficar
        x = np.linspace(a, b, 1000)

        # Evalúa la derivada en los valores de x
        derivada_vals = [float(resultados['derivada0'].subs(
            resultados['x'], x_val)) for x_val in x]

        # Crea la figura
        fig = go.Figure()

        # Agrega la curva de la derivada a la figura
        fig.add_trace(go.Scatter(x=x, y=derivada_vals, mode='lines'))
        # Configurar el tamaño del gráfico
        fig.update_layout(width=800, height=600)
        # Agrega un título y etiquetas para los ejes
        fig.update_layout(title="Gráfica de la derivada",
                          xaxis_title="x", yaxis_title="y")
        # Muestra la figura
        st.plotly_chart(fig, use_container_width=True)


# Run main function
if __name__ == "__main__":
    main()
