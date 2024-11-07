while True:

    print ('Calculadora simples: ')
    print ('1 - Adição: ')
    print ('2 - Subtração: ')
    print ('3 - Multiplicação: ')
    print ('4 - Divisão: ')
    print ('5 - Sair: ')


    escolha_operador = input ('Escolha um operador lógico nas opções acima: ')

    if escolha_operador >= '6':
        print ('Opção invalida, tente novamente!')
        break

    if escolha_operador == '5':
        print ('Im back')
        break

 

    n1 = int(input('Escolha um número inteiro: '))
    n2 = int(input('Escolha outro número inteiro: '))

    if escolha_operador == '1':
        resultado = n1 + n2
        print ('Resultado: ', resultado)

    elif escolha_operador == '2':
        resultado = n1 - n2
        print ('Resultado: ', resultado)

    elif escolha_operador == '3':
        resultado = n1 * n2
        print ('Resultado: ', resultado)

    elif escolha_operador == '4':
       if n2 != 0:
                        
            resultado = n1 / n2
            print("Resultado:", resultado)
            
       else: 
           print("Erro: Divisão por zero.")

    else:
        print ('Operação invalida, tente novamente.')