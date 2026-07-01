from rest_framework import serializers
from .models import Camisa, Cliente, DetalleFactura, Empleado, Factura, Personalizacion, Proveedor, Venta

class CamisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camisa
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class DetalleFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleFactura
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class PersonalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalizacion
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'
        read_only_fields = ['id_venta']