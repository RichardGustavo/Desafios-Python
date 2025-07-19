# Faça um programa que o usuário digite um número e mostre a sua tabuada

numero = int(input('Digite um número qualquer: '))
print('='*10)
print('A tabuada do número escolhido é essa:\n1x{}={}\n2x{}={}\n3x{}={}\n4x{}={}\n5x{}={}\n6x{}={}\n7x{}={}\n8x{}={}\n9x{}={}\n10x{}={}'.format(numero, numero*1, numero, numero*2, numero, numero*3, numero, numero*4, numero, numero*5, numero, numero*6, numero, numero*7, numero, numero*8, numero, numero*9, numero, numero*10))
print('='*10)
#Eu sei que essa nâo é a melhor forma de criar uma tabuada, mas como voltei a aprender há pouco tempo, estou usando o metodo format para gravar o conteúdo