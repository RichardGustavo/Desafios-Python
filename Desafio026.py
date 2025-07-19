"""
Faça um programa em que o usuário escreva qualquer coisa
conte quantas vezes a aparece a letra "A"
mostre em que posição ela aparece por primeiro
mostre em que posição ela aparece por último
"""

frase_qualquer = str(input("Digite qualquer coisa: "))

lower = frase_qualquer.lower()

print('A letra "A" aparece apenas', lower.count('a'), 'vez(es)')
print('A primeira vez que a letra "A" aparece é na posição número', lower.find('a'))
print('A última vez que a letra "A" aparece é na posição número', lower.rfind('a'))

# Estou conseguindo me adaptar aos métodos de uso e manipulação de string cada vez melhor.
