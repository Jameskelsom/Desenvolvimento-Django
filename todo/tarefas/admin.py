from django.contrib import admin
from .models import Categoria, Tarefa
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    pass

class TarefaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categoria)
admin.site.register(Tarefa)