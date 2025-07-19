# Faça um programa que leia o preço de um produto e o calcule com um desconto de 5%

preco = float(input('Informe o preço do seu produto: '))
desconto = (preco*5)/100

print('O preço do seu produto com 5% de desconto será de {:.2f}'.format(preco-desconto))