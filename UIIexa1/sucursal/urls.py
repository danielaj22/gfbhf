from django.urls import path
from sucursal import views

urlpatterns = [
    path('',views.sucursal_vista,name="views.sucursal_vista")
]