from django.db import models


# Create your models here.

class Pregunta(models.Model):
    pregunta_text = models.CharField('pregunta', max_length=100)
    publicacion_fecha= models.DateTimeField("fecha publicacion")


class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuest_text = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)