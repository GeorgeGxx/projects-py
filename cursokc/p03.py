nombre = input("¿Como te llamas? ")
print("Hola, ", nombre)

strEdad = input("¿Cuantos años tienes? ")
strAnno = input("¿En que año estamos? ")
strCumplidos = input("¿Cumpliste años ya este año? ")

edad = int(strEdad)
anno = int(strAnno)

if strCumplidos == "S":
    nacimiento = anno - edad
else:
    nacimiento = anno - edad - 1

print(nombre, "naciste en", nacimiento)
