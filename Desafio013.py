# Faça um programa que o usuário informe seu salário e nós acrescentemos 15% de aumento

salario = float(input('Informe o valor do seu salário: '))
aumento = (salario*15)/100

print('O valor do seu salário com reajuste de 15% é igual a {:.2f}'.format(salario+aumento))