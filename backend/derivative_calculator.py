import sympy as sp # Import sympy library 
import streamlit as st # Import sympy library 
import sympy as sp # Import sympy library 
import streamlit as st # Import streamlit library 
import plotly.graph_objects as go # Import plotly library
import numpy as np # Import numpy library

def calcular_derivadas(funcion, xo, n):
    x = sp.symbols('x')
    try:
        expr = sp.sympify(funcion)

        # Calculate the first n derivatives and evaluate at Xo
        derivadas = [expr]
        for i in range(1, n):
            derivada = sp.diff(derivadas[i-1], x)
            derivadas.append(derivada)

        resultados = [d.evalf(subs={x: xo}) for d in derivadas]
        return {'derivadas': derivadas, 'resultados': resultados}

    except (sp.SympifyError, TypeError):
        return {'error': 'Por favor, introduce una función válida.'}

def main():
    st.title("Calculadora de Derivadas")

    # Ask the user for the function and the value of Xo
    funcion = st.text_input("Introduce la función:")
    xo = st.number_input("Introduce el valor de Xo:", value=0.0)

    # Ask the user for the number of derivatives to calculate
    n = st.slider("Número de derivadas a calcular:", min_value=1, max_value=10, value=1, step=1)

    # Calculate the derivatives
    resultados = calcular_derivadas(funcion, xo, n)

    if st.button("Calcular"):
        # Show the results
        if 'error' in resultados:
            st.error(resultados['error'])
        else:
            # Plot the function and its derivatives
            fig = go.Figure()

            # Plot the function
            x = np.linspace(xo - 5, xo + 5, 1000)
            y = eval(funcion)
            fig.add_trace(go.Scatter(x=x, y=y, name='Función Original'))

            # Plot the derivatives
            for i, d in enumerate(resultados['derivadas']):
                # Check if the derivative is equal to the previous one
                if i > 0 and str(d) == str(resultados['derivadas'][i-1]):
                    continue

                # Evaluate the derivative at different points
                x = np.linspace(xo - 2, xo + 2, 1000)
                y = eval(str(d))
                fig.add_trace(go.Scatter(x=x, y=y, name=f"Derivada {i}"))

            # Show the results in Latex
            st.latex(f"f(x) = {funcion}")
            st.latex("\\\\")
            st.latex("Para \\ x = {0}".format(xo))
            st.latex("\\\\")

            for i, d in enumerate(resultados['derivadas']):
                # Check if the derivative is equal to the previous one
                if i > 0 and str(d) == str(resultados['derivadas'][i-1]):
                    continue

                st.latex("\\frac{{d^{0}}}{{dx^{0}}}f(x) = {1}".format(i, d))
                st.latex("\\\\")

                st.latex("\\frac{{d^{0}}}{{dx^{0}}}f({1}) = {2}".format(i, xo, resultados['resultados'][i]))
                st.latex("\\\\")
            # Set the layout of the plot and show it in the app
            fig.update_layout(title='Función y derivadas', xaxis_title='x', yaxis_title='f(x)')
            st.plotly_chart(fig)
# Run main function
if __name__ == "__main__":
    main()
