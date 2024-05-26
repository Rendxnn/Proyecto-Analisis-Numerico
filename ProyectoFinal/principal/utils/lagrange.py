import numpy as np
import pandas as pd

def lagrange_interpolation(arreglo_x, arreglo_y):
    x = np.array(eval(arreglo_x))
    y = np.array(eval(arreglo_y))

    n = len(x)
    tabla = np.zeros((n, n))
    
    for i in range(n):
        Li = np.array([1])
        den = 1
        for j in range(n):
            if j != i:
                paux = np.array([1, -x[j]])
                Li = np.convolve(Li, paux)
                den *= (x[i] - x[j])
        tabla[i, :] = y[i] * Li / den
    
    pol = np.sum(tabla, axis=0)
    pol_str = polynomial_to_string(pol)
    return pd.DataFrame([[pol_str]], columns=['Polinomio Solución'])

def polynomial_to_string(coefficients):
    terms = []
    n = len(coefficients)
    for i in range(n):
        coef = coefficients[i]
        power = n - i - 1
        if coef != 0:
            if power == 0:
                term = f"{coef:.4f} * x^{power}"
            elif power == 1:
                term = f"{coef:.4f} * x"
            else:
                term = f"{coef:.4f} * x^{power}"
            terms.append(term)
    
    polynomial_str = " + ".join(terms)
    return f"P(x) = {polynomial_str.replace('+ -', '- ')}"