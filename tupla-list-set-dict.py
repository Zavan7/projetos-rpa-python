"""
{} = set (conjunto) ou dict (dicionário), dependendo do uso.
() = tuple (tupla).
[] = list (lista).
"""

#1. {} = set (conjunto)

s_funcao = set(["maçã", "banana", "cereja", "cereja"])
s_chave = {"maçã", "banana", "cereja", "cereja"}
print(s_funcao)
print(s_chave)
print()

"""Limpa duplicatas, e escreve de forma aleatoria, de acordo como o sistema determina, mutaveis"""

#2. {} = dict (dicionário)

dicionario = {
    'Nome': 'Vitor',
    'Idade': 28,
    'Nacionalidade': 'Brasileiro'
}
for c, v in dicionario.items():
    print(f'{c}: {v}')

print()

"""Par de chave, valor, mutaveis"""

# 3. () = tuple (tupla)
t = (1, 2, 3, 4, 5)
print(t)

"""Imutavel"""

# 4. [] = list (lista).
l = [1, 2, 3, 4, 5]
print(l)

"""Mutavel"""