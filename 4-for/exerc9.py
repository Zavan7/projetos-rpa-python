n = int(input('Digite um número inteiro e positivo: '))

if n < 0:
    print ('Número inválido! Por favor, insira um número não negativo.')

else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print (f"O fatorial de {n} é {fatorial}")



