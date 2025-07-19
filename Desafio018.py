# Faça um programa que o professor sorteie o nome de 4 alunos

import random

nomes = ('João', 'José', 'Alfredo', 'Miguel')

aluno = random.choice(nomes)

print('O sorteado para dessa vez foi {}'.format(aluno))
