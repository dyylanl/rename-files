from hashlib import new
import os


def scan(path, extension):
    contenido = os.listdir(path)
    files = []
    index = 0
    if (extension==""):
        extension="*"
    for file in contenido:
        if (os.path.isfile(os.path.join(path, file)) and file.endswith(extension)):
            res = input('Desea cambiar el nombre de ' +file+'? [y/n]: ')
            if (res == 'y'):
                new_name = input('Ingrese el nuevo nombre: ')
                os.rename(file,new_name)


path = input('Ingrese la ruta de los archivos a procesar: ')
extension = input('Ingrese la extension: ')
scan(path,extension)