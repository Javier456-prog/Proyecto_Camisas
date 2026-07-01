from django.urls import path
from . import views

urlpatterns = [

    path('', views.listar_datos, {'modelo': 'camisas'}, name='listar_camisas'),

    path('camisas/', views.listar_datos, {'modelo': 'camisas'}),
    path('clientes/', views.listar_datos, {'modelo': 'clientes'}),
    path('proveedores/', views.listar_datos, {'modelo': 'proveedores'}),
    path('ventas/', views.listar_datos, {'modelo': 'ventas'}),
    path('facturas/', views.listar_datos, {'modelo': 'facturas'}),
    path('empleados/', views.listar_datos, {'modelo': 'empleados'}),

    path('registrar_venta/', views.registrar_venta, name='registrar_venta'),
]