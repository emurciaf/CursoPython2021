from pathlib import Path
import os

# Lee del directorio "directorio1"
fichero_path = Path(os.pardir, "..\CursoPython2021", "quijote-ext01.txt")
with fichero_path.open('r') as file:
    print(file.read())
