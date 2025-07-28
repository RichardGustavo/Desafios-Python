# Faça um programa que leia 3 retas e determine se podem ou não formar um  \
# triângulo

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da teceira reta: '))

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print('Esses valores podem formar um triângulo.')
else:
    print('Esses valores NÃO podem formar um triângulo.')
