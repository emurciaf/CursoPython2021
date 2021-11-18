import io


# Lee los párrafos de un fichero.
# Strip() evita una línea en blanco entre ellos.

with open("clase4\quijote_pg2000.txt", 'r') as file:
    contenidos = file.readlines(2000)
    for c in contenidos:
        print(c.strip())