from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data_inicio', 'data_termino', 'status')
    list_filter = ('status', 'data_inicio')
    search_fields = ('descricao',)