import os

def scan(aut, path, extension):
    try:
        contenido = os.listdir(path)
        files = []
        index = 0
        for file in contenido:
            if (os.path.isfile(os.path.join(path, file))):
                if (extension == "" or file.endswith(extension)): #este if se podria mejorar pero we
                    if (aut == 'y'): #este tmb xdd
                        new_name = ((file.split("."))[0]+str(index)+str(extension))
                        os.rename(file, new_name)
                        index += 1
                    else:
                        print('Nombre actual: ' + file)
                        new_name = input('Ingrese el nuevo nombre: ')
                        os.rename(file,new_name)
    except(FileNotFoundError):
        print('Error, ingreso una ruta invalida.')
    except(KeyboardInterrupt):
        print('')
        print('Adios!')

def main():
    res = input('Cambiar nombre automaticamente? [y/n]: ')
    path = input('Ingrese la ruta de los archivos a procesar: ')
    extension = input('Ingrese la extension (deje en blanco para procesar todas las extensiones): ')
    scan(res, path, extension)

main()