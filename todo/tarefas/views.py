from django.shortcuts import render
from django.http import HttpResponse
from .forms import CategoriaForm, TarefaForm
# Create your views here.


def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)  # enviar dados para o form
        if form.is_valid():
            form.save()
            return HttpResponse('Categoria adicionada com sucesso!')
        else:
            print(form.errors)
    else:
        form = CategoriaForm()  # chamar form em branco
    return render(request, 'tarefas/nova_categoria.html', {'form': form})


def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)  # enviar dados para o form
        if form.is_valid():
            form.save()
            return HttpResponse('Tarefa adicionada com sucesso!')
        else:
            print(form.errors)
    else:
        form = TarefaForm()  # chamar form em branco
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})
