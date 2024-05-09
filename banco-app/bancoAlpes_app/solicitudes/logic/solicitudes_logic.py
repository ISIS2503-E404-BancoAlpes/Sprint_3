from ..models import Solicitud
from django.shortcuts import get_object_or_404

def get_solicitudes():
    queryset=Solicitud.objects.all()

    return (queryset)

def get_solicitudes_cliente(id):
    queryset=Solicitud.objects.filter(cliente=id)

    return (queryset)



def get_solicitud(solicitud_id):
    return get_object_or_404(Solicitud,pk=solicitud_id)


def create_solicitud(form):
    solicitud = form.save()
    solicitud.save()
    return ()
