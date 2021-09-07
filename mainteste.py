
from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

#Construa um algoritmo para implementar a classe Aluno(código, nome matrícula).
#A classe Aluno possui duas subclasses, a classe AluEnsinoMedio(ano)
#e AlunoGraduacao(semestre). As 3 classes possuem o método construtor
#e também o método imprimir(), que imprime na tela os valores de todos os
#atributos da sua classe



def cadastrar_aluno():
    nome = input("-Nome completo do Aluno para cadastro: ").upper()
    if len(nome) == 0:
        input("Erro")
        return cadastrar_aluno()
    matricula()
    codigo()
    #não to conseguindo puxar o imprimir da class Aluno
    Aluno().imprimir

#cria um número aleatório
def matricula():
    matri = randint(999, 9999)
    return

#recebe input de CPF
def codigo():
    codigo = input("-Insira CPF do Aluno: ")
    if len(codigo) != 11:
        input("Erro")
        return codigo

#menu de teste
def menu():
    while True:
        opcao = input('''
    ----Menu----
    1 - Cadastrar Aluno
    2 - Ver informação de Aluno
    0 -	Finalizar o Programa

    Escolha: ''')
        if opcao == '0':
            exit()
        elif opcao == '1':
            cadastrar_aluno()
#        elif opcao == '2':
#            info_aluno()
        else:
            input("Erro. Escolha o índice de alguma ação. [ENTER]")

menu()
