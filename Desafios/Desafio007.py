# Faça um programa que leia um valor em metros e o converta em centímetros e milímetros
valor = float(input('Digite um valor em metros: '))

print('O valor de {:.0f}m em centímetros é igual a {:.0f}cm e em milímetros é igual a {:.0f}mm'.format(valor, valor*100, valor*1000))
