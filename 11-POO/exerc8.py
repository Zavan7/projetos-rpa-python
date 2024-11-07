class Estudante:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome


    def get_idade(self):
        return self.idade
    
    def set_idade (self, idade):
        self.idade = idade

    
    def get_nota(self):
        return self.nota
    
    def set_nota(self, nota):
        self.nota = nota


def menu():

    estudantes = []
    
    while True:
        
        print("\n1. Adicionar Estudante")
        print("2. Atualizar Nota")
        print("3. Visualizar Estudante")
        print("4. Listar Estudantes")
        print("5. Sair")
        
        escolha = input("\nEscolha uma opção: ")
        if escolha == "1":
            
            nome = input("Digite o nome do estudante: ")
            
            idade = int(input("Digite a idade do estudante: "))
            
            nota = float(input("Digite a nota do estudante: "))
            
            novo_estudante = Estudante(nome, idade, nota)
            
            estudantes.append(novo_estudante)
            
            print(f"Estudante {nome} adicionado com sucesso!")
            
        elif escolha == "2":
            
            nome = input("Digite o nome do estudante para atualizar a nota: ")

            for estudante in estudantes:
                
                if estudante.get_nome() == nome:
                    
                    nova_nota = float(input("Digite a nova nota: "))
                    
                    estudante.set_nota(nova_nota)
                    
                    print("Nota atualizada com sucesso!")
                    
                    break
                    
            else:
                
                print("Estudante não encontrado.")
                
        elif escolha == "3":
            
            nome = input("Digite o nome do estudante para visualizar as informações: ")

            for estudante in estudantes:
                
                if estudante.get_nome() == nome:
                    
                    print(f"Nome: {estudante.get_nome()}, Idade: {estudante.get_idade()}, Nota: {estudante.get_nota()}")
                    
                    break
                    
            else:
                
                print("Estudante não encontrado.")
                
        elif escolha == "4":
            
            print("Listando todos os estudantes:")

            for estudante in estudantes:
                
                print(f"Nome: {estudante.get_nome()}, Idade: {estudante.get_idade()}, Nota: {estudante.get_nota()}")

        elif escolha == "5":
            
            print("Saindo do programa.")
            
            break
            
            
        else:
            
            print("Opção inválida.")

if __name__ == "__main__":
    
    menu()