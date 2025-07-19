# Escreva um programa em que leia o nome de uma cidade e verifique se ela começa com 'Santo'

cidade = str(input("Digite o nome da sua cidade: "))

print(cidade.find("Santo"))

if cidade.split()[0] == "Santo":
    print('Sua cidade começa com a palavra "Santo"')
elif cidade.split()[0] == "santo":
    print('Sua cidade começa com a palavra "Santo"')
else:
    print('Sua cidade não começa com a palavra "Santo"')


# Código feito totalmente sem ajuda externa.
