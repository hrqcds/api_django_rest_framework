from django.contrib import admin
from escola.models import Aluno, Curso, Matricula  # importação das classes


class Alunos(admin.ModelAdmin):  # instanciando a classe alunos
    # informa os dados que serão disponibilizados
    list_display = ("id", "nome", "rg", "cpf", "data_nascimento")
    list_display_links = ("id", "nome")  # só posso alterar esses campos
    search_fields = ("nome",)  # busco por nome (atentar pra virgula no final)
    list_per_page = 20


class Cursos(admin.ModelAdmin):
    list_display = ("id", "descricao", "codigo_curso")
    list_display_links = ("id", "codigo_curso")
    search_fields = ("codigo_curso",)


class Matriculas(admin.ModelAdmin):
    list_display = ("id", "aluno", "curso", "periodo")
    list_display_links = ("id",)


admin.site.register(Aluno, Alunos)
admin.site.register(Curso, Cursos)
admin.site.register(Matricula, Matriculas)
