from rest_framework import viewsets
from .models import Camisa, Cliente, DetalleFactura, Empleado, Factura, Personalizacion, Proveedor, Venta
from .serializers import *

class CamisaViewSet(viewsets.ModelViewSet):
    queryset = Camisa.objects.all()
    serializer_class = CamisaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class DetalleFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class PersonalizacionViewSet(viewsets.ModelViewSet):
    queryset = Personalizacion.objects.all()
    serializer_class = PersonalizacionSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer