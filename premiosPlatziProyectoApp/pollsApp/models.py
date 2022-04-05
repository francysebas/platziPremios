from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Pregunta(models.Model):
    pregunta_text = models.CharField('pregunta', max_length=100)
    publicacion_fecha= models.DateTimeField("fecha publicacion")

    def __str__(self):
        return self.pregunta_text

    def was_published_recently(self):
        return self.publicacion_fecha >= timezone.now() - datetime.timedelta(days=1)

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_text = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.respuesta_text