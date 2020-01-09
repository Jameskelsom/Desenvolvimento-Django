from django import forms
from .models import Categoria, Tarefa


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'


class TarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = '__all__'
