import io


# Lee los párrafos de un fichero.
# Strip() evita una línea en blanco entre ellos.

with open("clase4\quijote-ext01.txt", 'r') as file:
    file.seek(18)
    contenido = file.read(42)
    print(contenido)
