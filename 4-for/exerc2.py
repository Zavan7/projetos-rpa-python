i = int(input('Digite um número inteiro positivo: '))

soma_pares = 0

for i in range (1, i + 1):

    if i % 2 == 0:
        print (f'Número {i} + {soma_pares} = {i+soma_pares}')

        soma_pares += i

print (f'A soma dos pares é:  {soma_pares}')