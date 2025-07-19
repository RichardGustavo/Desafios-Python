# Faça Pitagoras

from math import hypot

n1 = int(input('Digite o valor do cateto oposto: '))
n2 = int(input('Digite o valor do cateto adjascente: '))

hipotenusa = hypot(n1, n2)
print('O valor da hipotenusa é igual a {:.2f}'.format(hipotenusa))

# Nesse exemplo eu apenas importei o métido Hypot
