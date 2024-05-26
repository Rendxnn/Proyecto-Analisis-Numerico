import sympy as sp
import pandas as pd

def metodo_secante(funcion, x0, x1, tolerancia, numero_iteraciones):
	x1 = float(x1)
	x0 = float(x0)
	tolerancia = float(tolerancia)
	numero_iteraciones = int(numero_iteraciones)

	x = sp.symbols('x')
	func = sp.sympify(funcion)
	f = sp.lambdify(x, func)

	tabla_iteraciones = []

	for iteracion in range(1, numero_iteraciones + 1):
		x_siguiente = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
		error = abs(x1 - x0)

		tabla_iteraciones.append([iteracion, x0, x1, error])

		if error < tolerancia:
			break

		x0 = x1
		x1 = x_siguiente

	if iteracion >= numero_iteraciones:
		print("El método de la secante no converge después de", numero_iteraciones, "iteraciones.")

	return pd.DataFrame(tabla_iteraciones, columns=["Iteración", "x0", "x1", "Error"])
