# No arquivo urls.py do aplicativo "alunos_app"
from django.urls import path
from .views import AlunoListView, criar_aluno, editar_aluno, excluir_aluno, pagina_inicial

urlpatterns = [
    path('lista_alunos/', AlunoListView.as_view(), name='lista_alunos'),
    path('criar_aluno/', criar_aluno, name='criar_aluno'),
    path('editar_aluno/<int:pk>/', editar_aluno, name='editar_aluno'),
    path('excluir_aluno/<int:pk>/', excluir_aluno, name='excluir_aluno'),
    path('pagina_inicial/', pagina_inicial, name='pagina_inicial'),
    # Adicione outras rotas conforme necessário
]

