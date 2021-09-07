from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao
from random import randint

#Construa um algoritmo para implementar a classe Aluno(código, nome matrícula).
#A classe Aluno possui duas subclasses, a classe AluEnsinoMedio(ano)
#e AlunoGraduacao(semestre). As 3 classes possuem o método construtor
#e também o método imprimir(), que imprime na tela os valores de todos os
#atributos da sua classe

print("-------------------------------------------------------------------------")
#Info de aluno
al = Aluno("Michael Mauricio de Sena Pacheco", 315999, "60072826002")
al.imprimir()
print("-------------------------------------------------------------------------")
#Info de aluno com ano
aem = AlunoEnsinoMedio("Almirante Meireles", 635999, "80092814030", 2003)
aem.imprimir()
print("-------------------------------------------------------------------------")
#Info de aluno com série
ag = AlunoGraduacao("Maximus Menegueli", 658999, "10703569996", "3°")
ag.imprimir()
