class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.acordando = False
        self.comendo = False
        self.dirigindo = False

    def acordando(self):
        if self.acordando:
            print(f'{self.nome} já está acordado.')
        else:
           self.acordando = True
           print(f'{self.nome} acordou.')

    def comendo(self):
        if self.comendo:
            if self.dirigindo:
                print(f"{self.nome} não pode comer enquanto dirige.")
            elif not self.acordado:
                print(f"{self.nome} não pode comer enquanto está dormindo.")

    def parar_de_comer(self):
        
        # Verifica se a pessoa não está comendo
        if not self.comendo:
            
            # Se sim, imprime que a pessoa não está comendo
            print(f"{self.nome} não está comendo no momento.")
            
        else:
            
            # Se a pessoa estiver comendo, então ela pode parar de comer
            self.comendo = False
            
            # Imprime que a pessoa parou de comer
            print(f"{self.nome} terminou de comer.")
    def dirigir(self):
        
        # Verifica se a pessoa está dormindo
        if not self.acordando:
            
            # Se sim, imprime que não pode dirigir
            print(f"{self.nome} não pode dirigir enquanto está dormindo.")
            
        # Verifica se a pessoa está comendo
        elif self.comendo:
            
            # Se sim, imprime que não deve dirigir enquanto come
            print(f"{self.nome} não deve dirigir enquanto come.")
            
        # Verifica se a pessoa já está dirigindo
        elif self.dirigindo:
            
            # Se sim, imprime que a pessoa já está dirigindo
            print(f"{self.nome} já está dirigindo.")
            
        else:
            
            # Se nenhuma das condições acima for verdadeira, a pessoa pode dirigir
            self.dirigindo = True
            
            # Imprime que a pessoa começou a dirigir
            print(f"{self.nome} começou a dirigir.")
            
    # Método para fazer a pessoa parar de dirigir
    def parar_de_dirigir(self):
        
        # Verifica se a pessoa não está dirigindo
        if not self.dirigindo:
            
            # Se sim, imprime que a pessoa não está dirigindo
            print(f"{self.nome} não está dirigindo no momento.")
            
        else:
            
            # Se a pessoa estiver dirigindo, então ela pode parar
            self.dirigindo = False
            
            # Imprime que a pessoa parou de dirigir
            print(f"{self.nome} parou de dirigir.")

            
    # Método para fazer a pessoa dormir
    def dormir(self):
        
        # Verifica se a pessoa está dirigindo
        if self.dirigindo:
            
            # Se sim, imprime que não pode dormir enquanto dirige
            print(f"{self.nome} não pode dormir enquanto dirige.")
            
        # Verifica se a pessoa está comendo
        elif self.comendo:
            
            # Se sim, imprime que não pode dormir enquanto come
            print(f"{self.nome} não pode dormir enquanto come.")
            
        # Verifica se a pessoa já está dormindo
        elif not self.acordando:
            
            # Se sim, imprime que a pessoa já está dormindo
            print(f"{self.nome} já está dormindo.")
            
        else:
            
            # Se nenhuma das condições acima for verdadeira, a pessoa pode dormir
            print(f"{self.nome} foi dormir.")
            
            # Define o estado "acordado" como Falso
            self.acordando = False
            
            # Define o estado "comendo" como Falso
            self.comendo = False
vitor = Pessoa('Vitor')

vitor.acordando()