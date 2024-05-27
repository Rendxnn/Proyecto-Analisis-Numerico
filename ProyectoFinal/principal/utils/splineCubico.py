import numpy as np
import pandas as pd

def spline_cubico(arreglo_x, arreglo_y):
    x = np.array(eval(arreglo_x))
    y = np.array(eval(arreglo_y))
    
    n = len(x)
    A = np.zeros((4*(n-1), 4*(n-1)))
    b = np.zeros(4*(n-1))
    cua = np.power(x, 2)
    cub = np.power(x, 3)
    
    h = 1
    c = 1
    for i in range(1, n):
        A[i-1, c-1] = cub[i-1]
        A[i-1, c] = cua[i-1]
        A[i-1, c+1] = x[i-1]
        A[i-1, c+2] = 1
        b[i-1] = y[i-1]
        c += 4
        h += 1
    
    c = 1
    for i in range(1, n):
        A[h-1, c-1] = cub[i]
        A[h-1, c] = cua[i]
        A[h-1, c+1] = x[i]
        A[h-1, c+2] = 1
        b[h-1] = y[i]
        c += 4
        h += 1
    
    c = 1
    for i in range(1, n-1):
        A[h-1, c-1] = 3 * cua[i]
        A[h-1, c] = 2 * x[i]
        A[h-1, c+1] = 1
        A[h-1, c+3] = -3 * cua[i]
        A[h-1, c+4] = -2 * x[i]
        A[h-1, c+5] = -1
        b[h-1] = 0
        c += 4
        h += 1
    
    c = 1
    for i in range(1, n-1):
        A[h-1, c-1] = 6 * x[i]
        A[h-1, c] = 2
        A[h-1, c+3] = -6 * x[i]
        A[h-1, c+4] = -2
        b[h-1] = 0
        c += 4
        h += 1
    
    A[h-1, 0] = 6 * x[0]
    A[h-1, 1] = 2
    b[h-1] = 0
    h += 1
    A[h-1, c-1] = 6 * x[-1]
    A[h-1, c] = 2
    b[h-1] = 0
    
    val = np.linalg.solve(A, b)
    
    # Construimos el DataFrame
    polinomios = []
    for i in range(n-1):
        polinomio = f"{val[4*i]:.6f} * x^3 + {val[4*i+1]:.6f} * x^2 + {val[4*i+2]:.6f} * x + {val[4*i+3]:.6f}"
        if i == 0:
            condicion = f"{x[i]:.2f} <= x <= {x[i+1]:.2f}"
        else:
            condicion = f"{x[i]:.2f} < x <= {x[i+1]:.2f}"
        polinomios.append([condicion, polinomio])
    
    df = pd.DataFrame(polinomios, columns=['Intervalo', 'Polinomio'])
    return df