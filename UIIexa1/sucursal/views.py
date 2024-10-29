from django.shortcuts import render
from .models import sucursal
# Create your views here.
def sucursal_vista(request):
    Listadosucursales = sucursal.objects.all()
    return render(request,"sucursal.html",{"lassucursales":Listadosucursales})