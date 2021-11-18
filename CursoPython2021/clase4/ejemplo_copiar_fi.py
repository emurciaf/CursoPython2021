import os
import shutil

# copia normal
# shutil.copy(src='clase4\quijote-ext01.txt', dst='clase4\quijote-ext02.txt')

# copia conservando metadatos
shutil.copy2(src='clase4\quijote-ext01.txt', dst='clase4\quijote-ext03.txt')
