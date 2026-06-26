from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.listar_datos, {'modelo': 'camisas'}, name='listar_camisas'),

    
    path('<str:modelo>/', views.listar_datos, name='listar_datos'),
]