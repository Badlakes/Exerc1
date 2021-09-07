

class Aluno():
    def __init__(self, nome, codigo, matri):
        self.nome = nome
        self.codigo = codigo
        self.matri = matri

    def imprimir(self):
        print("Aluno:", self.nome)
        print("N° de Matrícula: ", self.matri)
        print("Código: ", self.codigo)


