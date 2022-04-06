from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pregunta, Respuesta
from django.urls import reverse

def index(request):
    lates_respuesta_list = Pregunta.objects.all()
    return render(request, "pollsApp/index.html", {
        "lates_respuesta_list": lates_respuesta_list
    })

def detalle(request, question_id):
    # pregunta = Pregunta.objects.get(pk=question_id)
    pregunta = get_object_or_404(Pregunta, pk=question_id)
    return render(request, "pollsApp/detalle.html",{
        "pregunta":pregunta
    })

def resultado(request, question_id):
   # return HttpResponse(f"Estas viendo los resultados de la  número {question_id}")
   pregunta = get_object_or_404(Pregunta, pk=question_id)
   return render(request, "pollsApp/resultado.html/",{
       "pregunta":pregunta
   })

def voto(request, question_id):
   # return HttpResponse(f"Estás votando a la pregunta número {question_id}")
    pregunta = get_object_or_404(Pregunta, pk=question_id)
    try:
        seleccionar_respuesta= pregunta.respuesta_set.get(pk=request.POST["respuesta_form"])
    except(KeyError, Respuesta.DoesNotExist):
        return render(request, "pollsApp/detalle.html", {
            "pregunta": pregunta,
            "error_message": "No elegiste una respuesta"
        })
    else:
        
        seleccionar_respuesta.votos +=1
        seleccionar_respuesta.save()
        return HttpResponseRedirect(reverse("polls:resultado", args=(question_id,)))

