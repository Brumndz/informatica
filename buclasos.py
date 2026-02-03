def demo_bucle_while():
    # Bucle while: repetición basada en condición
    print("\nBucle while (contador):")
    contador = int(input("Ingrese el valor inicial del contador: "))
    while contador < 20:
        contador += 1
        print("contador =", contador)
        if contador == 14:
            print("rompo el bucle en 4 (break)")
            break
demo_bucle_while()

