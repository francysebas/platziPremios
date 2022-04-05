from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path('', views.index, name="index"),
    # ex: /polls/5/
    path('<int:question_id>/', views.detalle, name="detalle"),
    # ex: /polls/5/resultado
    path('<int:question_id>/resultado/', views.resultado, name="resultado"),
    # ex: /polls/5/voto
    path('<int:question_id>/voto/', views.voto, name="voto"),


]
