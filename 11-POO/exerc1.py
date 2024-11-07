class Frutas:
    def __init__ (self, fruta, preco_kg, qnt_estoque):
        self.fruta = fruta
        self.preco_kg = preco_kg
        self.qnt_estoque = qnt_estoque

    def exibir_info (self):
        print(f'Nome da fruta: {self.fruta}')
        print(f'Preço da fruta por kg: R$ {self.preco_kg:.2f} ')
        print(f'Unidade em estoque : {self.qnt_estoque}')

fruta1 = Frutas ('Maçã', 2.5, 10)

fruta2 = Frutas ('Banana', 1.5, 50)


fruta1.exibir_info()
print('_'*50)
print()
fruta2.exibir_info()

