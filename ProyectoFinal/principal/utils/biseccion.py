import pandas as pd
import numpy as np
import math

def biseccion_method(Xi, Xs, Tol, Niter, Fun):
    data = [] # This will store our data
    x=Xi #Indica el valor de x, siendo este el primero del intervalo
    fi=eval(Fun) #Evalua la funcion en el valor de x inicial

    x=Xs
    fs=eval(Fun) #Evalua la funcion en el valor de x final

    if fi==0:
        s=Xi
        E=0
        data.append([0, Xi, fi, E])
    elif fs==0:
        s=Xs
        E=0
        data.append([0, Xs, fs, E])
    elif fs*fi<0: #Si la multiplicacion de las funciones es menor a 0, entonces se puede aplicar el metodo. Cambio de signo
        c=0 # Creo que es un contador
        Xm=(Xi+Xs)/2 #Nueva aproximacion de la raiz
        x=Xm         # X = el nuevo valor           
        fe=eval(Fun) #Evalua la funcion en el nuevo valor de x
        E=100
        data.append([c, Xm, fe, E])

        while E>Tol and fe!=0 and c<Niter:
            if fi*fe<0: #Significa que la funcion cambia de signo 
                Xs=Xm #Cambia el valor de Xs con el Xm actual (En otras palabras es como tener un nuevo B)
                x=Xs #Asigna a x el valor del nuevo Xs (nuevo B)   
                fs=eval(Fun) #Evalua la funcion en el nuevo valor de x
            else:
                Xi=Xm #No cambia de signo entonces sigue siendo una A
                x=Xi #Asigna a x el el valor del nuevo Xi (nuevo A)
                fs=eval(Fun) #Evalua la funcion en el nuevo valor de x
            Xa=Xm #X auxiliar para calcular el error
            Xm=(Xi+Xs)/2 #Nueva aproximacion de la raiz
            x=Xm #X a evaluar
            fe=eval(Fun) #Evalua la funcion en el nuevo valor de x
            Error=abs(Xm-Xa) #CAlcula el error
            c=c+1 #Aumenta el contador
            data.append([c, Xm, fe, Error])
        if fe==0: #Encontro raiz
            s=x
            print(s,"es raiz de f(x)")
        elif Error<Tol: #Es una aproximacion con la presicion deseada
            s=x
            print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
        else: #Fracaso
            s=x
            print("Fracaso en ",Niter, " iteraciones ") 
    else: 
        print("El intervalo es inadecuado")
    
    df = pd.DataFrame(data, columns=['Iteración', 'Xm', 'f(Xm)', 'Error'])
    return df
