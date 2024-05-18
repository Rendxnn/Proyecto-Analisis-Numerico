import numpy as np
import pandas as pd
from . import eliminaciongaussSimple

def vandermonde_method(points):
    # Inicializar variables
    results = {
        'matrixA': [],
        'B': [],
        'ai': [],
        'polynom': None,
        'coeffs': []
    }

    # Verificar errores
    if len(set(points['x'])) != len(points['x']):
        raise ValueError(f"X tiene duplicados, un valor de X solo puede ser declarado una vez: puntos x = {points['x']}")
    if len(set(points['y'])) != len(points['y']):
        raise ValueError(f"Y tiene duplicados, un valor de Y solo puede ser declarado una vez: puntos y = {points['y']}")

    # Definir grado
    degree = len(points['x'])

    # Inicializar matrices
    matrixA = np.zeros((degree, degree))
    B = np.zeros((degree, 1))
    ai = ["a_" + str(i + 1) for i in range(degree)]

    # Llenar matrices
    for i in range(degree):
        B[i] = points['y'][i]
        for j in range(degree):
            matrixA[i][j] = points['x'][i] ** (degree - j - 1)

    # Definir resultados
    results['matrixA'] = matrixA
    results['B'] = B
    results['ai'] = ai

    # Aplicar el método gaussSimpleFunction a matrixA y B para obtener x
    x = eliminaciongaussSimple.gaussSimple_method(matrixA, B)
    results['polynom'] = [round(coef, 6) for coef in x]

    # Crear DataFrame
    df = pd.DataFrame(results)

    return df
