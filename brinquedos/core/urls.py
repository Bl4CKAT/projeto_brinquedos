from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import FormRegistro
from . import views
from .views import LoginPersonalizado

urlpatterns = [
    path('', views.lista_brinquedos, name='lista_brinquedos'),
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('login/', LoginPersonalizado.as_view(template_name='login.html'), name='login'),
    path('logout/', views.sair, name='logout'),
    path('editar/<int:id>/', views.editar_brinquedo, name='editar_brinquedo'),
    path('excluir/<int:id>/', views.excluir_brinquedo, name='excluir_brinquedo'),
]