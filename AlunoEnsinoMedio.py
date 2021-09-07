from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def __init__(self, nome, codigo, matri, ano):
        super().__init__(nome, codigo, matri)
        self.ano = ano
        
    def imprimir(self):
        super().imprimir()
        print("Ano: ", self.ano)

