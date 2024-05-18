import numpy as np
from scipy.linalg import solve_triangular

def gaussSimpleFunction(matrixA, B):
    results = {
        'iterations': [],
        'conclusion': None,
        'finalSolution': []
    }
    m = len(matrixA)
    n = len(matrixA[0])
    
    if m != n:
        raise ValueError("La matriz no es cuadrada")
    
    if m != len(B):
        raise ValueError("B tiene una dimensión diferente")
    
    if np.linalg.det(matrixA) == 0:
        raise ValueError("El determinante de la matriz no puede ser cero")
    
    M = np.zeros((n, n + 1))
    
    for i in range(n):
        for j in range(n):
            M[i][j] = matrixA[i][j]
        M[i][n] = B[i][0]
    
    results['iterations'].append(np.copy(M))
    
    for i in range(n - 1):
        if M[i][i] == 0:
            for j in range(i + 1, n):
                if M[j][i] != 0:
                    aux = np.copy(M[j])
                    M[j] = np.copy(M[i])
                    M[i] = aux
                    break
        
        for j in range(i + 1, n):
            if M[j][i] != 0:
                auxOp = np.zeros(n + 1)
                for k in range(i, n + 1):
                    auxOp[k] = M[j][k] - (M[j][i] / M[i][i]) * M[i][k]
                
                for k in range(i, n + 1):
                    M[j][k] = auxOp[k]
        
        results['iterations'].append(np.copy(M))
    
    resultX = solve_triangular(M[:, :n], M[:, n], lower=False)
    results['conclusion'] = "Después de aplicar la sustitución regresiva obtenemos:"
    results['finalSolution'] = resultX.tolist()
    
    return results
