from django.contrib import admin
from django.urls import path, include
from alunos_app.views import pagina_inicial # Importe a classe AlunoListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos_app/', include('alunos_app.urls')),
    # Adicione a seguinte linha para a URL raiz:
    path('', pagina_inicial, name='alunos_app/pagina_inicial'),  # Use a classe AlunoListView para a URL raiz
]

