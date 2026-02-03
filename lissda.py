# ...existing code...
def main():
    while True:
        ejmv, ejmv2 = ("Ingrese un número: ", "Ingrese otro número: ")
        # si el usuario presionó 'f' en cualquiera de las entradas, salir
        if ejmv == "f" or ejmv2 == "f":
            print("Saliendo del programa.")
            return

        try:
            resultado = ejmv / ejmv2
            if resultado < 0:
                print("Error: el resultado es negativo, se esperaba un valor positivo. Intente de nuevo.\n")
                continue
            print("El resultado de la división es:", resultado)
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero. Intente con otro divisor.\n")
            continue
        except Exception as e:
            print("Ha ocurrido un error inesperado:", str(e))
            continue
        finally:
            print("Operación finalizada.")
# ...existing code...
# filepath: c:\Users\Daniel\Desktop\Python bs\lissda.py
# ...existing code...
def main():
    while True:
        ejmv, ejmv2 = ("Ingrese un número: ", "Ingrese otro número: ")
        # si el usuario presionó 'f' en cualquiera de las entradas, salir
        if ejmv == "f" or ejmv2 == "f":
            print("Saliendo del programa.")
            return

        try:
            resultado = ejmv / ejmv2
            if resultado < 0:
                print("Error: el resultado es negativo, se esperaba un valor positivo. Intente de nuevo.\n")
                continue
            print("El resultado de la división es:", resultado)
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero. Intente con otro divisor.\n")
            continue
        except Exception as e:
            print("Ha ocurrido un error inesperado:", str(e))
            continue
        finally:
            print("Operación finalizada.")
# ...existing code...