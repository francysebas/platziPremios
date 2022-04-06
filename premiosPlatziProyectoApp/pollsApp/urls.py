from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    # path('', views.index, name="index"),
    path('', views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    path('<int:pk>/', views.DetalleView.as_view(), name="detalle"),
    # ex: /polls/5/resultado
    path('<int:pk>/resultado/', views.ResultadoView.as_view(), name="resultado"),
    # ex: /polls/5/voto
    path('<int:question_id>/voto/', views.voto, name="voto"),


]
