# Crie um programa que converta o valor de reais para dólar

real = float(input('Quanto de real voce gostaria de converter? '))
conversao = real/3.27

print('O valor em dólar é US${:.2f}'.format(conversao))