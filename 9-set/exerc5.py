numeros = [10, 20, 30, 10, 40, 20]
n_set = set(numeros)
print(n_set)

pertece = 25

if pertece in n_set:
    print(f'O {pertece} pertence ao conjunto')
else:
    print(f'O {pertece} não pertence ao conjunto')

conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

print("\nUnião")
print(conjunto_a | conjunto_b)

print("\ninterseção")
print(conjunto_a & conjunto_b)

print("\ndiferença")
print(conjunto_a - conjunto_b)

print("\ndiferença simétrica")
print(conjunto_a ^ conjunto_b)