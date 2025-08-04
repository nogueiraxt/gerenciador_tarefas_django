from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['descricao', 'data_inicio', 'data_termino', 'status']
        widgets = {
            'descricao': forms.TextInput(attrs={'placeholder': 'Descreva a tarefa'}),
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_termino': forms.DateInput(attrs={'type': 'date'}),
        }