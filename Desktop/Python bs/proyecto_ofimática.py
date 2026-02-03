def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

while True:
        print("Seleccione la operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Ingrese la opción: ")
        
        if opcion == '5':
            print("Saliendo de la calculadora.")
            break
        
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        if opcion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")
        elif opcion == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif opcion == '4':
            try:
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
                else:
                print("Opción inválida. Por favor, intente de nuevo.")
            except ZeroDivisionError:
                print("no se divide a 0")