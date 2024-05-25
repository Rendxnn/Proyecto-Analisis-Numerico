import pandas as pd
import sympy as sp

def busquedaincremental_method(funcion, X0, Delta, Niter):
    X0 = float(X0)
    Delta = float(Delta)
    Niter = int(Niter)

    # Inicializamos listas para almacenar datos de cada iteración
    iteraciones = []
    xi_vals = []
    fxi_vals = []

    # Convertimos la cadena de la función a una expresión sympy
    x = sp.symbols('x')
    func = sp.sympify(funcion)

    # Evaluamos la función en el punto inicial
    f0 = func.subs(x, X0)

    if f0 == 0:
        print(X0, "es raiz de f(x)")
        iteraciones.append(0)
        xi_vals.append(X0)
        fxi_vals.append(f0)
    else:
        X1 = X0 + Delta
        f1 = func.subs(x, X1)
        i = 1
        iteraciones.append(i)
        xi_vals.append(X1)
        fxi_vals.append(f1)
        print("\n----------------TABLA----------------")
        print("i =", i, " xi =", X1, " f(xi) =", f1)

        while f0 * f1 > 0 and i < Niter:
            X0 = X1
            f0 = f1
            X1 = X0 + Delta
            f1 = func.subs(x, X1)
            i += 1
            iteraciones.append(i)
            xi_vals.append(X1)
            fxi_vals.append(f1)
            print("i =", i, " xi =", X1, " f(xi) =", f1)

        if f1 == 0:
            print(X1, "\nes raiz de f(x)")
        elif f0 * f1 < 0:
            print("\nExiste una raiz de f(x) entre ", X0, " y ", X1, "\n")
        else:
            print("\nFracaso en ", Niter, " iteraciones ")

    # Creamos un DataFrame con los resultados de las iteraciones
    df = pd.DataFrame({
        "Iteración": iteraciones,
        "xi": xi_vals,
        "f(xi)": fxi_vals
    })

    return df

# Ejemplo de uso:
# resultados_busqueda_incremental = busquedaincremental_method("x**2 - 4", 0, 0.5, 10)
# print(resultados_busqueda_incremental)
