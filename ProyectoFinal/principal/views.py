from django.shortcuts import render
from django.http import JsonResponse
from .metodos import *
import json


def home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        metodo = data.get('opciones')
        print(metodo)
    return render(request, 'home.html')