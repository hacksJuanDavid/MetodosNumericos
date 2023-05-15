'''
#Crear una calculadora de matrices 

    Suma de matrices
    Resta de matrices
    Multiplicación de matrices
    Inversa de una matriz
    Transposición de una matriz
    Cálculo de determinante
    Cálculo de la traza de una matriz
    Resolución de sistemas de ecuaciones lineales mediante matrices
    Matrices triangular superior e inferior
    Matrices diagonales
    Factorización LU
    Eliminación de Gauss-Jordan

'''
import numpy as np
import streamlit as st
import sympy as sp

# Funcion para sumar matrices


def sumMatrix(a, b):
    # Comprobar si las matrices son cuadradas
    if isSquareMatrix(a) and isSquareMatrix(b):
        try:
            # Sumar las matrices
            return np.add(a, b)
        except:
            st.warning('Las matrices no se pueden sumar')
            st.write("\n")

# Funcion para restar matrices


def subMatrix(a, b):
    # Comprobar si las matrices son cuadradas
    if isSquareMatrix(a) and isSquareMatrix(b):
        try:
            # Restar las matrices
            return np.subtract(a, b)
        except:
            st.warning('Las matrices no se pueden restar')
            st.write("\n")

# Funcion para multiplicar matrices


def multMatrix(a, b):
    # Comprobar si las matrices son cuadradas
    if isSquareMatrix(a) and isSquareMatrix(b):
        try:
            # Multiplicar las matrices
            return np.dot(a, b)
        except:
            st.warning('Las matrices no se pueden multiplicar')
            st.write("\n")

# Funcion para multiplicar una matriz por un escalar


def multScalarMatrix(matrices):
    try:
        # Input para el escalar
        scalar = st.number_input('Escalar', value=1.0, step=0.1)

        # Input para seleccionar la matriz a multiplicar
        matrix_name = st.selectbox(
            'Seleccione la matriz a multiplicar',
            list(matrices.keys())
        )

        matrix = matrices[matrix_name]

        # Si la matriz esta vacia
        if matrix is None:
            st.warning('La matriz esta vacia')
            st.write("\n")
            return None

        # Calcular la matriz resultante si escoge una matrix diferente a de la seleccionada
        if matrix_name != matrices.keys():
            result = np.multiply(scalar, matrix)

        # Multiplicar la matriz por el escalar
        result = np.multiply(scalar, matrix)

        # Botón para ejecutar la función
        if st.button('Multiplicar matriz por escalar'):
            # Retornar el resultado
            return result

    except:
        st.warning('Hubo un error al multiplicar la matriz por el escalar')
        st.write("\n")
        return None

# Funcion para calcular la inversa de una matriz


def invMatrix(a):
    # Parsear la matriz a una matriz de SymPy
    a = sp.Matrix(a)

    # Comprobar si la matriz es cuadrada
    if isSquareMatrix(a):
        # Comprobar si la matriz tiene inversa
        if a.det() == 0:
            st.warning('La matriz no tiene inversa')
            st.write("\n")
        else:
            try:
                # Calcular la inversa de la matriz
                return a.inv()
            except:
                st.warning('Hubo un error al calcular la inversa')
                st.write("\n")
    else:
        st.warning('La matriz no es cuadrada')
        st.write("\n")

# Funcion para calcular la transpuesta de una matriz


def transMatrix(a):
    return np.transpose(a)

# Funcion para calcular el determinante de una matriz


def detMatrix(a):
    # Parsear la matriz a una matriz de SymPy
    a = sp.Matrix(a)

    # Comprobar si la matriz es cuadrada
    if isSquareMatrix(a):
        try:
            print("Determinante: Matrix ingresada", a)
            # Calcular el determinante de la matriz
            return a.det()
        except:
            st.warning('Hubo un error al calcular el determinante')
            st.write("\n")
    else:
        st.warning('La matriz no es cuadrada')
        st.write("\n")

# Funcion para calcular la traza de una matriz


def traceMatrix(a):
    # Parsear la matriz a una matriz de SymPy
    a = sp.Matrix(a)

    # Comprobar si la matriz es cuadrada
    if isSquareMatrix(a):
        try:
            # Calcular la traza de la matriz
            return a.trace()
        except:
            st.warning('Hubo un error al calcular la traza')
            st.write("\n")
    else:
        st.warning('La matriz no es cuadrada')
        st.write("\n")

# Funcion para resolver un sistema de ecuaciones lineales mediante matrices


def solveMatrix(a, b):
    # Parsear la matriz a una matriz de SymPy
    a = sp.Matrix(a)
    b = sp.Matrix(b)

    # Solve the system of equations
    try:
        # Calcular la solucion del sistema de ecuaciones
        return a.solve(b)
    except:
        st.warning('Hubo un error al calcular la solucion')
        st.write("\n")

# Funcion para calcular matrix triangular


def triangularMatrix(a):
    # Comprobar si la matriz es cuadrada
    if isSquareMatrix(a):
        try:
            # Calcular la matriz triangular
            return np.triu(a)
        except:
            st.warning('Hubo un error al calcular la matriz triangular')
            st.write("\n")
    else:
        st.warning('La matriz no es cuadrada')
        st.write("\n")

# Funcion para calcular la matriz triangular superior


def upperTriangularMatrix(a):
    return np.triu(a)

# Funcion para calcular la matriz triangular inferior


def lowerTriangularMatrix(a):
    return np.tril(a)

# Funcion para calcular la matriz diagonal


def diagonalMatrix(a):
    # Parsear la matriz a una matriz de SymPy
    a = sp.Matrix(a)

    # Comprobar si la matriz es cuadrada
    if isSquareMatrix(a):
        try:
            # Calcular la matriz diagonal
            P, D = a.diagonalize()
            return D
        except:
            st.warning('Hubo un error al calcular la matriz diagonal')
            st.write("\n")
    else:
        st.warning('La matriz no es cuadrada')
        st.write("\n")

# Funcion para calcular la factorizacion LU


def luMatrix(a):
    # Parsear la matriz a una matriz de SymPy
    a = sp.Matrix(a)

    # Comprobar si la matriz es cuadrada
    if isSquareMatrix(a):
        try:
            # Calcular la factorizacion LU
            return a.LUdecomposition()
        except:
            st.warning('Hubo un error al calcular la factorizacion LU')
            st.write("\n")
    else:
        st.warning('La matriz no es cuadrada')
        st.write("\n")


# Funcion para calcular la eliminacion Gauss-Jordan
def gaussJordanEliminationMatrix():
    # Creamos 3 columnas para filas, columnas y términos independientes
    col1, col2 = st.columns(2)

    # Creamos input para filas
    rows = col1.number_input(
        'Ingrese el numero de filas de la matriz', min_value=1, max_value=10, value=1)

    # Creamos input para columnas
    cols = col2.number_input(
        'Ingrese el numero de columnas de la matriz', min_value=1, max_value=10, value=1)

    # Creamos una matriz de ceros y una lista de términos independientes
    matrix = np.zeros((rows, cols))
    terminos_independientes = [0] * rows

    # Obtener los valores de la matriz del usuario
    st.write('Ingrese los valores para la matriz y los términos independientes:')
    for i in range(rows):
        # Agregar una columna para términos independientes
        cols_input = st.columns(cols + 1)
        for j in range(cols):
            # Leer la entrada del usuario como una cadena y convertirla a un número
            value_str = cols_input[j].text_input('Ingrese un valor para la celda ['+str(
                i)+']['+str(j)+']', key='matrix_'+'_'+str(i)+'_'+str(j))
            try:
                value = float(value_str)
                matrix[i][j] = value
            except:
                st.warning('Ingrese un numero valido')
                st.write("\n")
        # Leer el valor del término independiente para esta fila
        termino_str = cols_input[cols].text_input(
            'Ingrese un valor para el termino independiente ['+str(i)+']', key='terminos_'+'_'+str(i))
        try:
            termino = float(termino_str)
            terminos_independientes[i] = termino
        except:
            st.warning('Ingrese un numero valido para el termino independiente')
            st.write("\n")

    # Crear un boton para calcular gauss jordan
    if st.button('Calcular Gauss-Jordan'):
        # Concatenar la matriz y los términos independientes en una matriz aumentada
        Ab = np.concatenate(
            (matrix, np.array(terminos_independientes).reshape(-1, 1)), axis=1)

        # Iterar sobre las filas de la matriz aumentada
        n = len(Ab)
        for i in range(n):
            # Dividir la fila i por Ab[i,i]
            Ab[i, :] = Ab[i, :] / Ab[i, i]

            # Hacer 0s debajo del pivote en la columna i
            for j in range(i+1, n):
                Ab[j, :] = Ab[j, :] - Ab[i, :] * Ab[j, i]

            # Hacer 0s arriba del pivote en la columna i
            for j in range(i):
                Ab[j, :] = Ab[j, :] - Ab[i, :] * Ab[j, i]

        # La matriz Ab está ahora en forma escalonada reducida, extraer la última columna como solución
        x = Ab[:, -1]

        st.subheader('La solución del sistema de ecuaciones es:')
        # Print the solution latex
        st.latex('x = ' + sp.latex(sp.Matrix(x)))


# ////////////////////////////////////////////////////////////////////////////////////////
# Funcion comprobar si es cuadrada la matriz


def isSquareMatrix(matrix):
    return matrix.shape[0] == matrix.shape[1]

# Funcion comprobar si es rectangular la matriz


def isRectangularMatrix(matrix):
    return matrix.shape[0] != matrix.shape[1]

# Funcion comprobar si es matriz nula


def isNullMatrix(matrix):
    return np.all(matrix == 0)

# Funcion comprobar si es matriz identidad


def isIdentityMatrix(matrix):
    return np.all(matrix == np.identity(matrix.shape[0]))

# Funcion comprobar si es matriz triangular superior


def isUpperTriangularMatrix(matrix):
    return np.all(np.triu(matrix) == matrix)

# Funcion comprobar si es matriz triangular inferior


def isLowerTriangularMatrix(matrix):
    return np.all(np.tril(matrix) == matrix)

# Funcion comprobar si es matriz diagonal


def isDiagonalMatrix(matrix):
    return np.all(np.tril(matrix, -1) == 0) and np.all(np.triu(matrix, 1) == 0)

# Funcion comprobar si es matriz simetrica


def isSymmetricMatrix(matrix):
    return np.all(matrix == matrix.T)

# Funcion comprobar si es matriz antisimetrica


def isAntiSymmetricMatrix(matrix):
    return np.all(matrix == -matrix.T)

# Funcion comprobar si es matriz ortogonal


def isOrthogonalMatrix(matrix):
    return np.all(np.linalg.inv(matrix) == matrix.T)


# Funcion que comprueba que tipo de matriz es
def matrixChecker(matrix):
    # Comprobar que tipo de matriz es
    if isSquareMatrix(matrix):
        st.warning('La matriz es cuadrada')
        st.write("\n")

    elif isRectangularMatrix(matrix):
        st.warning('La matriz es rectangular')
        st.write("\n")

    elif isNullMatrix(matrix):
        st.warning('La matriz es nula')
        st.write("\n")

    elif isIdentityMatrix(matrix):
        st.warning('La matriz es identidad')
        st.write("\n")

    elif isUpperTriangularMatrix(matrix):
        st.warning('La matriz es triangular superior')
        st.write("\n")

    elif isLowerTriangularMatrix(matrix):
        st.warning('La matriz es triangular inferior')
        st.write("\n")

    elif isDiagonalMatrix(matrix):
        st.warning('La matriz es diagonal')
        st.write("\n")

    elif isSymmetricMatrix(matrix):
        st.warning('La matriz es simetrica')
        st.write("\n")

    elif isAntiSymmetricMatrix(matrix):
        st.warning('La matriz es antisimetrica')
        st.write("\n")

    elif isOrthogonalMatrix(matrix):
        st.warning('La matriz es ortogonal')
        st.write("\n")

    else:
        st.warning('La matriz es ninguna de las anteriores')
        st.write("\n")

# ////////////////////////////////////////////////////////////////////////////////////////


# Función para crear matrices con nombre y dimensiones y guardarlas en un diccionario
def createMatrices():
    matrices = {}

    st.write('Ingrese las dimensiones y los valores de las matrices')

    # Contador de matrices
    matrix_count = 1

    # Bucle para crear varias matrices
    while True:
        st.write('Matriz', matrix_count)

        # Ingrese un nombre único para cada matriz
        name = st.text_input(
            f'Ingrese el nombre de la matriz {matrix_count}', key=f'matrix_name_{matrix_count}')

        # Salir del bucle si no se ingresa un nombre de matriz
        if not name:
            break

        # Crear 2 columnas para las dimensiones de la matriz
        cols = st.columns(2)

        # Obtener las dimensiones de la matriz del usuario
        rows = cols[0].number_input(
            'Ingrese el numero de filas', min_value=1, key='matrix_'+str(matrix_count)+'_rows')
        cols = cols[1].number_input(
            'Ingrese el numero de columnas', min_value=1, key='matrix_'+str(matrix_count)+'_cols')

        # Crear la matriz y guardarla en el diccionario
        matrices[name] = np.zeros((rows, cols), dtype=object)

        # Obtener los valores de la matriz del usuario
        st.write('Ingrese los valores para la matriz', name)
        for i in range(rows):
            cols_input = st.columns(cols)
            for j in range(cols):
                # Leer la entrada del usuario como una cadena
                value_str = cols_input[j].text_input('Ingrese un valor para la celda ['+str(
                    i)+']['+str(j)+']', key='matrix_'+str(matrix_count)+'_'+str(i)+'_'+str(j))

                # Evaluar la expresión matemática ingresada por el usuario
                if value_str:
                    value = sp.sympify(value_str)
                    # Si es una constante numérica, convertirla en un número flotante
                    if value.is_number:
                        matrices[name][i][j] = float(value)
                    else:
                        # Crear un diccionario con los valores de las variables
                        # que aparecen en la expresión
                        vars_dict = {symbol: matrices.get(
                            str(symbol), symbol) for symbol in value.free_symbols}
                        # Reemplazar las variables por sus valores
                        value = value.subs(vars_dict)
                        # Guardar la expresión simbólica en la matriz
                        matrices[name][i][j] = value

        # Incrementar el contador de matrices
        matrix_count += 1
        # Matrix Checker
        matrixChecker(matrices[name])

    # Print matrices
    print("Matrices del sistema cache:", matrices)
    # Devolver el diccionario de matrices
    return matrices

# Función para calcular la operación


def calcular_operacion(operacion, matrices):
    # Buscar si la operación contiene el determinante
    if "det(" in operacion:
        # Extraer el nombre de la matriz
        nombre_matriz = operacion[operacion.find("(")+1:operacion.find(")")]

        print("Nombre de la matriz det:", nombre_matriz)
        # Buscar la matriz correspondiente
        matriz = matrices.get(nombre_matriz)
        if matriz is None:
            try:
                raise ValueError(f"La matriz {nombre_matriz} no está definida")
            except ValueError as e:
                st.error(e)
                st.stop()
        # Calcular el determinante
        resultado_det = detMatrix(matriz)

        # Imprimir el resultado del determinante en formato LaTeX
        printMatricesSymPy(matrices, nombre_matriz, resultado_det, "det")

        # Reemplazar la operación del determinante en la expresión original con su resultado
        operacion = operacion.replace(
            f"det({nombre_matriz})", str(resultado_det))

    # Buscar si la operación contiene la inversa
    elif "inv(" in operacion:
        # Extraer el nombre de la matriz
        nombre_matriz = operacion[operacion.find("(")+1:operacion.find(")")]

        print("Nombre de la matriz inv:", nombre_matriz)
        # Buscar la matriz correspondiente
        matriz = matrices.get(nombre_matriz)
        if matriz is None:
            try:
                raise ValueError(f"La matriz {nombre_matriz} no está definida")
            except ValueError as e:
                st.error(e)
                st.stop()
        # Calcular la inversa
        resultado_inv = invMatrix(matriz)

        # Imprimir el resultado de la inversa en formato LaTeX
        printMatricesSymPy(matrices, nombre_matriz, resultado_inv, "inv")

        # Reemplazar la operación de la inversa en la expresión original con su resultado
        operacion = operacion.replace(
            f"inv({nombre_matriz})", str(resultado_inv))

    # Buscar si la operación contiene la transpuesta
    elif "t(" in operacion:
        # Extraer el nombre de la matriz
        nombre_matriz = operacion[operacion.find("(")+1:operacion.find(")")]
        # Buscar la matriz correspondiente
        matriz = matrices.get(nombre_matriz)
        if matriz is None:
            try:
                raise ValueError(f"La matriz {nombre_matriz} no está definida")
            except ValueError as e:
                st.error(e)
                st.stop()
        # Calcular la transpuesta
        resultado_transpuesta = transMatrix(matriz)

        # Imprimir el resultado de la transpuesta en formato LaTeX
        printMatricesX1Numpy(matrices, nombre_matriz,
                             resultado_transpuesta, "t")

        # Reemplazar la operación de la transpuesta en la expresión original con su resultado
        operacion = operacion.replace(
            f"t({nombre_matriz})", str(resultado_transpuesta))

    # Buscar si la operación contiene la traza
    elif "tr(" in operacion:
        # Extraer el nombre de la matriz
        nombre_matriz = operacion[operacion.find("(")+1:operacion.find(")")]
        # Buscar la matriz correspondiente
        matriz = matrices.get(nombre_matriz)
        if matriz is None:
            try:
                raise ValueError(f"La matriz {nombre_matriz} no está definida")
            except ValueError as e:
                st.error(e)
                st.stop()
        # Calcular la traza
        resultado_traza = traceMatrix(matriz)

        # Imprimir el resultado de la traza en formato LaTeX
        printMatricesSymPy(matrices, nombre_matriz, resultado_traza, "tr")

        # Reemplazar la operación de la traza en la expresión original con su resultado
        operacion = operacion.replace(
            f"tr({nombre_matriz})", str(resultado_traza))

    # Buscar si la operación contiene la triangular
    elif "triu(" in operacion:
        # Extraer el nombre de la matriz
        nombre_matriz = operacion[operacion.find("(")+1:operacion.find(")")]
        # Buscar la matriz correspondiente
        matriz = matrices.get(nombre_matriz)
        if matriz is None:
            try:
                raise ValueError(f"La matriz {nombre_matriz} no está definida")
            except ValueError as e:
                st.error(e)
                st.stop()
        # Calcular la triangular
        resultado_triu = triangularMatrix(matriz)

        # Imprimir el resultado de la triangular en formato LaTeX
        printMatricesX1Numpy(matrices, nombre_matriz, resultado_triu, "triu")

        # Reemplazar la operación de la triangular en la expresión original con su resultado
        operacion = operacion.replace(
            f"triu({nombre_matriz})", str(resultado_triu))

    # Buscar si la operación contiene la Diagonal
    elif "diag(" in operacion:
        # Extraer el nombre de la matriz
        nombre_matriz = operacion[operacion.find("(")+1:operacion.find(")")]
        # Buscar la matriz correspondiente
        matriz = matrices.get(nombre_matriz)
        if matriz is None:
            try:
                raise ValueError(f"La matriz {nombre_matriz} no está definida")
            except ValueError as e:
                st.error(e)
                st.stop()
        # Calcular la Diagonal
        resultado_diag = diagonalMatrix(matriz)

        # Imprimir el resultado de la Diagonal en formato LaTeX
        printMatricesSymPy(matrices, nombre_matriz, resultado_diag, "diag")

        # Reemplazar la operación de la Diagonal en la expresión original con su resultado
        operacion = operacion.replace(
            f"diag({nombre_matriz})", str(resultado_diag))

    # Buscar si la operación contiene la LU
    elif "lu(" in operacion:
        # Extraer el nombre de la matriz
        nombre_matriz = operacion[operacion.find("(")+1:operacion.find(")")]
        # Buscar la matriz correspondiente
        matriz = matrices.get(nombre_matriz)
        if matriz is None:
            try:
                raise ValueError(f"La matriz {nombre_matriz} no está definida")
            except ValueError as e:
                st.error(e)
                st.stop()
        # Calcular la LU
        resultado_LU = luMatrix(matriz)[0]

        # Imprimir el resultado de la LU en formato LaTeX
        printMatricesSymPy(matrices, nombre_matriz, resultado_LU, "lu")

        # Reemplazar la operación de la LU en la expresión original con su resultado
        operacion = operacion.replace(
            f"LU({nombre_matriz})", str(resultado_LU))

    try:
        # Evaluar la expresión actualizada
        resultado = eval(operacion, {}, matrices)

        # print
        print("Resultado operaciones:", resultado)

        # Convierte el resultado a latex y la operacion le da formato de matriz para imprimirlo en streamlit
        resultado = fr"{operacion} = \begin{{bmatrix}}" + " \\\\".join(
            [" & ".join(map(str, row)) for row in resultado]) + r" \end{bmatrix}"

        # Imprimir resultado en streamlit
        st.latex(resultado)

    except Exception as e:
        st.error(f"No se pudo evaluar la expresión: {e}")
        st.stop()

    # Retornar el resultado
    return resultado


# Funcion imprimir matrices


def printMatricesX2Numpy(matrices, matrix1, matrix2, result, operation):
    try:
        # Convertir las matrices en cadenas de texto LaTeX
        matrix1_latex = fr"{matrix1} = \begin{{bmatrix}}" + " \\\\".join(
            [" & ".join(map(str, row)) for row in matrices[matrix1]]) + r" \end{bmatrix}"
        matrix2_latex = fr"{matrix2} = \begin{{bmatrix}}" + " \\\\".join(
            [" & ".join(map(str, row)) for row in matrices[matrix2]]) + r" \end{bmatrix}"
        result_latex = fr"{matrix1} {operation} {matrix2} = \begin{{bmatrix}}" + " \\\\".join(
            [" & ".join(map(str, row)) for row in result]) + r" \end{bmatrix}"

        # Mostrar la operación y el resultado en LaTeX
        st.write(
            f"El resultado de la operación {operation} entre las matrices es:")
        st.latex(
            fr"\begin{{aligned}} & ({matrix1_latex}) {operation} ({matrix2_latex}) =  \end{{aligned}}")
        st.latex(fr"\begin{{aligned}} & {result_latex} \end{{aligned}}")
    except:
        st.write('No se puede imprimir la matriz')


# Funcion imprimir matrices
def printMatricesX1Numpy(matrices, matrix1, result, operation):
    try:
        # Convertir las matrices en cadenas de texto LaTeX
        matrix1_latex = fr"{matrix1} = \begin{{bmatrix}}" + " \\\\".join(
            [" & ".join(map(str, row)) for row in matrices[matrix1]]) + r" \end{bmatrix}"
        result_latex = fr"{matrix1} {operation} = \begin{{bmatrix}}" + " \\\\".join(
            [" & ".join(map(str, row)) for row in result]) + r" \end{bmatrix}"

        # Mostrar la operación y el resultado en LaTeX
        st.write(
            f"El resultado de la operación {operation} entre las matrices es:")
        st.latex(
            fr"\begin{{aligned}} & ({matrix1_latex}) {operation} =  \end{{aligned}}")
        st.latex(fr"\begin{{aligned}} & {result_latex} \end{{aligned}}")
    except:
        # Esta excepción se produce cuando se intenta imprimir una matriz vacía
        st.write('No se puede imprimir la matriz esta vacia')

# Funcion imprimir matrices SymPy x2


def printMatricesSymPyX2(matrices, matrix1, matrix2, result, operation):
    # Convertir las matrices simbólicas en listas de listas de Python
    matrix1_list = sp.Matrix(matrices[matrix1]).tolist()
    matrix2_list = sp.Matrix(matrices[matrix2]).tolist()

    # Si es un numero , no convertirlo en lista de listas
    if isinstance(result, (int, float, complex)):
        result_list = [[result]]
    elif isinstance(result, sp.Float):
        # Recortar el resultado a 2 decimales
        result = round(result, 2)
        # Convertir el resultado en una lista de listas
        result_list = [[float(result)]]
    else:
        # if isntance of sympy matrix
        if isinstance(result, sp.Matrix):
            result_list = result.tolist()
        # if isntance of sympy float
        elif isinstance(result, sp.Float):
            # Recortar el resultado a 2 decimales
            result = round(result, 2)
            # Convertir el resultado en una lista de listas
            result_list = [[float(result)]]
        else:
            # Convertir el resultado en una lista de listas
            result_list = sp.Matrix(result).tolist()

    # Convertir las matrices en cadenas de texto LaTeX
    matrix1_latex = fr"{matrix1} = \begin{{bmatrix}}" + " \\\\".join(
        [" & ".join(map(str, row)) for row in matrix1_list]) + r" \end{bmatrix}"

    matrix2_latex = fr"{matrix2} = \begin{{bmatrix}}" + " \\\\".join(
        [" & ".join(map(str, row)) for row in matrix2_list]) + r" \end{bmatrix}"

    result_latex = fr"{matrix1} {operation} {matrix2} = \begin{{bmatrix}}" + " \\\\".join(
        [" & ".join(map(str, row)) for row in result_list]) + r" \end{bmatrix}"

    # Mostrar la operación y el resultado en LaTeX
    st.write(
        f"El resultado de la operación {operation} entre las matrices es:")
    st.latex(
        fr"\begin{{aligned}} & ({matrix1_latex}) {operation} ({matrix2_latex}) =  \end{{aligned}}")
    st.latex(fr"\begin{{aligned}} & {result_latex} \end{{aligned}}")


# Funcion imprimir matrices SymPy
def printMatricesSymPy(matrices, matrix1, result, operation):
    # Convertir las matrices simbólicas en listas de listas de Python
    matrix1_list = sp.Matrix(matrices[matrix1]).tolist()

    # Si es un numero , no convertirlo en lista de listas
    if isinstance(result, (int, float, complex)):
        result_list = [[result]]

    else:
        # if isntance of sympy matrix
        if isinstance(result, sp.Matrix):
            result_list = result.tolist()
        # if isntance of sympy float
        elif isinstance(result, sp.Float):
            # Recortar el resultado a 2 decimales
            result = round(result, 2)
            # Convertir el resultado en una lista de listas
            result_list = [[float(result)]]
        else:
            # Convertir el resultado en una lista de listas
            result_list = [[result]] if isinstance(result, float) else []

        # Convertir las listas de listas en cadenas de texto LaTeX
        matrix1_latex = fr"{matrix1} = \begin{{bmatrix}}" + " \\\\".join(
            [" & ".join(map(str, row)) for row in matrix1_list]) + r" \end{bmatrix}"
        result_latex = fr"{matrix1} {operation} = \begin{{bmatrix}}" + (" \\\\".join(
            [" & ".join(map(str, row)) for row in result_list]) if result_list else "") + r" \end{bmatrix}"

        # Siempre que el resultado no sea una lista vacía imprir hasta el final
        if result_list:
            # Mostrar la operación y el resultado en LaTeX
            st.write(
                f"El resultado de la operación {operation} entre las matrices es:")
            st.latex(
                fr"\begin{{aligned}} & ({matrix1_latex}) {operation} =  \end{{aligned}}")
            st.latex(fr"\begin{{aligned}} & {result_latex} \end{{aligned}}")
        else:
            # Mostrar la operación y el resultado en LaTeX
            st.write(
                f"El resultado de la operación {operation} entre las matrices es:")
            st.latex(
                fr"\begin{{aligned}} & ({matrix1_latex}) {operation} =  \end{{aligned}}")
            st.latex(fr"\begin{{aligned}} & {result} \end{{aligned}}")


# Funtion main


def main():

    # Tabs

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Crear matrices", "Calcular matrices", "Operacion entre matrices ", "Calcular Matrices por un escalar", "Calculadora de matrices por Gauss-Jordan"])

    with tab1:
        # Creamos las matrices
        st.title('Crear matrices')
        matrices = createMatrices()

    with tab2:
        # Creamos la opcion de seleccionar las matrices
        st.title('Seleccionar matrices x2')
        matrix1 = st.selectbox(
            'Seleccione la primera matriz',
            list(matrices.keys())
        )

        matrix2 = st.selectbox(
            'Seleccione la segunda matriz',
            list(matrices.keys())
        )

        # Creamos las opciones de la calculadora
        st.title('Opciones para calcular matrices')
        options = st.selectbox(
            'Seleccione una opcion',
            ('Suma de matrices', 'Resta de matrices', 'Multiplicacion de matrices', 'Inversa de una matriz', 'Transpuesta de una matriz', 'Determinante de una matriz', 'Traza de una matriz',
             'Resolver un sistema de ecuaciones lineales mediante matrices', 'Matriz triangular', 'Matriz triangular superior', 'Matriz triangular inferior', 'Matriz diagonal', 'Factorizacion LU')
        )

        # Cramos un boton para calcular
        if st.button('Calcular'):
            # Creamos la opcion de calcular
            st.title('Calcular Resultado')
            if options == 'Suma de matrices':
                try:
                    # Las matrices deben ser cuadradas
                    if isSquareMatrix(matrices[matrix1]) and isSquareMatrix(matrices[matrix2]):
                        if matrix1 is None or matrix2 is None:
                            st.error(
                                "Por favor, seleccione dos matrices para sumar.")
                        else:
                            result = sumMatrix(
                                matrices[matrix1], matrices[matrix2])

                            # Print matrices
                            printMatricesX2Numpy(
                                matrices, matrix1, matrix2, result, "+")
                    else:
                        st.error("Las matrices deben de ser cuadradas.")
                except:
                    st.error("Por favor, seleccione dos matrices para sumar.")
                    st.error("Las matrices deben de ser cuadradas.")

            elif options == 'Resta de matrices':
                try:
                    # Las matrices deben ser cuadradas
                    if isSquareMatrix(matrices[matrix1]) and isSquareMatrix(matrices[matrix2]):

                        if matrix1 is None or matrix2 is None:
                            st.error(
                                "Por favor, seleccione dos matrices para restar.")
                        else:
                            result = subMatrix(
                                matrices[matrix1], matrices[matrix2])

                            # Print matrices
                            printMatricesX2Numpy(
                                matrices, matrix1, matrix2, result, "-")
                    else:
                        st.error("Las matrices deben de ser cuadradas.")
                except:
                    st.error("Por favor, seleccione dos matrices para restar.")
                    st.error("Las matrices deben de ser cuadradas.")

            elif options == 'Multiplicacion de matrices':
                try:
                    # Las matrices deben ser cuadradas
                    if isSquareMatrix(matrices[matrix1]) and isSquareMatrix(matrices[matrix2]):
                        if matrix1 is None or matrix2 is None:
                            st.error(
                                "Por favor, seleccione dos matrices para multiplicar.")
                        else:
                            result = multMatrix(
                                matrices[matrix1], matrices[matrix2])

                            # Print matrices
                            printMatricesX2Numpy(
                                matrices, matrix1, matrix2, result, "*")
                    else:
                        st.error("Las matrices deben de ser cuadradas.")
                except:
                    st.error(
                        "Por favor, seleccione dos matrices para multiplicar.")
                    st.error("Las matrices deben de ser cuadradas.")

            elif options == 'Inversa de una matriz':
                # Las matrices deben ser cuadradas
                try:
                    # Las matrices deben ser cuadradas
                    if isSquareMatrix(matrices[matrix1]) and isSquareMatrix(matrices[matrix2]):

                        if matrix1 is None or matrix2 is None:
                            st.error(
                                "Por favor, seleccione una matriz para calcular su inversa.")
                        else:
                            result1 = invMatrix(matrices[matrix1])
                            result2 = invMatrix(matrices[matrix2])

                            # Print matrices SymPy
                            printMatricesSymPy(
                                matrices, matrix1, result1, "^-1")
                            printMatricesSymPy(
                                matrices, matrix2, result2, "^-1")
                    else:
                        st.error("Las matrices deben de ser cuadradas.")
                except:
                    st.error(
                        "Por favor, seleccione una matriz para calcular su inversa.")
                    st.error("El determinante tiene que ser diferente de 0.")
                    st.error("Las matrices deben de ser cuadradas.")

            elif options == 'Transpuesta de una matriz':
                if matrix1 is None or matrix2 is None:
                    st.error(
                        "Por favor, seleccione una matriz para calcular su transpuesta.")
                else:
                    result1 = transMatrix(matrices[matrix1])
                    result2 = transMatrix(matrices[matrix2])

                    # Print matrices
                    printMatricesX1Numpy(matrices, matrix1, result1, "^T")
                    printMatricesX1Numpy(matrices, matrix2, result2, "^T")

            elif options == 'Determinante de una matriz':
                if matrix1 is None or matrix2 is None:
                    st.error(
                        "Por favor, seleccione una matriz para calcular su determinante.")
                else:
                    result1 = detMatrix(matrices[matrix1])
                    result2 = detMatrix(matrices[matrix2])

                    # Print matrices
                    printMatricesSymPy(matrices, matrix1, result1, "det")
                    printMatricesSymPy(matrices, matrix2, result2, "det")

            elif options == 'Traza de una matriz':
                if matrix1 is None or matrix2 is None:
                    st.error(
                        "Por favor, seleccione una matriz para calcular su traza.")
                else:
                    result1 = traceMatrix(matrices[matrix1])
                    result2 = traceMatrix(matrices[matrix2])

                    # Print matrices
                    printMatricesSymPy(matrices, matrix1, result1, "tr")
                    printMatricesSymPy(matrices, matrix2, result2, "tr")

            elif options == 'Resolver un sistema de ecuaciones lineales mediante matrices':
                if matrix1 is None or matrix2 is None:
                    st.error(
                        "Por favor, seleccione una matriz para calcular su traza.")
                else:
                    result = solveMatrix(matrices[matrix1], matrices[matrix2])

                    # Print matrices
                    printMatricesSymPyX2(
                        matrices, matrix1, matrix2, result, "=")

            elif options == 'Matriz triangular':
                if matrix1 is None or matrix2 is None:
                    st.error(
                        "Por favor, seleccione una matriz para calcular su traza.")
                else:
                    result1 = triangularMatrix(matrices[matrix1])
                    result2 = triangularMatrix(matrices[matrix2])

                    # Print matrices
                    printMatricesX1Numpy(matrices, matrix1, result1, "T")
                    printMatricesX1Numpy(matrices, matrix2, result2, "T")

            elif options == 'Matriz triangular superior':
                if matrix1 is None or matrix2 is None:
                    st.error(
                        "Por favor, seleccione una matriz para calcular su traza.")
                else:
                    result1 = upperTriangularMatrix(matrices[matrix1])
                    result2 = upperTriangularMatrix(matrices[matrix2])

                    # Print matrices
                    printMatricesX1Numpy(matrices, matrix1, result1, "U")
                    printMatricesX1Numpy(matrices, matrix2, result2, "U")

            elif options == 'Matriz triangular inferior':
                if matrix1 is None or matrix2 is None:
                    st.error(
                        "Por favor, seleccione una matriz para calcular su traza.")
                else:
                    result1 = lowerTriangularMatrix(matrices[matrix1])
                    result2 = lowerTriangularMatrix(matrices[matrix2])

                    # Print matrices
                    printMatricesX1Numpy(matrices, matrix1, result1, "L")
                    printMatricesX1Numpy(matrices, matrix2, result2, "L")

            elif options == 'Matriz diagonal':
                if matrix1 is None or matrix2 is None:
                    st.error(
                        "Por favor, seleccione una matriz para calcular su traza.")
                else:
                    result1 = diagonalMatrix(matrices[matrix1])
                    result2 = diagonalMatrix(matrices[matrix2])

                    # Print matrices
                    printMatricesSymPy(matrices, matrix1, result1, "D")
                    printMatricesSymPy(matrices, matrix2, result2, "D")

            elif options == 'Factorizacion LU':
                if matrix1 is None or matrix2 is None:
                    st.error(
                        "Por favor, seleccione una matriz para calcular su traza.")
                else:
                    result1 = luMatrix(matrices[matrix1])
                    result2 = luMatrix(matrices[matrix2])

                    # Print matrices
                    printMatricesX1Numpy(matrices, matrix1, result1, "LU")
                    printMatricesX1Numpy(matrices, matrix2, result2, "LU")

    with tab3:
        # Crear un input para la operación
        st.title('Operacion entre matrices')
        st.write(
            'Las funciones disponibles son: +, -, *, /, ^, **,sin(x),cos(x),tan(x),sqrt(x),exp(x),log(x)')
        st.write(
            'Las funciones especiales son: det(), inv(),t(), tr(), triu(), diag(), lu()')

        operacion = st.text_input(
            'Ingrese la operación que desea realizar', value='A+B')

        # Creamos un boton para calcular la operacion
        if st.button('Calcular operacion'):
            result = calcular_operacion(operacion, matrices)

            # try:
            # Calculamos la operacion
            #    result = calcular_operacion(operacion, matrices)
            # except:
            #    st.error("Por favor, ingrese una operacion valida. Por ejemplo : A + B")

    with tab4:
        # Calcular un escalar por una matriz
        st.title('Calcular Matrices por un escalar')
        # Calcular multiplicacion por un escalar
        result = multScalarMatrix(matrices)

        # Print matrices
        printMatricesX1Numpy(matrices, matrix1, result, "k")

    with tab5:
        # Calcular la Eliminacion Gauss-Jordann de una matriz
        st.title('Calcular Eliminacion Gauss-Jordan')
        # Calcular Eliminacion Gauss-Jordan
        result = gaussJordanEliminationMatrix()


# Ejecutar funcion main
if __name__ == '__main__':
    main()
