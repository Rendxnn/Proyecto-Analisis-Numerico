import pandas as pd
import numpy as np
import math
import sympy as sp

def biseccion_method(funcion, Xi, Xs, Tol, Niter):
    # Inicializamos listas para almacenar datos de cada iteración
    Xi = float(Xi)
    Xs = float(Xs)
    Niter = int(Niter)
    Tol = float(Tol)

    Xmar = []
    fm = []
    E = []

    # Convertimos la cadena de la función a una expresión sympy
    x = sp.symbols('x')
    func = sp.sympify(funcion)

    # Evaluamos la función en los extremos del intervalo
    fi = func.subs(x, Xi)
    fs = func.subs(x, Xs)

    # Verificamos si alguno de los extremos es raíz
    if fi == 0:
        s = Xi
        E = 0
        print(Xi, "es raiz de f(x)")
    elif fs == 0:
        s = Xs
        E = 0
        print(Xs, "es raiz de f(x)")
    elif fs * fi < 0:
        c = 0
        Xm = (Xi + Xs) / 2
        Xmar.append(Xm)
        fe = func.subs(x, Xm)
        fm.append(fe)
        E.append(100)

        # Comenzamos las iteraciones de bisección
        while E[c] > Tol and fe != 0 and c < Niter:
            if fi * fe < 0:
                Xs = Xm
                fs = func.subs(x, Xs)
            else:
                Xi = Xm
                fi = func.subs(x, Xi)

            Xa = Xm
            Xm = (Xi + Xs) / 2
            Xmar.append(Xm)
            fe = func.subs(x, Xm)
            fm.append(fe)
            Error = abs(Xm - Xa)
            E.append(Error)
            c = c + 1

            if fe == 0:
                s = Xm
                print(s, "es raiz de f(x)", "En iteraciones: ", c + 1)
            elif Error < Tol:
                s = Xm
                print(s, "es una aproximacion de un raiz de f(x) con una tolerancia", Tol, "En iteraciones: ",
                      c + 1)
                print("Fm", fm)
                print("Error", E)
                print("Xmi: ", Xmar)
            elif c == Niter:
                s = Xm
                print("Fracaso en ", Niter, " iteraciones ")

    else:
        print("El intervalo es inadecuado")

    # Creamos un DataFrame con los resultados de las iteraciones
    df = pd.DataFrame(
        {"Iteración": range(1, c + 2), "Xm": Xmar, "f(Xm)": fm, "Error": E}
    )

    return df

# Ejemplo de uso:
# resultados_biseccion = metodo_biseccion(Xi=0, Xs=1, Tol=0.0001, Niter=10, Funcion="x**2 - 2")
# print(resultados_biseccion)


# Ejemplo de uso:
# resultados_biseccion = metodo_biseccion(Xi=0, Xs=1, Tol=0.0001, Niter=10, Funcion="x**2 - 2")
# print(resultados_biseccion)
#print(metodo_biseccion(2,4,5e-5,100,"(x**2) -13"))
