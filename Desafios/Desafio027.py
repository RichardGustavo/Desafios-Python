from random import choice

numero = (1, 2, 3, 4, 5)
numero_aleatorio = choice(numero)
numero_usuário = int(input('Digite um número entre 1 e 5: '))

if numero_usuário == numero_aleatorio:
    print('Você ganhou')
else:
    print('Você perdeu')
