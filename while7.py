suma = 0
contador = 0
num = int(input("Ingresa un número (0 para terminar): "))
while num != 0:
    suma += num
    contador += 1
    num = int(input("Ingresa otro número (0 para terminar): "))
if contador > 0:
    print("Media:", suma / contador)
else:
    print("No se ingresaron números.")
