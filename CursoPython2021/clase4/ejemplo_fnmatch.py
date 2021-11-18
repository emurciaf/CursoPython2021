import fnmatch
import os


patron = 'ejemplo*.py'
print('Patrón de búsqueda: ', patron)
print('*****')

ficheros = os.listdir('./clase4')
for nombre in ficheros:
    # print('Nombre:', (nombre, fnmatch.fnmatch(nombre, patron)))
    print('Nombre: %-25s %s' % (nombre, fnmatch.fnmatch(nombre, patron)))

print('*****')
print('Nombre: ', ficheros)
print('Coinciden: ', fnmatch.filter(ficheros, patron))