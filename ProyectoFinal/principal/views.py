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
import numpy as np
from bokeh.plotting import figure
from bokeh.embed import components

def home(request):
    metodos_diccionario = {"newton": newton.newton_method, "secante": secante.metodo_secante, "biseccion": biseccion.biseccion_method, "puntofijo": puntofijo.puntofijo_method, "busquedaincremental": busquedaincremental.busquedaincremental_method, "reglafalsa": reglafalsa.reglafalsa_method, "raicesmultiples2": raicesmultiples2.raicesmultiples_method  }
    metodo = request.GET.get("metodo")
    variables_metodo = None
    tabla_resultado = None

    if metodo:
        parametros_metodo = inspect.signature(metodos_diccionario[metodo]).parameters.items()

        variables_metodo = [x[0] for x in parametros_metodo]

        entradas_metodo = [request.GET.get(f'{x}_entrada') for x in variables_metodo]

        if entradas_metodo[0]: 

            tabla_resultado = metodos_diccionario[metodo](*entradas_metodo).to_html(index=False)

    #GRAFICAR
    funcion = request.GET.get('funcion_entrada')
    script, div = None, None
    if funcion:
        x = np.linspace(-10, 10, 400)
        y = eval(funcion)  

        plot = figure(title=f'Gráfica de la función {funcion}', x_axis_label='x', y_axis_label='y')
        plot.line(x, y, legend_label=funcion, line_width=2)
        script, div = components(plot)

    print(tabla_resultado)

    return render(request, 'home.html', {
        "metodo": metodo,
        "variables_metodo": variables_metodo,
        "tabla_resultado": tabla_resultado,
        'script': script,
        'div': div
    })

