from pathlib import Path
import os

fich_path = Path(Path.home(), "directorio ficheros")    #C:\Users\emurcia

if not fich_path.exists():
    os.makedirs(fich_path)

fich_path = fich_path.joinpath("quijote_pg2000.txt")

with fich_path.open('w') as file:
    lineas = [
        "Primera parte del ingenioso hidalgo don Quijote de la Mancha \n"
        "Capítulo primero. Que trata de la condición y ejercicio del famoso \n"
        "hidalgo don Quijote \n"
    ]
    file.writelines(lineas)

