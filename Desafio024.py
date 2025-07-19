# Crie um programa que leia o nome da pessoa e veja se ela possui Silva no nome, independete do lugar

nome = str(input('Digite seu nome completo: '))

verificar_nome = ('Silva' in nome)

if verificar_nome == True:
    print('Seu nome possui Silva no nome')
else:
    print('Seu nome não possui Silva nome')

# Programa feito sem ajuda externa, mesmo sabendo que dá pra melhorar e alterar algumas coisas que ainda nao aprendi.

