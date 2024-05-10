from django.db import models

class Solicitud(models.Model):
    id= models.IntegerField(primary_key = True) 
    tipo= models.CharField(max_length=50)
    fecha= models.DateField(auto_created=True)   #Fecha de creación
    cliente= models.IntegerField(max_length=50)
    llave= models.CharField(max_length=50)
    def __str__(self):
        return '%s , %s, %s,%s'%(self.id, self.fecha,self.cliente,self.tipo)
# Create your models here.
