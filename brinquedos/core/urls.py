from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_brinquedos, name='lista_brinquedos'),
    path('editar/<int:id>/', views.editar_brinquedo, name='editar_brinquedo'),
    path('excluir/<int:id>/', views.excluir_brinquedo, name='excluir_brinquedo'),
]