from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Aluno
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
def pagina_inicial(request):
    # Código para a página inicial
    return render(request, 'alunos_app/pagina_inicial.html')

