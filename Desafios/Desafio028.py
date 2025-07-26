# Faça um programa que leia a velocidade de um carro, \
# se ele ultrapassar 80 km por hora ele será multado em R$ 7,00 por km a mais

velocidade = float(input('Digite a velocidade do seu carro em Km/h: '))

if velocidade <= 80:
    print('Você está dentro do limite de velocidade')
else:
    print('Você ultrapassou {} kilometros do limite, sua multa será de R$ {}'.format(velocidade - 80, (velocidade - 80) * 7))
