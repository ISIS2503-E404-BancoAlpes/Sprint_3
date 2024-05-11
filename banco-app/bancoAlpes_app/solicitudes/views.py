from django.shortcuts import render
from .logic.solicitudes_logic import get_solicitudes ,create_solicitud, get_solicitud,modificar_sol_mod ,verificar_hash
from .forms import SolicitudForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from bancoAlpes_app.auth0backend import getRole, getEmail
from django.contrib.auth.decorators import login_required


@login_required
def solicitud_list(request):
    role,email= getRole(request)
    solicitudes = get_solicitudes()
    solicitudes_aux=[]
    for solicitud in solicitudes:
           if not verificar_hash(solicitud):
              modificar_sol_mod(solicitud)
           if role == "user":
             if solicitud.cliente == email:  
                solicitudes_aux.append(solicitud)
           else: 
              solicitudes_aux.append(solicitud)
           
    solicitudes= solicitudes_aux
            
    context={'solicitudesList':solicitudes}    
    return render(request, 'solicitudes/solicitudes.html',context)

@login_required
def solicitud_update(request,solicitud_id):
   solicitud= get_solicitud(solicitud_id)
   role,email= getRole(request)
    
   if role == "user" and solicitud.cliente == email:
    if request.method == 'POST':
        form= SolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            create_solicitud(form,email) 
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
    role,email= getRole(request)
    if role== "user":
        if request.method == 'POST':
            form = SolicitudForm(request.POST)
            if form.is_valid():
                create_solicitud(form,email)
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
    else:
        return HttpResponse("Unauthorized User") 