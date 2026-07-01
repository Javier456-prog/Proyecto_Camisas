from django.contrib import admin
from .models import Camisa, Cliente, Venta, Factura, Empleado, Proveedor

admin.site.register(Camisa)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Factura)
admin.site.register(Empleado)
admin.site.register(Proveedor)
