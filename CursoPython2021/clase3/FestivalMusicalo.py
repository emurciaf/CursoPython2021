#import clase3.FestivalMusical
from clase3.FestivalMusical import FestivalMusical

import datetime


festival1 = FestivalMusical ('Creamfileds', 'UK', 'Dance')
festival2 = FestivalMusical('Primavera Sound', 'SP', 'Dance')

print( festival1.nombre, festival1.pais, festival1.estilo_musical)
print( festival2.nombre, festival2.pais, festival2.estilo_musical)

festival2.festival_metodo()
print(festival2.nombre.upper())

festival1.nombre = 'Benicassim'
print( festival1.nombre)

#del festival1
#print( festival1.nombre)

FestivalMusical.valor_ticket(50)

print(FestivalMusical.valor_ticket)     #accede a la clase
print(festival2.valor_ticket)           #accede a la instancia

dia1 = datetime.date(2021,11,18)
FestivalMusical.dia_evento(dia1)