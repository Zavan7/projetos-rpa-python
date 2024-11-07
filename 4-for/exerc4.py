n = int(input('Digite um número inteiro e descubra seu quadrado: '))

soma_quadrado = 0

for i in range (1, n +1):
    quadrado = i**2
    print(f'Quadrado de {i}: {quadrado}')
    soma_quadrado += quadrado

print('A soma dos quadrados é: ', soma_quadrado)