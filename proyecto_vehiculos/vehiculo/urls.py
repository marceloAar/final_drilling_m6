from django.urls import path
from . import views

app_name = 'vehiculo'

urlpatterns = [    
    path('', views.index, name='vehiculo_index'),
    path('vehiculo/add/', views.add_vehiculo, name='add_vehiculo'),
    path('vehiculo/list/', views.list_vehiculos, name='list_vehiculos'),    
]