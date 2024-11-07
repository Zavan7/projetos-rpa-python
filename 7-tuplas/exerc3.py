produto = ("Smartphone", 1000.00, [2, 3, 4])
print(produto)
print()

produto[2].append(5)
vendas_atualizadas = produto[2]

print(produto)

print()

print("Questões:\n")

print("a) Ao tentar alterar o preço do Smartphone, qual erro você encontrou?")
print("O erro ao tentar alterar o preço do Smartphone é:")
print("TypeError: 'tuple' object does not support item assignment\n")

print("b) Vendas atualizadas:", vendas_atualizadas)  


print()