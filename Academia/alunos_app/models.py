# alunos_app/models.py
from django.db import models

class Plano(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco_mensal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Instrutor(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    plano = models.ForeignKey(Plano, on_delete=models.SET_NULL, null=True)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

