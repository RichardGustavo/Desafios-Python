# Crie um programa que leia um número qualquer e mostre a parte inteira (Ex: O número 6.127 tem sua parte inteira 6)

from math import trunc
numero = float(input('Digite um número quebrado qualquer: '))

truncar = trunc(numero)

print('O número {} tem sua parte inteira de {}'.format(numero, truncar))
