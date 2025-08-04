from django.db import models
import uuid

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('A fazer', 'A fazer'),
        ('Em andamento', 'Em andamento'),
        ('Concluída', 'Concluída'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_termino = models.DateField(verbose_name="Data de Término")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='A fazer')

    def __str__(self):
        return self.descricao