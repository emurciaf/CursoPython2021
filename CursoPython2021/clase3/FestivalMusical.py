import datetime

class FestivalMusical:
    def __init__(self, nombre, pais, estilo_musical):
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical
    def festival_metodo(self):
        print('El mejor festival es:')

    @classmethod
    def valor_ticket( cls, valor):
        cls.valor_ticket = valor

    @staticmethod
    def dia_evento(dia):
        #if dia.weekday() >= 5:
        if dia.weekday() == 5 or dia.weekday() == 6:
            return print('Es un fin de semana')
        else:
            return print('Es un día laborable')
