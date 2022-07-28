from hashlib import new
import os
from re import I
try:
    ejemplo_dir = input('Ingrese la ruta a escanear: ')
    contenido = os.listdir(ejemplo_dir)
    files = []
    index = 0
    for fichero in contenido:
        if os.path.isfile(os.path.join(ejemplo_dir, fichero)):# and fichero.endswith('.jpg'):
            files.append(fichero)
            print('Nombre actual: ' + files[index])
            new_name = (files[index]+''+str(index))
            print('Nuevo nombre: '+new_name)
            res = input('Desea cambiarlo? y/n: ')
            if (res == 'y'):
                os.rename(files[index], new_name)
except:
    print('Error. Abortando...')
