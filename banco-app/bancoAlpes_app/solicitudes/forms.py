from django import forms

from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta: 
        model= Solicitud
        fields=[
            'id',
            'tipo',
            'fecha'
      
        ]
        labels= {
            'id':'Id',
            'tipo':'Tipo',
            'fecha':'Fecha'
        }
