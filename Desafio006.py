# Faça um programa que leia duas notas de um aluno, calcule e mostre sua média

nota1 = int(input(('Qual sua primeira nota?: ')))
nota2 = int(input(('Qual sua segunda nota?: ')))
media = (nota1+nota2)/2

print('A média de suas notas é igual a {:.2f}'.format(media))
