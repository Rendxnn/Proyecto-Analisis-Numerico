import pandas as pd

def busquedaincremental_method(texto_funcion, valor_inicial, delta, max_iteraciones):
    import cmath
    import sympy as sp

    # Inicializar variables
    resultados = []
    contador = 0
    a_x = valor_inicial
    b_x = valor_inicial + delta

    # Inicializar DataFrame
    data = {'Iteración': [], 'a_x': [], 'b_x': [], 'f(a)': [], 'f(b)': []}
    df = pd.DataFrame(data)

    # Verificar errores
    if max_iteraciones < 0:
        raise ValueError("El número máximo de iteraciones es < 0")
    if delta < 0:
        raise ValueError("Delta es un valor incorrecto")

    # Definir la función
    x = sp.symbols('x')
    funcion = sp.sympify(texto_funcion)

    # Evaluar la función en a y b
    f_a = funcion.subs(x, a_x)
    f_b = funcion.subs(x, b_x)

    # Verificar si f(a) o f(b) es imaginario
    if cmath.phase(f_a) != 0:
        raise ValueError(f"f(a) no está definido en el dominio de la función: xi = {a_x}")
    if cmath.phase(f_b) != 0:
        raise ValueError(f"f(b) no está definido en el dominio de la función: xi = {b_x}")

    # Bucle principal
    while contador < max_iteraciones:
        if f_a * f_b < 0 or f_a * f_b == 0:
            resultados.append(f"Existe una raíz para la función en [{a_x}, {b_x}]")

        # Agregar valores al DataFrame
        df = df.append({'Iteración': contador, 'a_x': a_x, 'b_x': b_x, 'f(a)': f_a, 'f(b)': f_b}, ignore_index=True)

        a_x = b_x
        f_a = f_b
        b_x = b_x + delta
        f_b = funcion.subs(x, b_x)

        if cmath.phase(f_b) != 0:
            raise ValueError(f"f(b) no está definido en el dominio de la función: xi = {b_x}")

        contador += 1

    # Verificar si resultados está vacío
    if not resultados:
        resultados.append(f"No se encontró ninguna raíz en [{valor_inicial}, {b_x}]")

    return df, resultados
