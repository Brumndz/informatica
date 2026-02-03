while True:
    print("Calculadora Simple")
    print("Elija una operación:")
    print("1. Suma"
          "\n2. Resta"
          "\n3. Multiplicación"
          "\n4. División"
          "\n5. Salir")
    eleccion = int(input())

    if eleccion not in [1, 2, 3, 4, 5]:
        print("Error: Opción inválida.")
        continue
    elif eleccion == 5:
        print("Saliendo de la calculadora.")
        break

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    if eleccion == 1:
        print("La suma es:", num1 + num2)
    elif eleccion == 2:
        print("La resta es:", num1 - num2)
    elif eleccion == 3:
        print("La multiplicación es:", num1 * num2)
    elif eleccion == 4:
        try:
            print("La división es:", num1 / num2)
        except ZeroDivisionError:
            print("Error: División por cero no permitida.")
        except ValueError:
            print("Error: Entrada inválida.")