# Faça o usuário digitar um ângulo qualquer e o programa informe seu seno, cosseno e tangente

import math

angulo = float(input('Digite um valor para um angulo qualquer: '))

angulo_rad = math.radians(angulo)

seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print('O valor de seno é {:.4f}, cosseno é {:.4f}, e tangente é {:.2f}'.format(seno, cosseno, tangente))


# Para esse código precisei de ajuda externa, pesquisei que precisava receber o valor da variável ângulo e converter para radianos
