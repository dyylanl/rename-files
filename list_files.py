from hashlib import new
import os
from re import I

ejemplo_dir = input('Ingrese la ruta a escanear: ')
contenido = os.listdir(ejemplo_dir)
imagenes = []
index = 0
for fichero in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)):# and fichero.endswith('.jpg'):
        imagenes.append(fichero)
        print('Cambiando nombre de:' + imagenes[index])
        new_name = (imagenes[index]+''+str(index))
        print(new_name)

print(imagenes)

