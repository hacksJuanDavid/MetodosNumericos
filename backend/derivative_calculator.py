import sympy as sp # Import sympy library 
import streamlit as st # Import sympy library 
import sympy as sp # Import sympy library 
import streamlit as st # Import streamlit library 

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

    # Show the results
    if 'error' in resultados:
        st.error(resultados['error'])
    else:
        st.write(f"La función original es: {funcion}")

        for i, d in enumerate(resultados['derivadas']):
            # Check if the derivative is equal to the previous one
            if i > 0 and str(d) == str(resultados['derivadas'][i-1]):
                continue

            st.write(f"La derivada {i} es: {d}")
            st.write(f"El valor de la derivada {i} en {xo} es: {resultados['resultados'][i]}")

# Run main function
if __name__ == "__main__":
    main()
