"""
Faça um programa que leia o nome inteiro de uma pessoa e mostre o primeiro e o
último nome separadamente
"""

nome = str(input("Digite seu nome completo: "))

split_nome = nome.split()
ultimo_nome = len(split_nome) -1

print("Seu primeiro nome é {}".format(split_nome[0]))
print("Seu último nome é {}".format(split_nome[ultimo_nome]))


# Precisei de ajuda externa para a ultima linha do código