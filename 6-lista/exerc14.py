numeros = []

# Usa um loop for para repetir o bloco de código 5 vezes
for i in range(5):
    
    # Pede ao usuário para inserir um número
    numero = int(input("Digite um número: "))
    
    # Adiciona o número inserido pelo usuário à lista de números
    numeros.append(numero)

# Classifica os números na lista em ordem crescente
numeros.sort()

# Imprime a lista classificada
print("Números em ordem crescente:", numeros)