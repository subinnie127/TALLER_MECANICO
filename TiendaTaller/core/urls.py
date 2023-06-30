from django.urls import path
from .views import home, poblar_bd, vehiculo, vehiculo_tienda, vehiculo_ficha
from . import views


urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('vehiculo/<action>/<id>', vehiculo, name="vehiculo"),
    path('vehiculo_tienda', vehiculo_tienda, name="vehiculo_tienda"),
    path('vehiculo_ficha/<id>', vehiculo_ficha, name="vehiculo_ficha"),
    path('index/', views.index, name="index"),
    path('contacto/', views.contacto, name="contacto"),
    path('nosotros/', views.nosotros, name="nosotros"),
]
