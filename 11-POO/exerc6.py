class Termometro:
    def __init__(self):
        self._temperatura = 0


    @property
    def temperatura(self):
        return self._temperatura
    
    @temperatura.setter
    def temperatura (self, valor):
        if -100 <= valor <=100:
            self._temperatura = valor
        else:
            print('Temperatura fora de alcance!')
    
t = Termometro()
t.temperatura = 25
print(t.temperatura)
t.temperatura = 200
print(t.temperatura)