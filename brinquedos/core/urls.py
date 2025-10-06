from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import  reverse_lazy
from . import views

urlpatterns = [
    path('', views.lista_brinquedos, name='lista_brinquedos'),
    path('registrar/', CreateView.as_view(template_name='registro.html', form_class=UserCreationForm,
        success_url=reverse_lazy('login')), name='registrar'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editar/<int:id>/', views.editar_brinquedo, name='editar_brinquedo'),
    path('excluir/<int:id>/', views.excluir_brinquedo, name='excluir_brinquedo'),
]