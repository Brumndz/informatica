x = int(input("Ingresa un número entero: "))
signo = "negativo" if x < 0 else "positivo"
print("Signo (ternario):", signo)

#diferencia de lista y tupla, diccionario y sus usos
mi_lista = [1, 2, 3]
mi_tupla = (1, 2, 3)
#escribir diferencias entre estas dos estructuras de datos
print("Lista:", mi_lista, "Tupla:", mi_tupla)
mi_lista[0] = 10  # listas son mutables
print("Lista modificada:", mi_lista)
# mi_tupla[0] = 10  # tuplas son inmutables, esto causaría un error

mi_diccionario = {"a": 1, "b": 2}
print("Diccionario:", mi_diccionario)
mi_diccionario["a"] = 10  # diccionarios son mutables
print("Diccionario modificado:", mi_diccionario)
# uso de diccionarios para mapear claves a valores
print("Valor para clave 'b':", mi_diccionario["b"])
# uso de listas para colecciones ordenadas
print("Elemento en índice 1 de la lista:", mi_lista[1])
# uso de tuplas para datos inmutables
print("Elemento en índice 1 de la tupla:", mi_tupla[1])

# ...existing code...

def demo_funciones():
    # Definición y llamada de funciones
    print("\nFunciones:")

    def cuadrado(n):
        return n * n

    def sumar(a, b=0):
        return a + b

    entrada = int(input("Ingrese números"))
    valorpot = int(input("Ingrese número"))

    cuadrados = [cuadrado(v) for v in [valorpot]]
    print("valores:", valorpot)
    print("cuadrados:", cuadrados)
    print("sumar =", sumar(entrada))


demo_funciones()
# ...existing code...

# seleccionar que tipo de elemento en el diccionario se quiere imprimir
mi_diccionario = {"a": 1, "b": 2}
for i in mi_diccionario:
    print(i, mi_diccionario[i])  


#tablas de multiplicar
num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# ...existing code...
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



