from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_brinquedos, name='lista_brinquedos'),
]