import sympy as sp
import pandas as pd

def raicesmultiples_method(funcion, x0, tolerancia, max_iterations):

    x0 = float(x0)
    tolerancia = float(tolerancia)
    max_iterations = int(max_iterations)
    
    # Convertir la cadena de la función a una expresión sympy
    x = sp.symbols('x')
    func = sp.sympify(funcion)
    f = sp.lambdify(x, func)

    # Calcular la derivada y la segunda derivada de la función
    f_prime = sp.diff(func, x)
    f_double_prime = sp.diff(f_prime, x)

    # Convertir la derivada y la segunda derivada a funciones lambda
    f_prime_lambda = sp.lambdify(x, f_prime)
    f_double_prime_lambda = sp.lambdify(x, f_double_prime)

    # Inicializar la suposición inicial
    x0 = x0

    # Crear lista para almacenar los datos de cada iteración
    tabla_iteraciones = []

    # Iterar hasta que se cumpla el criterio de convergencia o se alcance el número máximo de iteraciones
    for iteracion in range(1, max_iterations + 1):
        fx0 = f(x0)
        fpx0 = f_prime_lambda(x0)
        fppx0 = f_double_prime_lambda(x0)

        error = abs(fx0)
        tabla_iteraciones.append([iteracion, x0, fx0, None, None, error])

        if error < tolerancia:
            break

        x1 = x0 - (fx0 * fpx0) / ((fpx0 ** 2) - fx0 * fppx0)
        fx1 = f(x1)

        tabla_iteraciones[-1][3] = x1
        tabla_iteraciones[-1][4] = fx1

        error = abs(x1 - x0) / abs(x1)
        tabla_iteraciones[-1][-1] = error

        # Actualizar la suposición inicial para la siguiente iteración
        x0 = x1

    # Convertir la lista de iteraciones a un DataFrame de Pandas
    df = pd.DataFrame(tabla_iteraciones, columns=["Iteración", "x0", "f(x0)", "x1", "f(x1)", "Error"])
    
    return df

