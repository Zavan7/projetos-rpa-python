aluno = {
    "matricula": "A12345",
    "nome": "João Silva",
    "curso": "Engenharia de Computação",
    "semestre": 5,
    "cr": 8.5
}


# ADICIONANDO ITENS
aluno['hobbie'] = ['Leitura', 'Corrida', 'Xadrez']
aluno['idade'] = 22

# ATUALIZANDO ITENS
aluno['semestre'] = 6
aluno['cr'] = 8.7

print (aluno)

# REMOVENDO ITENS
del aluno ['idade']
item_removido_1 = aluno.pop('hobbie')
item_removido_2 = aluno.popitem()
print(item_removido_1)

print (aluno)

# COPIANDO DICIONARIOS
copia_aluno_1 = aluno.copy()
copia_aluno_2 = dict(aluno)

print(copia_aluno_1)
print(copia_aluno_2)