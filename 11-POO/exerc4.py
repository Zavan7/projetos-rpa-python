class Evento:
    def __init__(self, capacidade = 10):
        self.capacidade = capacidade
        self.lugares_disponiveis = capacidade

    def reservar(self):
        if self.lugares_disponiveis == 0:
            print('Desculpe, todos os lugares estão reservados')

            return
    
        self.lugares_disponiveis -= 1

        print('Lugar reservado com sucesso!')

    def cancelar(self):
        if self.lugares_disponiveis == 10:
            print('Não tem reserva para cancelar')

            return
    
        self.lugares_disponiveis += 1

        print('Reserva cancelada!')

    def lugares_vagos(self):
        return f'Lugares disponíveis {self.lugares_disponiveis}'
    
evento = Evento()



evento.reservar()
print(evento.lugares_vagos())

evento.reservar()
print(evento.lugares_vagos())

evento.reservar()
print(evento.lugares_vagos())

evento.cancelar()
print(evento.lugares_vagos())

evento.cancelar()
print(evento.lugares_vagos())

evento.cancelar()
print(evento.lugares_vagos())

evento.cancelar()
print(evento.lugares_vagos())