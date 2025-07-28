# Faça um programa que calculo o aumento de um funcionário com base no seu salário \
# Salários acima de R$ 1250,00, calule um aumento de 10%
# Salários inferiores, calcule um aumento de 15%

salario = float(input('Digite o valor de seu salário: '))

if salario > 1250:
    print(f'Seu salário com correção de 10% será de R${(salario/10)+salario}')
else:
    print(f'Seu salário com correção de 15% será de R${(salario/15)+salario:.2f}')
