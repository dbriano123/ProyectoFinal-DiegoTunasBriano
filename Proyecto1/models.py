from django.db import models

class Pagina(models.Model):

    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=120)
    subtitulo=models.CharField(max_length=120)
    cuerpo=models.CharField(max_length=1200)
    autor=models.CharField(max_length=120)
    fecha=models.DateField()
    imagen=models.CharField(max_length=250)
    

class Usuario(models.Model):
    
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=80)
    usuario=models.CharField(max_length=80)
    email=models.CharField(max_length=80)
    clave=models.CharField(max_length=80)
    tipo=models.CharField(max_length=80)
    
    