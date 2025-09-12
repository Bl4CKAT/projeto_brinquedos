from django.shortcuts import render
from .models import Brinquedo

def lista_brinquedos(request):
    brinquedos = Brinquedo.objects.all()
    return render(request, "lista.html", {"brinquedos": brinquedos})

# Create your views here.
