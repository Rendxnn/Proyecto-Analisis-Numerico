import pandas as pd
import numpy as np
import math

def puntofijo_method(X0, Tol, Niter, Fun, g):
    data = [] # This will store our data
    x=X0
    f=eval(Fun)
    c=0
    Error=100               
    data.append([c, x, f, Error])

    while Error>Tol and f!=0 and c<Niter:
        x=eval(g)
        fe=eval(Fun)
        c=c+1
        Error=abs(x-data[c-1][1])
        data.append([c, x, fe, Error])	
    if fe==0:
        s=x
        print(s,"es raiz de f(x)")
    elif Error<Tol:
        s=x
        print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
    else:
        s=x
        print("Fracaso en ",Niter, " iteraciones ") 

    df = pd.DataFrame(data, columns=['Iteración', 'Xn', 'f(Xn)', 'Error'])
    return df
