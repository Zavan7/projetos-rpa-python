def fabrica_de_funcoes(operacao):
    
    def soma(*args):
        
        return sum(args)
    
    def subtracao(*args):
        
        resultado = args[0]
        
        for num in args[1:]:
            
            resultado -= num
            
        return resultado
    
    def multiplicacao(*args):
        
        resultado = 1
        
        for num in args:
            
            resultado *= num
            
        return resultado
    
    def divisao(*args):
        
        resultado = args[0]
        
        for num in args[1:]:
            
            if num == 0:
                
                raise ValueError("Divisão por zero não é permitida.")
                
            resultado /= num
            
        return resultado
    
    if operacao == "soma":
        
        return soma
    
    elif operacao == "subtracao":
        
        return subtracao
    
    elif operacao == "multiplicacao":
        
        return multiplicacao
    
    elif operacao == "divisao":
        
        return divisao
    
    else:
        
        def operacao_nao_suportada(*args):

            return "Operação não suportada."
        
        return operacao_nao_suportada
    
    
adicionar = fabrica_de_funcoes("soma")
print(adicionar(5, 3, 2, 9, 4, 7)) 

subtrair = fabrica_de_funcoes("subtracao")
print(subtrair(50, 30, 5)) 

multiplicar = fabrica_de_funcoes("multiplicacao")
print(multiplicar(5, 3, 2)) 

dividir = fabrica_de_funcoes("divisao")
print(dividir(10, 2, 2)) 

operacao_invalida = fabrica_de_funcoes("modulo")
print(operacao_invalida(5, 3)) 