import requests
from django.shortcuts import render
from datetime import date

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
        response = requests.get(api_url, timeout=5)

        print("Código de respuesta:", response.status_code)

        if response.status_code == 200:
            datos = response.json()
        else:
            datos = []
            print("Error al consumir la API:")
            print(response.text)

    except Exception as e:
        datos = []
        print("❌ Error de conexión API:", e)

    if modelo == "camisas":
        return render(request, "camisas.html", {
            "datos": datos
        })

    return render(request, "lista_dinamica.html", {
        "datos": datos,
        "modelo": modelo
    })


def registrar_venta(request):

    # ============================
    # Cargar datos desde la API
    # ============================

    try:
        clientes = requests.get(
            "http://127.0.0.1:8000/api/clientes/",
            timeout=5
        ).json()

    except Exception as e:
        print("Error clientes:", e)
        clientes = []

    try:
        empleados = requests.get(
            "http://127.0.0.1:8000/api/empleados/",
            timeout=5
        ).json()

    except Exception as e:
        print("Error empleados:", e)
        empleados = []

    try:
        camisas = requests.get(
            "http://127.0.0.1:8000/api/camisas/",
            timeout=5
        ).json()

    except Exception as e:
        print("Error camisas:", e)
        camisas = []

    total = None
    mensaje = ""

    cliente_sel = ""
    empleado_sel = ""
    camisa_sel = ""
    cantidad_sel = ""

    if request.method == "POST":

        print("\n===== FORMULARIO RECIBIDO =====")
        print(request.POST)

        cliente_sel = request.POST.get("cliente", "")
        empleado_sel = request.POST.get("empleado", "")
        camisa_sel = request.POST.get("camisa", "")
        cantidad_sel = request.POST.get("cantidad", "")

        try:
            cantidad = int(cantidad_sel)
        except ValueError:
            cantidad = 0

        if not cliente_sel or not empleado_sel or not camisa_sel or cantidad <= 0:

            mensaje = "❌ Complete todos los campos."

        else:

            camisa_seleccionada = None

            for camisa in camisas:
                if str(camisa["id_camisa"]) == str(camisa_sel):
                    camisa_seleccionada = camisa
                    break

            if camisa_seleccionada:

                precio = float(camisa_seleccionada["precio"])
                total = precio * cantidad

                datos = {
                    "fecha": str(date.today()),
                    "producto": camisa_seleccionada["marca"],
                    "total": total,
                    "id_empleado": int(empleado_sel)
                }

                print("\n========== DATOS ENVIADOS ==========")
                print(datos)

                try:

                    respuesta = requests.post(
                        "http://127.0.0.1:8000/api/ventas/",
                        json=datos,
                        timeout=5
                    )

                    print("\n========== STATUS ==========")
                    print(respuesta.status_code)

                    print("\n========== RESPUESTA ==========")
                    print(respuesta.text)

                    if respuesta.status_code == 201:

                        mensaje = "✅ Venta registrada correctamente."

                        cliente_sel = ""
                        empleado_sel = ""
                        camisa_sel = ""
                        cantidad_sel = ""

                    else:

                        mensaje = f"❌ Error {respuesta.status_code}"
                        print(respuesta.text)

                except Exception as e:

                    import traceback
                    traceback.print_exc()

                    mensaje = f"❌ Error de conexión: {e}"

            else:

                mensaje = "❌ Camisa no encontrada."

    return render(request, "registrar_venta.html", {
        "clientes": clientes,
        "camisas": camisas,
        "empleados": empleados,
        "total": total,
        "mensaje": mensaje,
        "cliente_sel": cliente_sel,
        "empleado_sel": empleado_sel,
        "camisa_sel": camisa_sel,
        "cantidad_sel": cantidad_sel
    })