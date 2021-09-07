from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao
from random import randint

#Construa um algoritmo para implementar a classe Aluno(código, nome matrícula).
#A classe Aluno possui duas subclasses, a classe AluEnsinoMedio(ano)
#e AlunoGraduacao(semestre). As 3 classes possuem o método construtor
#e também o método imprimir(), que imprime na tela os valores de todos os
#atributos da sua classe

#Info com aluno
al = Aluno("Michael Mauricio de Sena Pacheco", 315999, "60072826002")
al.imprimir()

aem = AlunoEnsinoMedio("Cleiton Meireles", 635999, "80092814030")
