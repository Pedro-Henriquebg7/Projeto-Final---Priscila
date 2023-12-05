from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Aluno, Plano, Instrutor
from .forms import AlunoForm

class AlunoListView(View):
    template_name = 'alunos_app/lista_alunos.html'

    def get(self, request, *args, **kwargs):
        alunos = Aluno.objects.all()
        return render(request, self.template_name, {'alunos': alunos})

def criar_aluno(request):
    # Código para criar aluno
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm()
    return render(request, 'alunos_app/criar_aluno.html', {'form': form})


def editar_aluno(request, pk):
    # Código para editar aluno
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'alunos_app/editar_aluno.html', {'form': form, 'aluno': aluno})

def excluir_aluno(request, pk):
    # Código para excluir aluno
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    return render(request, 'alunos_app/excluir_aluno.html', {'aluno': aluno})
# alunos_app/views.py


def pagina_inicial(request):
    # Obtenha as informações que você deseja exibir
    informacoes = {
        'titulo': 'Bem-vindo à Academia Boa Forma',
        'descricao': 'A melhor academia da cidade!',
        'contato': {
            'email': 'contato@academiaboaforma.com',
            'telefone': '(84) 99234-3548',
        },
    }

    # Passe as informações para o template
    return render(request, 'alunos_app/pagina_inicial.html', informacoes)

