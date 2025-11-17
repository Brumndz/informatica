while True:
    print("Calculadora v3")
    print("Elija una operación:")
    print("1. Suma"
          "\n2. Resta"
          "\n3. Multiplicación"
          "\n4. División"
          "\n5. Salir")
    sel = int(input())

    if sel not in [1, 2, 3, 4, 5]:
        print("Error: Opción inválida, intente otra opción.")
        continue
    elif sel == 5:
        print("Saliendo de la calculadora.")
        break

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    if sel == 1:
        print("La suma es:", num1 + num2)
    elif sel == 2:
        print("La resta es:", num1 - num2)
    elif sel == 3:
        print("La multiplicación es:", num1 * num2)
    elif sel == 4:
        try:
            print("La división es:", num1 / num2)
        except ZeroDivisionError:
            print("Error: la división por cero no es permitida.")
        except ValueError:
            print("Error: Entrada inválida.")