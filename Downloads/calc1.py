eleccion = input("Seleccione la operación (suma, resta, multiplicacion, division): ")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
try:
    if eleccion == "suma":
        print("La suma es:", suma)
    elif eleccion == "resta":
        print("La resta es:", resta)
    elif eleccion == "multiplicacion":
        print("La multiplicación es:", multiplicacion)
    elif eleccion == "division":
        print("La división es:", division)
except ZeroDivisionError:
    print("Error: División por cero no permitida.")