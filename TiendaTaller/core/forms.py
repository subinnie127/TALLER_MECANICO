from django import forms
from django.forms import ModelForm, fields
from .models import Vehiculo

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'imagen','servicio','detalle_servicio', 'categoria']

class ContactForm(forms.Form):
        nombre = forms.CharField(max_length=100)
        apellido = forms.CharField(max_length=100)
        email = forms.EmailField()
        numero = forms.CharField(max_length=20)
        direccion = forms.CharField(max_length=100)
        ciudad = forms.CharField(max_length=100)
        region = forms.CharField(max_length=100)
        mensaje = forms.CharField(widget=forms.Textarea)

def clean_numero(self):
    numero = self.cleaned_data['numero']
    if not numero.isdigit():
        raise forms.ValidationError("El número de teléfono debe contener solo dígitos.")
    return numero
def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

def clean_apellido(self):
    apellido = self.cleaned_data['apellido']
    if len(apellido) < 3:
        raise forms.ValidationError("El apellido debe tener al menos 3 caracteres.")
    return apellido

def clean_email(self):
    email = self.cleaned_data['email']
    return email

def clean_direccion(self):
    direccion = self.cleaned_data['direccion']
    if not direccion.strip():
        raise forms.ValidationError("La dirección es obligatoria.")
    return direccion

def clean_ciudad(self):
    ciudad = self.cleaned_data['ciudad']
    if not ciudad.strip():
        raise forms.ValidationError("La ciudad es obligatoria.")
    return ciudad

def clean_region(self):
    region = self.cleaned_data['region']
    if not region.strip():
        raise forms.ValidationError("La región es obligatoria.")
    return region

def clean_mensaje(self):
    mensaje = self.cleaned_data['mensaje']
    if len(mensaje) > 200:
        raise forms.ValidationError("El mensaje no puede superar los 200 caracteres.")
    return mensaje