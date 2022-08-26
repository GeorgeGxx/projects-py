# Fizz Buzz
# Programa del numero 1 al numero n
# si el numero es divisible entre 3, imprime fizz
# si el numero es divisible entre 5, imprime buzz
# si el numero es divisible entre 3 y 5, imprime fizzbuzz

hasta = int(input("Hasta que numero quieres contar?: "))
for variable in range(1,hasta+1):
    print(variable)
    if variable % 3 == 0:
        print("fizz")
    elif variable % 5 == 0:
        print("buzz")
    elif variable % 3 == 0 and variable % 5 == 0:
        print("fizzbuzz")