# Crie um programa que calcule o valor do aluguel de um carro, sabendo que sua diária custa R$60,00 e R$0,15 por KM rodado

diaria = int(input('Você alugou o carro por quanto dias? '))
kilometragram = float(input('Quantos kilometros você rodou com o carro? '))

despesa = (diaria*60) + (kilometragram*0.15)

print('O valor total a pagar será de R${}'.format(despesa))