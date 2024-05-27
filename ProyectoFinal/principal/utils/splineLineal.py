import numpy as np
import pandas as pd

def spline_lineal(arreglo_x, arreglo_y):
    x = np.array(eval(arreglo_x))
    y = np.array(eval(arreglo_y))
    
    n = len(x)
    A = np.zeros((2*(n-1), 2*(n-1)))
    b = np.zeros(2*(n-1))
    
    h = 1
    c = 1
    for i in range(1, n):
        A[i-1, c-1] = x[i-1]
        A[i-1, c] = 1
        b[i-1] = y[i-1]
        c += 2
        h += 1
    
    c = 1
    for i in range(1, n):
        A[h-1, c-1] = x[i]
        A[h-1, c] = 1
        b[h-1] = y[i]
        c += 2
        h += 1
    
    val = np.linalg.solve(A, b)
    tabla = np.reshape(val, (2, n-1))
    tabla = tabla.transpose()
    
    polinomios = []
    intervalos = []
    for i in range(n-1):
        intervalo = f"{x[i]:.2f} <= x <= {x[i+1]:.2f}"
        polinomio = f"{val[2*i]:.6f} * x + {val[2*i+1]:.6f}"
        intervalos.append(intervalo)
        polinomios.append(polinomio)
    
    df = pd.DataFrame({"Intervalo": intervalos, "Polinomio": polinomios})
    
    return df