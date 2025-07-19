"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
1 - O nome com todas as letras maiúsculas
2 - O nome com todas as letras minúsculas
3 - Quantas letras ao todo, sem considerar espaços
4 - Quantas letras tem o primeiro nome
"""

nome = input('Digite seu nome: ')
new_name = nome.replace(" ", "")
split_name = nome.split()[0]

print(nome.upper())
print(nome.lower())
print(len(new_name))
print(len(split_name))  