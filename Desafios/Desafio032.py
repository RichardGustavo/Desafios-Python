# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

numero1, numero2, numero3 = (input('Digite 3 números: ')).split()

max = max(numero1, numero2, numero3)
min = min(numero1, numero2, numero3)

print(f'O maior número é {max}')
print(f'O menor número é {min}')
