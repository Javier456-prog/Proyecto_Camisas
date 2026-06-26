import requests
from django.shortcuts import render

MODELS_MAP = {
    'camisas': 'camisas',
    'clientes': 'clientes',
    'proveedores': 'proveedores',
    'ventas': 'ventas',
    'facturas': 'facturas',
    'empleados': 'empleados',
}

def listar_datos(request, modelo):

    api_url = f'http://127.0.0.1:8000/api/{MODELS_MAP.get(modelo, modelo)}/'

    try:
        response = requests.get(api_url)
        datos = response.json()
    except:
        datos = []

    if modelo == "camisas":
        return render(request, "camisas.html", {
            "datos": datos
        })

    return render(request, "lista_dinamica.html", {
        "datos": datos,
        "modelo": modelo
    })