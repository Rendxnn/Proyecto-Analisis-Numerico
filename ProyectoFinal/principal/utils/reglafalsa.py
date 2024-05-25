import pandas as pd
import sympy as sp
import cmath

def reglafalsa_method(Xi, Xs, Tol, Niter, Fun):
    # Convertir los parámetros a los tipos adecuados
    Xi = float(Xi)
    Xs = float(Xs)
    Tol = float(Tol)
    Niter = int(Niter)

    # Crear la variable simbólica y la función a partir de la cadena
    x = sp.symbols('x')
    func = sp.sympify(Fun)
    f = sp.lambdify(x, func, "sympy")

    data = []  # Lista para almacenar los datos de cada iteración
    fm = []
    E = []
    Xmar = []

    # Evaluar la función en los extremos del intervalo
    fi = f(Xi)
    fs = f(Xs)

    # Verificar si alguno de los extremos es raíz
    if fi == 0:
        s = Xi
        E = 0
        print(Xi, "es raíz de f(x)")
    elif fs == 0:
        s = Xs
        E = 0
        print(Xs, "es raíz de f(x)")
    elif fs * fi < 0:
        c = 0
        Xm = Xs - ((fs * (Xs - Xi)) / (fs - fi))
        Xmar.append(Xm)
        fe = f(Xm)
        fm.append(fe)
        E.append(100)
        while E[c] > Tol and fe != 0 and c < Niter:
            if fi * fe < 0:
                Xs = Xm
                fs = f(Xs)
            else:
                Xi = Xm
                fi = f(Xi)

            Xa = Xm
            Xm = Xs - ((fs * (Xs - Xi)) / (fs - fi))
            Xmar.append(Xm)
            fe = f(Xm)
            fm.append(fe)
            Error = abs((Xm - Xa) / Xm)
            E.append(Error)
            c = c + 1
            data.append([c, Xm, fe, "{:.15f}".format(Error)])  # Formateo del error

            if fe == 0:
                s = Xm
                print(s, "es raíz de f(x)", "En iteraciones: ", c + 1)
            elif Error < Tol:
                s = Xm
                print(s, "es una aproximación de una raíz de f(x) con una tolerancia", Tol, "En iteraciones: ", c + 1)
            elif c == Niter:
                s = Xm
                print("Fracaso en ", Niter, " iteraciones ")

    else:
        print("El intervalo es inadecuado")

    # Crear un DataFrame con los datos recopilados
    df = pd.DataFrame(data, columns=['Iteración', 'Xm', 'f(Xm)', 'Error'])
    return df

# Ejemplo de uso:
# print(reglafalsa_method(0, 2, 0.0001, 100, "x**3 - 2*x**2 + x - 3"))
