from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Brinquedo
from .forms import BrinquedoForm

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