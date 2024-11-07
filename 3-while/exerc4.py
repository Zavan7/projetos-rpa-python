saldo_conta = 1000.00

while True:

    print("Caixa Eletrônico")
    print("1 - Verificar Saldo")
    print("2 - Depositar Dinheiro")
    print("3 - Sacar Dinheiro")
    print("4 - Sair")

    opcao = input('Escolha de 1-4: ')

    if opcao == '1':
        print (f'Seu saldo é de R$  {saldo_conta:.2f}')
        

    elif opcao == '2':
        depoisto = float(input('Digite um valor para deposito: R$ '))
        if depoisto > 0:
            saldo_conta += depoisto
            print ('Deposito realizado com sucesso.')        

    elif opcao == '3':
        saque = float(input('Digite um valor para sacar: R$ '))
        if saque > 0 and saque <= saldo_conta:
            saldo_conta -= saque
            print ('Saque realizado com sucesso.')
        else: 
            print("Valor de saque inválido ou saldo insuficiente.")

    elif opcao == '4':
        print ('Operação encerrada')

    else:
        print ('Opção invalida.')
        break
        