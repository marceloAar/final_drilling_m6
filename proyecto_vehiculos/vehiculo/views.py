"""FINAL DRILLING MODULO 6 
VENTA VIRTUAL DE VEHÍCULOS
Marcelo Aceituno | Python 0079"""
from .forms import VehiculoForm
from django.shortcuts import render, redirect
from .models import Vehiculo
from django.contrib.auth.decorators import permission_required, login_required


"""Funcion para la pagina de inico index.html
ruta http://127.0.0.1:8000/"""
def index(request):       
    return render(request, 'vehiculo/index.html')



"""Funcion para agregar vehiculos si el ususario esta con permiso o autenticado
ruta http://127.0.0.1:8000/vehiculo/add"""
@login_required()
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo:list_vehiculos')  # Cambia esto a la ruta deseada
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add_vehiculo.html', {'form': form})    
    


"""Funcion para listar los vehiculos si el ususario esta con permiso o autenticado
ruta http://127.0.0.1:8000/vehiculo/list"""
@login_required()
@permission_required('vehiculo.view_vehiculo', raise_exception=True)
def list_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/list_vehiculos.html', {'vehiculos': vehiculos})


def login(request):
    return render(request, 'vehiculo/login.html')


"""Funcion para logout de la aplicacion
ruta http://127.0.0.1:8000/logout"""
# @login_required()
# def salir(request):
#     logout(request)
#     return redirect('/')