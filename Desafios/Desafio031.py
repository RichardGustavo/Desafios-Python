# Faça um programa que leia um ano qualquer e diga se ele é bissexto

from calendar import isleap

ano = int(input('Digite um ano qualquer: '))

if isleap(ano) is True:
    print('Esse ano é Bissexto')
else:
    print('Esse ano não é Bissexto')
