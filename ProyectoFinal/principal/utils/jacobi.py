import numpy as np
import pandas as pd

def jacobi_method(A, b, x0, tol, niter):
    tol = float(tol)
    niter = int(niter)
    A = np.array(eval(A))
    b = np.array(eval(b))
    x0 = np.array(eval(x0))

    c = 0
    error = tol + 1
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    iteraciones = []
    x_values = []
    errores = []

    while error > tol and c < niter:
        T = np.linalg.inv(D).dot(L + U)
        C = np.linalg.inv(D).dot(b)
        x1 = T.dot(x0) + C

        error = np.linalg.norm((x1 - x0) / x1, np.inf)
        x0 = x1
        c += 1
        iteraciones.append(c)
        x_values.append(x0)
        errores.append(error)

    if error < tol:
        s = x0
        mensaje = f"Es una aproximación de la solución del sistema con una tolerancia = {tol}"
    else:
        s = x0
        mensaje = f"Fracasó en {niter} iteraciones"

    # Crear un DataFrame con los resultados
    df = pd.DataFrame(x_values, columns=[f'X{i+1}' for i in range(x0.size)])
    df['Iteración'] = iteraciones
    df['Error'] = errores

    # Reorganizar las columnas para que la iteración aparezca primero
    cols = ['Iteración'] + [f'X{i+1}' for i in range(x0.size)] + ['Error']
    df = df[cols]

    return df
