numeros = [2, 5, 8, 10, 12, 15, 18, 20, 23, 25, 28]

n_imp = list(filter(lambda x: x % 2 != 0, numeros))

print (n_imp)

n_imp2 = tuple(map(lambda x: x **2, n_imp))

print (n_imp2)