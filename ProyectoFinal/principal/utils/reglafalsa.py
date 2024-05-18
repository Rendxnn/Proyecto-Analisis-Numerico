import pandas as pd
import sympy as sp
import cmath

def reglafalsa_method(texto_funcion, a, b, tol, max_iteraciones):
    # Inicializar variables
    count = 1

    # Verificar errores
    if max_iteraciones < 0:
        raise ValueError(f"El número máximo de iteraciones es < 0: iteraciones = {max_iteraciones}")
    if a >= b:
        raise ValueError(f"a tiene que ser menor que b: a = {a} ^ b = {b}")

    # Definir la función
    x = sp.symbols('x')
    funcion = sp.sympify(texto_funcion)

    # Evaluar la función en a y b
    f_a = funcion.subs(x, a)
    f_b = funcion.subs(x, b)

    # Verificar si f(a) o f(b) es imaginario
    if cmath.phase(f_a) != 0:
        raise ValueError(f"a no está definido en el dominio de la función: a = {a}")
    if cmath.phase(f_b) != 0:
        raise ValueError(f"b no está definido en el dominio de la función: b = {b}")

    if tol < 0:
        raise ValueError(f"tol es un valor incorrecto: tol = {tol}")

    # Inicializar variables
    x_r = b - (f_b * (a - b)) / (f_a - f_b)
    f_xr = funcion.subs(x, x_r)
    error = tol + 1
    temp = 0

    # Inicializar DataFrame
    data = {'Iteración': [count], 'a': [a], 'x_r': [x_r], 'b': [b], 'f(x_r)': [f_xr], 'error': [""], 'conclusión': [""]}
    df = pd.DataFrame(data)

    # Bucle principal
    while error > tol and count < max_iteraciones:
        if f_xr < 0:
            a = x_r
        if f_xr > 0:
            b = x_r

        count += 1
        temp = x_r
        x_r = b - (f_b * (a - b)) / (f_a - f_b)
        f_xr = funcion.subs(x, x_r)
        error = abs(x_r - temp)

        f_a = funcion.subs(x, a)
        f_b = funcion.subs(x, b)

        if cmath.phase(f_a) != 0:
            raise ValueError(f"a no está definido en el dominio de la función: a = {a}")
        if cmath.phase(f_b) != 0:
            raise ValueError(f"b no está definido en el dominio de la función: b = {b}")

        df = df.append({'Iteración': count, 'a': a, 'x_r': x_r, 'b': b, 'f(x_r)': f_xr, 'error': error, 'conclusión': ""}, ignore_index=True)

    # Definir conclusion
    if error < tol:
        conclusion = f"Se encontró una aproximación de la raíz para m = {x_r}"
    elif error > tol:
        conclusion = "Dado el número de iteraciones y la tolerancia, fue imposible encontrar una raíz satisfactoria"
    else:
        conclusion = "El método explotó"

    df.at[count-1, 'conclusión'] = conclusion

    return df
