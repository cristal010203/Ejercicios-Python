suma = 0
num = int(input("Ingresa un número positivo: "))
while num >= 0:
    suma += num
    num = int(input("Ingresa otro número (negativo para salir): "))
print("Suma total:", suma)

