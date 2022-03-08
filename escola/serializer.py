from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


# Criar uma classe e dizer os campos que quero usar em cada serializer
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:  # Informando a classe que o nosso serializer vai inicializar
        model = Aluno
        # especifica os dados que recebe na api
        fields = ["id", "nome", "rg", "cpf", "data_nascimento"]


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        # recebe todos os campos da classe curso
        fields = "__all__"


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []  # tras todos os dados, só exclui algum...


class ListMatriculaDeAlunos(serializers.ModelSerializer):
    # busca apenas a descrição do curso no lugar do ID
    curso = serializers.ReadOnlyField(source="curso.descricao")
    periodo = serializers.SerializerMethodField()  # busca a maneira como foi escrito

    class Meta:
        model = Matricula
        fields = ["curso", "periodo"]

    def get_periodo(self, obj):  # pega a variavel periodo e executa o method de display do mesmo
        return obj.get_periodo_display()


class ListaAlunosMatriculadoCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source="aluno.nome")

    class Meta:
        model = Matricula
        fields = ["aluno_nome"]
