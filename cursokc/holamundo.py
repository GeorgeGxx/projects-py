#Comentario

import sys

def holamundo():
    """ Imprime "Hello World" en la consola """
    for i in range(1, 10):
        nombre = 'GeorgeGxx'
        print("Hola Mundo " + nombre)
if __name__ == "__main__":
    holamundo()

documentacion = holamundo.__doc__
print(documentacion)