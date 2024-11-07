# Definindo a variável 'n' para determinar quantos números ímpares serão somados
n = 5

# Inicializando as variáveis
contador = 0
soma = 0
numero_impar_atual = 1

# Loop que continua até que o contador seja igual a 'n'
while contador < n:
    # Adiciona o valor de 'numero_impar_atual' à variável 'soma'
    soma += numero_impar_atual
    
    # Incrementa 'numero_impar_atual' em 2 para obter o próximo número ímpar
    numero_impar_atual += 2
    
    # Incrementa o contador para indicar que um número ímpar foi somado
    contador += 1

# Exibe o valor da soma dos primeiros 'n' números ímpares
print("A soma dos primeiros", n, "números ímpares é:", soma)