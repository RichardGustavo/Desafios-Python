# Crie um programa que calculo o preço de uma viagem em KM, viagens de até \
# 200km, use R$0,50 o km, acima de 200km, use R$0,45

distancia_viagem = float(input('Qual a distância da sua viagem?: '))

if distancia_viagem <= 200:
    print(f'Sua viagem custará {distancia_viagem*(1/2)}')
else:
    print(f'Sua viagem custará {distancia_viagem*.45}')
