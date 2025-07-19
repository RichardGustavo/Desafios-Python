# Crie um programa que o usuário informe a altura e largura de uma parede e nós definimos quanto de tinta será necessária para pintar essa parede, lembrando que cada litro de tinta pinta 2m² da parede

altura = float(input('Informa a altura de sua parede: '))
largura = float(input('Informa a largura de sua parede: '))

area = largura * altura
 
print('Será necessário {:.2f} litros de tinta para pintar sua parede'.format(area/2))
