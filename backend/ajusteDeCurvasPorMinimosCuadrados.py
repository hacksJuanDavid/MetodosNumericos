'''
# Calculadora ajuste de curvas por minimos cuadrados


Se considera que un conjunto de n puntos experimentales, condensados en la siguiente tabla:

X|x1,x2
Y|y1,y2

Se considera la gráfica de los puntos experimentales, el propósito es determinar una función aproximada 
y=fx
 de tal manera que su gráfica se ajuste a una tendencia de los puntos dados. Esto es, encontrar una función f tal que 
fxi≈yi. 

Generalmente las funciones escogidas como modelo matemático son polinomios de la forma  

fx=a0+a1x+a2x2+a3x3+…+ anxn

tal que 
fxi=ym.



'''

import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Funcion para calcular el polinomio parseado


def parse_polynomial(coeficientes):
    grado = len(coeficientes) - 1

    # Redondear los coeficientes a 5 decimales
    coeficientes = np.round(coeficientes, 5)

    # Si el coeficiente no es negativo, agregar el signo +
    polinomio_parseado = ''
    for i in range(grado + 1):
        if coeficientes[i] >= 0:
            polinomio_parseado += '+'
        polinomio_parseado += str(coeficientes[i]) + 'x^' + str(grado - i)
    # Eliminar el signo + del primer termino
    polinomio_parseado = polinomio_parseado[1:]
    return polinomio_parseado

# Funcion para calcular el coeficiente de correlacion


def coeficiente_correlacion(x, y, coeficientes):
    # Calcular el coeficiente de correlacion
    y_promedio = np.mean(y)
    y_calculado = np.polyval(coeficientes, x)
    sst = np.sum((y - y_promedio) ** 2)
    ssr = np.sum((y_calculado - y_promedio) ** 2)
    r = np.sqrt(ssr / sst)
    return r

# Funcion para calcular el ajuste de curvas por minimos cuadrados


def ajuste_curvas_minimos_cuadrados(x, y, grado=6):
    # Calcular los polinomios de grado 1 a 6
    resultados = []
    for i in range(1, grado + 1):
        # Calcular los coeficientes del polinomio
        coeficientes = np.polyfit(x, y, i)
        # Calcular el polinomio parseado
        polinomio_parseado = parse_polynomial(coeficientes)
        # Calcular el error
        error = np.sum((np.polyval(coeficientes, x) - y) ** 2)

        # Calcular el coeficiente de correlación para el polinomio
        r = coeficiente_correlacion(x, y, coeficientes)

        # Guardar los resultados en un diccionario
        resultados.append({'Grado': i, 'Polinomio': polinomio_parseado,
                          'Error': error, 'Coeficiente de correlación': r})

    # Convertir la lista de resultados en un DataFrame
    resultados_df = pd.DataFrame(resultados)

    # Mostrar los resultados
    st.write(resultados_df)
    print(resultados_df)

    # Ecuacion resultante del ajuste de curvas
    st.header("Ecuación resultante del ajuste de curvas")
    st.latex(resultados_df.iloc[0]['Polinomio'])

    # Grafica de los puntos experimentales y el ajuste de curvas
    st.header("Gráfica de los puntos experimentales y el ajuste de curvas")
    # Graficar los puntos experimentales
    fig = px.scatter(x=x, y=y, labels={
                     'x': 'x', 'y': 'y'}, title='Puntos experimentales')
    # Graficar el ajuste de curvas
    x_grafica = np.linspace(np.min(x), np.max(x), 100)
    y_grafica = np.polyval(np.polyfit(x, y, 1), x_grafica)
    fig.add_trace(go.Scatter(x=x_grafica, y=y_grafica,
                  mode='lines', name='Ajuste de curvas'))
    # Mostrar la grafica
    st.plotly_chart(fig, use_container_width=True)


# Función principal


def main():


    # Instrucciones de uso
    instrucciones_minimos_cuadrados = """
        <h1>Instrucciones de uso: Método de Mínimos Cuadrados</h1>

        <h2>Descripción</h2>
        <p>El método de mínimos cuadrados es una técnica utilizada para encontrar la mejor aproximación de una relación funcional entre dos conjuntos de datos. Este método se utiliza comúnmente para ajustar una línea recta o una curva a un conjunto de puntos, minimizando la suma de los errores cuadrados entre los puntos y la línea o curva ajustada.</p>

        <h2>Procedimiento</h2>
        <p>A continuación se detalla el procedimiento general para aplicar el método de mínimos cuadrados:</p>
        <ol>
            <li>Recolecta los datos en dos conjuntos: las variables independientes (x) y las variables dependientes (y).</li>
            <li>Representa los datos en un gráfico de dispersión para visualizar la relación entre las variables.</li>
            <li>Determina el tipo de función que mejor se ajusta a los datos. Algunos ejemplos comunes incluyen una línea recta (regresión lineal) o una curva de grado superior (regresión polinómica).</li>
            <li>Presiona el boton "Calcular" y obtendras los resultados.</li>
        </ol>

        <h2>Consideraciones adicionales</h2>
        <p>El método de mínimos cuadrados puede extenderse a casos más complejos, como ajustes polinómicos de grado superior o ajustes no lineales. Además, ten en cuenta que existen software y herramientas en línea que pueden ayudarte a realizar cálculos de mínimos cuadrados de manera más eficiente y precisa.</p>
    """
    st.sidebar.markdown(instrucciones_minimos_cuadrados, unsafe_allow_html=True)


    st.title("Ajuste de Curvas por Mínimos Cuadrados")

    # Ingreso de datos
    st.header("Ingreso de datos")
    num_puntos = st.number_input(
        "Número de puntos", min_value=2, step=1, value=5)
    x = []
    y = []

    # Ingreso de puntos experimentales de la forma (x, y) en dos columnas y cada columna tenga 2 puntos por fila
    st.header("Ingreso de puntos experimentales")
    for i in range(num_puntos):
        col1, col2 = st.columns(2)
        with col1:
            x.append(st.number_input("x{}".format(i+1), step=1.0))
        with col2:
            y.append(st.number_input("y{}".format(i+1), step=1.0))
    # Selección del tipo de ajuste
    st.header("Selección del tipo de ajuste")
    tipo_ajuste = st.selectbox("Tipo de ajuste", [
        "Minimos cuadrados"])
    # Crear botón para calcular el ajuste
    calcular = st.button("Calcular")
    if calcular:
        # Cálculo del ajuste
        st.header("Resultados")
        if tipo_ajuste == "Minimos cuadrados":
            # Calcular minimos cuadrados polinomiales de grado n
            ajuste_curvas_minimos_cuadrados(x, y)


if __name__ == "__main__":
    main()
