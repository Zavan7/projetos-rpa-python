filme = {
    "titulo": "Inception",
    "diretor": "Christopher Nolan",
    "ano": 2010,
    "genero": "Ficção Científica"
}

# keys(), values(), e items()

print('Chaves: ', list(filme.keys()))
print('Valores: ', list(filme.values()))
print('Chave, Valor: ', list(filme.items()))
print()

# 2. clear()

copia_filme = filme.copy()
# print(copia_filme)
copia_filme.clear()
print(copia_filme)

# 3. setdefault()
elenco = filme.setdefault('elenco', ["Leonardo DiCaprio", "Ellen Page"])
print('Elenco adicionado: ', elenco)
print('Filme atualizado: ', filme)

# update()

atualizacao = {
    'duração': 148,
    'idioma': 'ingles'
}

filme.update(atualizacao)
print('Filme atualizado: ', filme)

# fromkeys()

chaves = ["nome", "idade", "ocupacao"]
novo_filme = dict.fromkeys(chaves, 'desconhecido')
print(novo_filme)