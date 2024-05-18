from django.shortcuts import render
from django.http import JsonResponse
from .metodos import *
import json
import inspect
from .utils import newton 
from .utils import secante
from .utils import biseccion
from .utils import puntofijo


def home(request):
    metodos_diccionario = {"newton": newton.newton_method, "secante": secante.metodo_secante, "biseccion": biseccion.biseccion_method, "puntofijo": puntofijo.puntofijo_method}
    metodo = request.GET.get("metodo")
    variables_metodo = None
    tabla_resultado = None

    if metodo:
        parametros_metodo = inspect.signature(metodos_diccionario[metodo]).parameters.items()

        variables_metodo = [x[0] for x in parametros_metodo]

        entradas_metodo = [request.GET.get(f'{x}_entrada') for x in variables_metodo]

        if entradas_metodo[0]: 

            tabla_resultado = metodos_diccionario[metodo](*entradas_metodo).to_html(index=False)




    return render(request, 'home.html', {"metodo": metodo, "variables_metodo": variables_metodo, "tabla_resultado": tabla_resultado})