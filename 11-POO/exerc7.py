class Animal:
    def fazer_som(self):
        print('O animal fez o som.')

class Cachorro(Animal):
    def fazer_som(self):
        print('O cachorro faz wolf-wolf')

    def latir(self):
        print('Wolf-wolf')

class Gato(Animal):
    def fazer_som(self):
        print('O gato faz miau')

    def miar(self):
        print('Miau')


animal = Animal()

animal.fazer_som()

cachorro = Cachorro()

cachorro.fazer_som()

cachorro.latir()

gato = Gato()

gato.fazer_som()

gato.miar()