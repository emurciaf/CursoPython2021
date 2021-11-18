import io

entrada_agregar = """En un lugar de la Mancha, de cuyo nombre no quiero acordarme,
no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua,
rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, ..."""

with open("clase4\quijote-ext01.txt", 'a') as file:
    file.write(entrada_agregar)
