artista = {
    "nome": "Ludwig van Beethoven",
    "nascimento": 1770,
    "falecimento": 1827,
    "nacionalidade": "Alemã",
    "estilo": "Clássico"
}

print('Nome:', artista ['nome'])
# print('Profissão:', artista ['profissao'])

print()

print('Nacionalidade:', artista.get ('nacionalidade'))
print('Profissão:', artista.get ('profissao', 'Inf Indisponível'))

print()

if "estilo" in artista:
    
    # Se 'sistema' estiver presente, imprime o valor associado a essa chave
    print("O estilo musical é:", artista["estilo"])  # Saída esperada: iOS
    
else:
    
    # Se 'sistema' não estiver presente, imprime uma mensagem indicando isso
    print("Estilo musical não especificado.")


if "instrumento" in artista:
    
    # Se 'sistema' estiver presente, imprime o valor associado a essa chave
    print("O instrumento musical é:", artista["instrumento"])  # Saída esperada: iOS
    
else:
    
    # Se 'sistema' não estiver presente, imprime uma mensagem indicando isso
    print("\nO instrumento musical não especificado.")