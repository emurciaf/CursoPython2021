class FestivalMusical:
    def __init__(self, nombre, pais, estilo_musical):
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical
festival1 = FestivalMusical('Creamfileds', 'UK', 'Dance')
festival2 = FestivalMusical('Primavera Sound', 'SP', 'Dance')

print( festival1.nombre, festival1.pais, festival1.estilo_musical)
print( festival2.nombre, festival2.pais, festival2.estilo_musical)