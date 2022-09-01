#Funcion holamundo con Docstring

import sys

def holamundo():
    """ Imprime "Hello World" en la consola """
    for i in range(1, 10):
        nombre = 'GeorgeGxx'
        print("Hola Mundo " + nombre)
if __name__ == "__main__":
    holamundo()

nombre = holamundo.__name__
documentacion = holamundo.__doc__
print(nombre, " : ")
print(documentacion)