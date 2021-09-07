from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, nome, codigo, matri, semestre):
        super().__init__(nome, codigo, matri)
        self.semestre = semestre

    def imprimir(self):
        super().imprimir()
        print("Semestre: ", self.semestre)

