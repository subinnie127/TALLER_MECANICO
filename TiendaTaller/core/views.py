from django.shortcuts import redirect, render
from .models import Vehiculo, Categoria
from .forms import VehiculoForm

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def vehiculo_tienda(request):
    data = {"list": Vehiculo.objects.all().order_by('patente')}
    return render(request, "core/vehiculo_tienda.html", data)

def vehiculo_ficha(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    data = {"vehiculo":  vehiculo}
    return render(request, "core/vehiculo_ficha.html", data)

def vehiculo(request, action, id):
    data = {"mesg": "", "form": VehiculoForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = VehiculoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El vehículo fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos vehículos con la misma patente!"

    elif action == 'upd':
        objeto = Vehiculo.objects.get(patente=id)
        if request.method == "POST":
            form = VehiculoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El vehículo fue actualizado correctamente!"
        data["form"] = VehiculoForm(instance=objeto)

    elif action == 'del':
        try:
            Vehiculo.objects.get(patente=id).delete()
            data["mesg"] = "¡El vehículo fue eliminado correctamente!"
            return redirect(vehiculo, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El vehículo ya estaba eliminado!"

    data["list"] = Vehiculo.objects.all().order_by('patente')
    return render(request, "core/vehiculo.html", data)

def poblar_bd(request):
    Vehiculo.objects.all().delete()
    Vehiculo.objects.create(patente="ALAN67", marca='Volvo', modelo="Volvo Station Wagon", imagen="images/volvosw.jpg",servicio="Suspension y Direccion",detalle_servicio="arreglo", categoria=Categoria.objects.get(idCategoria=1))
    Vehiculo.objects.create(patente="BILL88", marca='Saleen', modelo="S7", imagen="images/saleen.jpg", categoria=Categoria.objects.get(idCategoria=1))
    Vehiculo.objects.create(patente="ELVI54", marca='Shelby', modelo="Cobra de 1967", imagen="images/cobra.jpg",servicio="Suspension y Direccion",detalle_servicio="arreglo", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="FEDE84", marca='Mercedes-Benz', modelo="Pagoda de 1972", imagen="images/pagoda.jpg",servicio="Suspension y Direccion",detalle_servicio="arreglo", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="JEFF46", marca='Ford', modelo="Wolf WR1 Ford Race Car", imagen="images/wolf.jpg",servicio="Suspension y Direccion",detalle_servicio="arreglo", categoria=Categoria.objects.get(idCategoria=1))
    Vehiculo.objects.create(patente="JOHN80", marca='Ford', modelo="Flathead Roadster de 1932", imagen="images/flathead.jpg",servicio="Suspension y Direccion",detalle_servicio="arreglo", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="PAUL62", marca='Rolls-Royce', modelo="Phantom", imagen="images/phantom.jpg",servicio="Suspension y Direccion",detalle_servicio="arreglo", categoria=Categoria.objects.get(idCategoria=1))
    Vehiculo.objects.create(patente="SCAR47", marca='Mustang', modelo="Mustang de 1970", imagen="images/mustang.jpg",servicio="Suspension y Direccion",detalle_servicio="arreglo", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="TIRO98", marca='Mercedes-Benz', modelo="Iron Bike de 1998", imagen="images/motoiron.jpg",servicio="Suspension y Direccion",detalle_servicio="arreglo", categoria=Categoria.objects.get(idCategoria=3))
    Vehiculo.objects.create(patente="UVAM20", marca='Silver Plus', modelo="Silver de 2000", imagen="images/silver.jpg",servicio="Suspension y Direccion",detalle_servicio="arreglo", categoria=Categoria.objects.get(idCategoria=3))
    return redirect(vehiculo, action='ins', id = '-1')
def index(request):
    return render (request, "core/index.html")
def contacto(request):
    return render(request, "core/contacto.html")
def nosotros(request):
    return render(request, "core/nosotros.html")