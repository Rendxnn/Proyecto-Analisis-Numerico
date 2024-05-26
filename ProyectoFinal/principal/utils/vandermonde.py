import numpy as np
import pandas as pd

def interpolacion_vandermonde(arreglo_x, arreglo_y):
    x = np.array(eval(arreglo_x))
    y = np.array(eval(arreglo_y))
    # Cantidad de puntos
    n = len(x)

    # Construcción de la matriz de Vandermonde y el vector b
    A = np.zeros((n, n))
    for i in range(n):
        A[:, i] = x**(n-1-i)
    b = y

    # Solución del sistema de ecuaciones
    a = np.linalg.solve(A, b)

    # Construcción del polinomio en forma de cadena de texto
    polinomio = f'P(x) = '
    for i in range(n):
        polinomio += f'{a[i]:.4f} * x^{n-1-i}'
        if i < n-1:
            polinomio += ' + '

    # Creación del DataFrame para el polinomio
    df_polinomio = pd.DataFrame([polinomio], columns=['Polinomio Interpolante'])

    # Retorno del DataFrame con el polinomio
    return df_polinomio
