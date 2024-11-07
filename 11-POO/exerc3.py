class FormatadorDeFrase:
    def __init__(self, frase):
        self.frase = frase

    def para_maiusculo(self):
        self.frase = self.frase.upper()

    def obter_frase(self):
        return self.frase

    def para_minusculo(self):
        self.frase = self.frase.lower()

    def primeira_letra_maiuscula(self):
        self.frase = self.frase.capitalize()

    def para_titulo(self):
        self.frase = self.frase.title()

    def contar_vogais(self):
        vogais = 'aeiouáéíóúàèìòùãõâêîôû'        
        contagem = 0
        frase_minuscula = self.frase.lower()

        for i in frase_minuscula:
            if i in vogais:
                contagem += 1
            return contagem
        
    def contar_consoantes(self):
        consoantes = 'bcdfghjklmnpqrstvwxyzç'
        contagem = 0
        frase_minuscula = self.frase.lower()

        for i in frase_minuscula:
            if i in consoantes:
                contagem += 1
            return contagem

    def contar_letra_a(self):
        return self.frase.lower().count('a')

    def encontre_palavra(self, palavra):
        return self.frase.lower().count(palavra.lower())

    def retorne_frase(self):
        return self.frase

def menu():
    
        print("\nBem-vindo ao Formatador de Frase!")
        
        frase = input("Por favor, digite uma frase: ")
        
        formatador = FormatadorDeFrase(frase)
        
        while True:

            print("\nEscolha uma opção para formatar a sua frase:")
            print("1. Converter para maiúsculas")
            print("2. Converter para minúsculas")
            print("3. Capitalizar a primeira letra da frase")
            print("4. Converter para o formato título.")
            print("5. Contar Vogais")
            print("6. Contar Consoantes")
            print("7. Contar letra 'a'")
            print("8. Pesquisar palavra")
            print("9. Mostrar frase atual")
            print("10. Sair")
            
            escolha = input("\nDigite o número da sua escolha: ")

            if escolha == '1':
                formatador.para_maiusculo()

            elif escolha == '2':
                formatador.para_minusculo()
            
            elif escolha == '3':
                formatador.primeira_letra_maiuscula()
            
            elif escolha == '4':
                formatador.para_titulo()
            
            elif escolha == '5':
                print(f'Total de vogais é: {formatador.contar_vogais()}')

            elif escolha == '6':
                print(f'Total de consoantes é: {formatador.contar_consoantes()}')

            elif escolha == '7':
                print(f'O número de letras A, é: {formatador.contar_letra_a()}')

            elif escolha == '8':
                palavra = input('Digite a palavra que gostaria de procurar: ')

                contagem = formatador.encontre_palavra(palavra)

                if contagem > 0:
                    print(f"A palavra '{palavra}', aparece {contagem} vezes dentro da frase.")
                else:
                    print(f"A plavra '{palavra}', não se encontra na frase.")
            
            elif escolha == '9':
                formatador.retorne_frase()
            
            elif escolha == '10':
                print('Até mais!')
                break
            
            else:
                print('Opção invalida, tente novamente!')

            print('Frase atual: ', formatador.obter_frase())
                
if __name__ == "__main__":
    menu()