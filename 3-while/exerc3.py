maior_numero = -1

inteiro_positivo  = int(input('Digita um núero inteiro maior que 0: '))

while inteiro_positivo >= 0:
    if inteiro_positivo > maior_numero:
        maior_numero = inteiro_positivo
    inteiro_positivo  = int(input('Digita um núero inteiro maior que 0: '))

print (f'O maior número é: ',maior_numero)