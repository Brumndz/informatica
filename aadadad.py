
print("Promedio de calificaciones")
notas = []
notat = 0
cant = 0
while True:
    try:
        num = int(input("Ingrese el número de estudiantes (máximo 10): "))
        if num > 1 or num < 10:
            for i in range(num):
                a = True
                nombre = str(input("Ingrese el nombre del estudiante: "))
                while a:
                    print("Ingrese 00 para terminar el ingreso de notas.\n")
                    nota = float(input("Ingrese las notas del estudiante: "))
                    notat += nota
                    cant += 1
                    if nota == 00:
                        break
                    else:
                        cant -= 1
                        promedio = notat / cant
                        notas.append(promedio)
                        a = False
                        nota = 0
                        print(f"Notas hasta ahora",notas)
                        print(f"El promedio del estudiante {nombre} es de {promedio}")
                        if promedio < 7:
                            print("Desaprobado")
                        elif promedio > 7:
                            print("Aprobado")
                print("El promedio de tus estudiante es ")
                
    except ValueError:
        print("Por favor, ingrese un número válido.")