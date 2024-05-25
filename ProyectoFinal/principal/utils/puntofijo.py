import sympy as sp
import pandas as pd

def puntofijo_method(funcion, g, x0, tol, niter):
    x0 = float(x0)
    tol = float(tol)
    niter = int(niter)
    
    x = sp.symbols('x')
    func = sp.sympify(funcion)
    g_func = sp.sympify(g)
    
    f = sp.lambdify(x, func, "numpy")
    g = sp.lambdify(x, g_func, "numpy")
    
    tabla_iteraciones = []
    E = float('inf')
    i = 0
    
    while i < niter and E > tol:
        x1 = g(x0)
        fx1 = f(x1)
        E = abs(x1 - x0)
        
        tabla_iteraciones.append([i, x0, x1, fx1, E])
        
        if E < tol:
            break
        
        x0 = x1
        i += 1
    
    if i >= niter:
        print("El método de punto fijo no converge después de", niter, "iteraciones.")
    else:
        print("Raíz encontrada en:", x1)
        print("Número de iteraciones:", i)
    
    df = pd.DataFrame(tabla_iteraciones, columns=["Iteración", "x0", "x1", "f(x1)", "Error"])
    
    return df

# Ejemplo de uso:
#print(punto_fijo("-7*log(x)+x-13", "7*log(x)+13", 30, 0.5e-5, 100))
