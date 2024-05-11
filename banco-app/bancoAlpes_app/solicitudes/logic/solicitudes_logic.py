from ..models import Solicitud
from django.shortcuts import get_object_or_404
import hashlib

def get_solicitudes():
    queryset=Solicitud.objects.all()

    return (queryset)

def get_solicitudes_cliente(email):
    queryset=Solicitud.objects.filter(cliente=email)
    return (queryset)

def calular_hash(solicitud):
    valor= str(solicitud)
    llave=hashlib.sha256(valor.encode())
    return llave.hexdigest()

def verificar_hash(solicitud):
    llave= solicitud.llave
    llave1= calular_hash(solicitud)
    return llave==llave1

def modificar_sol_mod(solicitud):
    solicitud.verificada= False
    solicitud.save()
    return ()    

def get_solicitud(solicitud_id):
    return get_object_or_404(Solicitud,pk=solicitud_id)


def create_solicitud(form,email):
    solicitud = form.save()
    solicitud.cliente = email
    solicitud.llave = calular_hash(solicitud)
    solicitud.verificada= True
    solicitud.save()
    return ()


