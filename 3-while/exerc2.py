soma_dos_numeros_digitados = 0

digite_numeros = int(input('Digita um número, ou 0 para sair: '))

while digite_numeros != 0:
    soma_dos_numeros_digitados += digite_numeros

    digite_numeros = int(input('Digita um número, ou 0 para sair: '))

print ('Total: ', soma_dos_numeros_digitados)