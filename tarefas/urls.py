from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('editar/<uuid:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('remover/<uuid:id>/', views.remover_tarefa, name='remover_tarefa'),
    path('remover_concluidas/', views.remover_concluidas, name='remover_concluidas'),
]