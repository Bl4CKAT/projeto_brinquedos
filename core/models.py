from django.db import models

class Brinquedo(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade = models.IntegerField()

def _str_(self):
    return self.nome

# Create your models here.
