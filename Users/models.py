from django.db import models
#from App2.models import Modelo1# EJEMPLO DE UNA IMPORTACION DESDE OTRA APP PARA UN MODELO DE ESTA Y PODER USARLO AQUI

#RECORDANDO QUE LOS MODELOS COMO BUENA PRACTICA EN DJANGO, SE CREAN SEGUN LAS APPS, NO SE MANTIENEN EN UN SOLO ARCHIVO.

class Rols(models.Model):
    Id_Rol = models.AutoField(primary_key=True)
    Rol_name = models.CharField(max_length=50, choices=[('Customer', 'Customer'), ('Delivery', 'Delivery')])


class Users(models.Model):
    Id_user = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=30)
    Email = models.EmailField(max_length=25)
    Password = models.CharField(max_length=25)
    Id_Rol = models.ForeignKey(Rols, on_delete=models.CASCADE)# además de ForeignKet existen OneToOneField y ManyToManyField

