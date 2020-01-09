from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição')