titulo= input('Digite o titulo do livro: ')
autor = input('Digite o autor do livro: ')
ano = input('Digite o ano de publicação do livro: ')


def criar_perfil(titulo, autor, ano):
    
    
    return {
        "titulo": titulo,
        "autor": autor,
        "ano": ano
    }

perfil = criar_perfil(titulo, autor, ano)

print("\nLivro adicionado:")


for chave, valor in perfil.items():
    print(f"{chave.capitalize()}: {valor}")