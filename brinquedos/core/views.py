from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Brinquedo
from .forms import BrinquedoForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormRegistro
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

class LoginPersonalizado(LoginView):
    template_name: 'login.html'

    def form_valid(self, form):
        """Quando o Login for bem sucedido apresentar mensagem de boas vindas"""
        response = super().form_valid(form)
        usuario = self.request.user
        messages.success(self.request, f"Bem vindo de volta, {usuario.username}!")
        return response

@login_required(login_url='login')
def lista_brinquedos(request):
    brinquedos = Brinquedo.objects.all()

    if request.method == 'POST':
        form = BrinquedoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_brinquedos') + '?added=true')

    else:
        form = BrinquedoForm()

    return render(request, "lista.html", {"brinquedos": brinquedos, "form": form})

def registrar_usuario(request):
    if request.method == 'POST':
        form = FormRegistro(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')

        else:
            form = FormRegistro()

        return render(request, 'registro.html', {'form': form})

def sair(request):
    logout(request)
    messages.success(request,'Você saiu com sucesso!')
    return redirect('login')

def editar_brinquedo(request, id):
    brinquedo = get_object_or_404(Brinquedo, id=id)
    if request.method == 'POST':
        form = BrinquedoForm(request.POST, instance=Brinquedo)
        if form.is_valid():
            form.save()
            return redirect('lista_brinquedos')

    else:
        form = BrinquedoForm(instance=brinquedo)
    return render(request, 'editar.html', {'form': form, 'brinquedo': brinquedo})


def excluir_brinquedo(request, id):
    brinquedo = get_object_or_404(Brinquedo, id=id)
    if request.method == 'POST':
        brinquedo.delete()
        return redirect('lista_brinquedos')
    return render(request, 'excluir.html', {'brinquedo': brinquedo})