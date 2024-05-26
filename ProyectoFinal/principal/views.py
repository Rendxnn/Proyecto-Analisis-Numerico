from django.shortcuts import render
from django.http import JsonResponse
import json
import inspect
from .utils import newton 
from .utils import secante
from .utils import biseccion
from .utils import puntofijo
from .utils import busquedaincremental
from .utils import reglafalsa
from .utils import raicesmultiples2
from .utils import jacobi
from .utils import seidel
from .utils import sor
from .utils import vandermonde
from .utils import newtonInterpolante
import math

import numpy as np
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import Span


def home(request):
    metodos_diccionario = {"newton": newton.newton_method, "secante": secante.metodo_secante, 
                           "biseccion": biseccion.biseccion_method, "puntofijo": puntofijo.puntofijo_method, 
                           "busquedaincremental": busquedaincremental.busquedaincremental_method, 
                           "reglafalsa": reglafalsa.reglafalsa_method, "raicesmultiples2": raicesmultiples2.raicesmultiples_method,
                           "jacobi": jacobi.jacobi_method,
                           "seidel": seidel.seidel_method,
                           "sor": sor.sor_method,
                           "vandermonde": vandermonde.interpolacion_vandermonde,
                           "newtonInterpolante": newtonInterpolante.newton_interpolante }
    metodo = request.GET.get("metodo")
    variables_metodo = None
    tabla_resultado = None

    if metodo:
        parametros_metodo = inspect.signature(metodos_diccionario[metodo]).parameters.items()

        variables_metodo = [x[0] for x in parametros_metodo]

        entradas_metodo = [request.GET.get(f'{x}_entrada') for x in variables_metodo]

        if entradas_metodo[0]: 

            tabla_resultado = metodos_diccionario[metodo](*entradas_metodo).to_html(classes='table table-striped table-dark', index=False, justify='center')

    #GRAFICAR
    funcion = request.GET.get('funcion_entrada')
    script, div = None, None
    if funcion:
        safe_dict = {**math.__dict__, **np.__dict__}

        safe_dict['x'] = np.linspace(-100, 100, 2000)

        try:
            y = eval(funcion, {"__builtins__": None}, safe_dict)
            plot = figure(
                title=f'Gráfica de la función {funcion}', 
                x_axis_label='x', 
                y_axis_label='y', 
            )
            plot.line(safe_dict['x'], y, legend_label=funcion, line_width=2)
            plot.xaxis.axis_line_width = 3
            plot.yaxis.axis_line_width = 3
            x_axis = Span(location=0, dimension='width', line_color='black', line_width=3)
            plot.add_layout(x_axis)
            y_axis = Span(location=0, dimension='height', line_color='black', line_width=3)
            plot.add_layout(y_axis)
            plot.x_range.start = -100
            plot.x_range.end = 100
            plot.y_range.start = -100
            plot.y_range.end = 100
            script, div = components(plot)


        except Exception as e:
            print(f"Error al evaluar la función: {e}")
    
    return render(request, 'home.html', {
        "metodo": metodo,
        "variables_metodo": variables_metodo,
        "tabla_resultado": tabla_resultado,
        'script': script,
        'div': div
    })

