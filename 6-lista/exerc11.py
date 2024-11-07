nomes = [" ", "Alice", "Bruno", "Clara", "Daniel", "Eduarda"]
notas = [' ', 85, 90, 78, 92, 88]


for i in nomes:
    print (i)

print()

for i, nome in enumerate(nomes):
    if i == 0:
        continue
    print (f'Aluno {i} é {nome}')

print()

for i, nome in enumerate(nomes):
    if not nome.strip():
        continue
    print(f'{i}: Aluno {nome}, teve uma nota total de: {notas[i]}')