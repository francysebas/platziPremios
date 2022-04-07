from dataclasses import field, fields
from importlib.metadata import files
from django.contrib import admin
from .models import Pregunta, Respuesta

class RespuestaEnLinea(admin.StackedInline):
    model = Respuesta
    extra = 3

class PreguntaAdmin(admin.ModelAdmin):
    fields=["publicacion_fecha","pregunta_text"]
    inlines = [RespuestaEnLinea]
    list_display = ("pregunta_text", "publicacion_fecha")
    list_filter = ["publicacion_fecha"]
    search_fields = ["pregunta_text"]


admin.site.register(Pregunta,PreguntaAdmin)

