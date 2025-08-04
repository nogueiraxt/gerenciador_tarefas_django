from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().order_by('data_inicio')
    return render(request, 'tarefas/listar_tarefas.html', {'tarefas': tarefas})

def adicionar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/formulario_tarefa.html', {'form': form, 'titulo': 'Adicionar Nova Tarefa'})

def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/formulario_tarefa.html', {'form': form, 'titulo': 'Editar Tarefa'})

def remover_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('listar_tarefas')

def remover_concluidas(request):
    Tarefa.objects.filter(status='Concluída').delete()
    return redirect('listar_tarefas')