import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp



def bisection(equation, a, b, error_tolerance):

    # Convierte la cadena de caracteres en una función que puede evaluarse
    equation = sp(equation)
    # Inicializar i con un valor predeterminado
    i = 0
    # Comprueba si la función tiene valores opuestos en los límites
    if equation.subs('x', a) * equation.subs('x', b) > 0:
        return "La función no cambia de signo en el intervalo especificado. Inténtalo de nuevo con un intervalo diferente."

    # Bucle while que se ejecuta hasta que la aproximación converge al valor deseado
    while abs(b - a) > error_tolerance:
        # Encuentra el punto medio del intervalo
        c = (a + b) / 2
        # Incrementa el contador de iteraciones
        i += 1
        # Calcula los valores de la función en los puntos a, b y c
        fa = equation.subs('x', a)
        fb = equation.subs('x', b)
        fc = equation.subs('x', c)
        # Comprueba en qué mitad del intervalo se encuentra la raíz
        if fa * fc < 0:
            b = c
        else:
            a = c
    # Retorna la aproximación de la raíz, la precisión y el número de iteraciones
    return c, abs(b - a), i



def false_position(f, a, b, tol, max_iter):

    fa = f(a)
    fb = f(b)

    # Verificar que el signo de la función sea distinto en a y b
    if fa * fb >= 0:
        raise ValueError("La función debe tener signos opuestos en a y b")

    error = np.zeros(max_iter)
    x = np.zeros(max_iter)
    x[0] = a

    for i in range(max_iter):
        # Calcular la siguiente aproximación
        x[i+1] = (a * fb - b * fa) / (fb - fa)
        fx = f(x[i+1])

        # Verificar si se alcanza la tolerancia
        if abs(fx) < tol:
            return x[i+1], i

        # Verificar si se ha excedido el número máximo de iteraciones
        if i == max_iter - 1:
            raise ValueError("El método de la regla falsa no converge después de %d iteraciones" % max_iter)

        # Verificar si se ha encontrado la raíz
        if abs(x[i+1] - x[i]) < tol:
            return x[i+1], i

       





def f(eq):

    return eval(eq)


def solve_equation(method, eq, a, b, tol, max_iterations=100):


    # Validar que `a` y `b` encierran una raíz
    fa = f(a, eq)
    fb = f(b, eq)
    if fa * fb >= 0:
        return None

    # Inicializar variables
    x = np.zeros(max_iterations)
    error = np.zeros(max_iterations)

    # Definir i con un valor predeterminado
    i = 0
    # Bisección
    if method == 'Bisección':
        for i in range(max_iterations):
            # Calcular el punto medio del intervalo
            c = (a + b) / 2
            fc = f(c, eq)
            x[i] = c

            # Verificar si se encontró la raíz
            if abs(fc) < tol:
                break

            # Reducir el intervalo
            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc

            # Calcular el error
            if i > 0:
                error[i] = abs(x[i] - x[i-1]) / abs(x[i])

        # Crear la gráfica y la tabla
        fig, ax = plt.subplots()
        x_values = np.linspace(a, b, 100)
        y_values = f(x_values, eq)
        ax.plot(x_values, y_values)
        ax.plot(x[:i+1], np.zeros(i+1), 'ro')
        table_data = np.vstack((x[:i+1], error[1:i+1])).T
        headers = ['Raíz', 'Error']
        return fig, pd.DataFrame(table_data, columns=headers)

    # Regula Falsi
    elif method == 'Regula Falsi':
        for i in range(max_iterations):
            # Calcular la nueva aproximación
            c = (a * fb - b * fa) / (fb - fa)
            fc = f(c, eq)
            x[i] = c

            # Verificar si se encontró la raíz
            if abs(fc) < tol:
                break

    # Reducir el intervalo
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        # Calcular el error
        if i > 0:
            error[i] = abs(x[i] - x[i-1]) / abs(x[i])

    # Crear la gráfica y la tabla
    fig, ax = plt.subplots()
    x_values = np.linspace(a, b, 100)
    y_values = f(x_values, eq)
    ax.plot(x_values, y_values)
    if i is None:
        i = 0
    ax.plot(x[:i+1], np.zeros(i+1), 'ro')
    table_data = np.vstack((x[:i+1], error[1:i+1])).T
    headers = ['Raíz', 'Error']
    return fig, pd.DataFrame(table_data, columns=headers)

# Ejemplo de uso de la función
fig, table = solve_equation('Bisection', 'x**2 - 2', 0, 2, 0.0001)
if fig is not None:
    plt.show()
    print(table)
else:
    print('No se encontró la raíz.')
