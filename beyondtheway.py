# beyondtheway.py
# Demostración de estructuras básicas en Python
# Ejecutar: python beyondtheway.py

def demo_secuencia():
    # Estructura secuencial: las instrucciones se ejecutan una tras otra
    a = 10
    b = 3
    suma = a + b
    producto = a * b
    mensaje = f"Secuencia: a={a}, b={b}, suma={suma}, producto={producto}"
    print(mensaje)


def demo_condicionales():
    # Estructuras condicionales: if / elif / else
    x = 7
    print("\nCondicionales para x =", x)
    if x < 0:
        print("x es negativo")
    elif x == 0:
        print("x es cero")
    else:
        print("x es positivo")

    # Anidado y uso de operador ternario
    signo = "negativo" if x < 0 else "no-negativo"
    print("Signo (ternario):", signo)


def demo_bucles_for():
    # Corrected version:
    lista = ["manzana", "banana", "cereza"]
    print("\nBucle for sobre lista:")
    for i, fruta in enumerate(lista, start=1):
        print(i, fruta)

    # for con range
    print("\nFor con range(5):")
    for n in range(5):
        print(n, end=" ")
    print()  # salto de línea


def demo_bucle_while():
    # Bucle while: repetición basada en condición
    print("\nBucle while (contador):")
    contador = 0
    while contador < 5:
        contador += 1
        if contador == 3:
            print("salto en 3 (continue)")
            continue
        print("contador =", contador)
        if contador == 4:
            print("rompo el bucle en 4 (break)")
            break


def demo_funciones():
    # Definición y llamada de funciones
    print("\nFunciones:")

    def cuadrado(n):
        return n * n

    def sumar(a, b=0):
        return a + b

    valores = [1, 2, 3]
    cuadrados = [cuadrado(v) for v in valores]  # comprensión de listas (expresión secuencial)
    print("valores:", valores)
    print("cuadrados:", cuadrados)
    print("sumar(4,5) =", sumar(4, 5))
    print("sumar(10) =", sumar(10))  # usa el valor por defecto


def demo_manejo_errores():
    # Manejo de excepciones: try / except / finally
    print("\nManejo de errores:")
    datos = ["100", "dos", "300"]
    for s in datos:
        try:
            n = int(s)
            print(f"Convertido {s} -> {n}")
        except ValueError:
            print(f"No se pudo convertir '{s}' a entero")
        finally:
            # finally se ejecuta siempre
            pass


def main():
    demo_secuencia()
    demo_condicionales()
    demo_bucles_for()
    demo_bucle_while()
    demo_funciones()
    demo_manejo_errores()


if __name__ == "__main__":
    main()