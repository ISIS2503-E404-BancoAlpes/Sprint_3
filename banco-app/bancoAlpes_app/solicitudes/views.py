from django.shortcuts import render
from .logic.solicitudes_logic import get_solicitudes ,create_solicitud, get_solicitud, get_solicitudes_cliente
from .forms import SolicitudForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from bancoAlpes_app.auth0backend import getRole, getId
from django.contrib.auth.decorators import login_required


@login_required
def solicitud_list(request):
    role= getRole(request)
    id= getId(request)
    if role == "admin":
        solicitudes = get_solicitudes()
    elif role == "user":
        #solicitudes= get_solicitudes_cliente(id)
        solicitudes= get_solicitudes()
    context={'solicitudesList':solicitudes}    
    return render(request, 'solicitudes/solicitudes.html',context)

@login_required
def solicitud_update(request,solicitud_id):
   solicitud= get_solicitud(solicitud_id)
   role= getRole(request)
   id= getId(request)
   if role == "user":
    if request.method == 'POST':
        form= SolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            create_solicitud(form) 
            return HttpResponseRedirect(reverse("solicitudesList"))
        else:
            print(form.errors) 
    else: 

        form= SolicitudForm(instance=solicitud)
    context={
            'form': form,
    }    
    return render(request,'solicitudes/update_solicitud.html',context)
   else:
     return HttpResponse("Unauthorized User")   
   

@login_required
def solicitud_create(request):

    id= getId(request)
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            create_solicitud(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created solicitud')
            return HttpResponseRedirect(reverse('solicitudesCreate'))
        else:
            print(form.errors)
    else:
       
       form = SolicitudForm()

    context = {
        'form': form,
    }
    return render(request, 'solicitudes/create_solicitud.html', context)
