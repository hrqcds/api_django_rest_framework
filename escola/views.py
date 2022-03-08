from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListMatriculaDeAlunos
from escola.serializer import ListaAlunosMatriculadoCursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()  # trazer todos os alunos do banco de dados
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo matriculas de alunos"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


# Listando dados de outras tabelas
class ListMatriculaDeAlunosViewSet(generics.ListAPIView):
    """listando as matriculas de um aluno"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(
            aluno_id=self.kwargs["pk"])  # pegando o id do parametro
        return queryset
    serializer_class = ListMatriculaDeAlunos


class ListAlunosMatriculadosViewSet(generics.ListAPIView):
    """listando alunos matriculasdos em um curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"])
        return queryset
    serializer_class = ListaAlunosMatriculadoCursoSerializer
