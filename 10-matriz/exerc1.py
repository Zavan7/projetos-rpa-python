M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

soma_pares = 0
soma_impares = 0

for linha in range(4):
    for coluna in range(4):
        if M[linha][coluna] % 2 == 0:
            
            soma_pares += M[linha][coluna]  

for linha in range(4):
    for coluna in range(4):
        if M[linha][coluna] % 2 != 0:
            
            soma_impares += M[linha][coluna]  


print(f"A soma dos números pares da matriz é: {soma_pares}\n")
print(f"A soma dos números impares da matriz é: {soma_impares}\n")