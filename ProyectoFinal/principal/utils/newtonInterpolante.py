import numpy as np
import pandas as pd

def Newtonint(x, y):
    n = len(x)
    Tabla = np.zeros((n, n + 1))
    Tabla[:, 0] = x
    Tabla[:, 1] = y
    for j in range(2, n + 1):
        for i in range(j - 1, n):
            Tabla[i, j] = (Tabla[i, j - 1] - Tabla[i - 1, j - 1]) / (Tabla[i, 0] - Tabla[i - j + 1, 0])
    
    coeficientes = np.diag(Tabla[:, 1:]) 
    return coeficientes

def Newtonor(x, coef):
    n = len(x)
    pol = np.array([1.])
    acum = pol.copy()
    pol = coef[0] * acum
    for i in range(n - 1):
        pol = np.insert(pol, 0, 0)
        acum = np.convolve(acum, [1, -x[i]])
        pol = pol + coef[i + 1] * acum
    return pol

def newton_interpolante(arreglo_x, arreglo_y):
    x = np.array(eval(arreglo_x))
    y = np.array(eval(arreglo_y))

    coeficientes = Newtonint(x, y)
    polinomio = Newtonor(x, coeficientes)
    degree = len(polinomio) - 1
    terms = []
    for i, coef in enumerate(polinomio):
        power = degree - i
        term = f"{coef:.4f} * x^{power}"
        terms.append(term)
    
    polynomial_str = "P(x) = " + " + ".join(terms)
    return pd.DataFrame([[polynomial_str]], columns=['Polinomio Solución'])