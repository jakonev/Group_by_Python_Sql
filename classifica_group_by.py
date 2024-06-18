from itertools import groupby

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f"Aluno(nome={self.nome}, nota={self.nota})"

class AgrupadorDeAlunos:
    def __init__(self, alunos):
        self.alunos = [Aluno(**aluno) for aluno in alunos]

    @staticmethod
    def ordena_por_nota(aluno):
        return aluno.nota

    def agrupar_por_nota(self):
        alunos_agrupados = sorted(self.alunos, key=self.ordena_por_nota)
        grupos = groupby(alunos_agrupados, key=self.ordena_por_nota)
        return grupos

    def imprimir_grupos(self):
        grupos = self.agrupar_por_nota()
        for chave, grupo in grupos:
            print(chave)
            print(list(grupo))

def main():
    alunos = [
        {'nome': 'Luiz', 'nota': 'A'},
        {'nome': 'Letícia', 'nota': 'B'},
        {'nome': 'Fabrício', 'nota': 'A'},
        {'nome': 'Rosemary', 'nota': 'C'},
        {'nome': 'Joana', 'nota': 'D'},
        {'nome': 'João', 'nota': 'A'},
        {'nome': 'Eduardo', 'nota': 'B'},
        {'nome': 'André', 'nota': 'A'},
        {'nome': 'Anderson', 'nota': 'C'},
    ]

    agrupador = AgrupadorDeAlunos(alunos)
    agrupador.imprimir_grupos()

if __name__ == "__main__":
    main()
