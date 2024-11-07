lista_compras = []

while True:
    
    print("\nMenu:")
    print("1. Adicionar item à lista")
    print("2. Remover item da lista")
    print("3. Exibir lista de compras")
    print("4. Sair")

    opcao = int(input("Escolha uma opção: "))

    # Se a opção escolhida for 1:
    if opcao == 1:
        
        item = input("Digite o item que deseja adicionar à lista: ")
        
        lista_compras.append(item)
        
        print("Item adicionado à lista!")

    elif opcao == 2:
        
        if len(lista_compras) == 0:
            
            print("A lista de compras está vazia.")
            
        else:
            
            item = input("Digite o item que deseja remover da lista: ")
            
            if item in lista_compras:
            
                lista_compras.remove(item)
                
                print("Item removido da lista!")
                
            else:
                
                print("O item não está na lista.")

    elif opcao == 3:
        
        print("\nLista de Compras:")
        
        for item in lista_compras:
            
            print("-", item)

    elif opcao == 4:
        
        print("Saindo...")
        
        break

    else:
        
        print("Opção inválida. Escolha uma opção válida.")

    print()