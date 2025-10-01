from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.lista_brinquedos, name='lista_brinquedos'),
    path('login/', auth_views.LoginView.as_view(template_name='login.htm'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('editar/<int:id>/', views.editar_brinquedo, name='editar_brinquedo'),
    path('excluir/<int:id>/', views.excluir_brinquedo, name='excluir_brinquedo'),
]