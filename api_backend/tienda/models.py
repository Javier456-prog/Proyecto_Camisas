# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Camisa(models.Model):
    id_camisa = models.CharField(primary_key=True, max_length=25)
    precio = models.FloatField()
    marca = models.CharField(max_length=25)
    talla = models.CharField(max_length=10)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente')
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')

    class Meta:
        
        db_table = 'camisa'


class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=25)
    nombre_cliente = models.CharField(max_length=45)
    apellido_cliente = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    telefono = models.CharField(max_length=15)

    class Meta:
        
        db_table = 'cliente'


class DetalleFactura(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    detalle_factura = models.CharField(max_length=45, blank=True, null=True)
    unidad = models.IntegerField()
    total = models.FloatField()
    precio = models.FloatField()
    id_factura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='id_factura')

    class Meta:
        
        db_table = 'detalle_factura'


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=45)
    apellido_empleado = models.CharField(max_length=45)
    rol = models.CharField(max_length=9)
    telefono = models.CharField(max_length=15)

    class Meta:
        
        db_table = 'empleado'


class Factura(models.Model):
    id_factura = models.CharField(primary_key=True, max_length=10)
    producto = models.CharField(max_length=45)
    fecha_emision = models.DateField()
    total = models.FloatField()
    subtotal = models.FloatField()
    iva = models.DecimalField(max_digits=4, decimal_places=2)
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')

    class Meta:
        
        db_table = 'factura'


class Personalizacion(models.Model):
    id_personalizacion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        
        db_table = 'personalizacion'


class Proveedor(models.Model):
    id_proveedor = models.CharField(primary_key=True, max_length=10)
    nombre_proveedor = models.CharField(max_length=45)
    apellido_proveedor = models.CharField(max_length=45)
    telefono_proveedor = models.CharField(max_length=10)

    class Meta:
       
        db_table = 'proveedor'


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    producto = models.CharField(max_length=45)
    total = models.FloatField()
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')

    class Meta:
        
        db_table = 'venta'
