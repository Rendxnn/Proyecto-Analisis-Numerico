import sympy as sp
import pandas as pd

def newton_method(funcion, initial_guess, tolerance=1e-10, max_iterations=100):
    initial_guess = int(initial_guess)
    tolerance = float(tolerance)
    max_iterations = int(max_iterations)

    x = sp.symbols('x')
    func = sp.sympify(funcion)
    f = sp.lambdify(x, func)
    f_prime = sp.lambdify(x, sp.diff(func, x))

    x_old = initial_guess
    iteration = 0
    tabla_iteraciones = []

    while True:
        x_new = x_old - f(x_old) / f_prime(x_old)
        error = abs(x_new - x_old)
        iteration += 1
        
        tabla_iteraciones.append([iteration, x_old, f(x_old), f_prime(x_old), x_new, error])

        if error < tolerance or iteration >= max_iterations:
            break
        x_old = x_new

    if iteration >= max_iterations:
        print("El método de Newton no converge después de", max_iterations, "iteraciones.")
    else:
        print("Raíz encontrada en:", x_new)
        print("Número de iteraciones:", iteration)

    # Convertir la lista de iteraciones en un DataFrame
    columnas = ["Iteración", "x_old", "f(x_old)", "f'(x_old)", "x_new", "Error"]
    df = pd.DataFrame(tabla_iteraciones, columns=columnas)

    return df

