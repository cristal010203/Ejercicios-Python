n = int(input("Ingresa un número positivo: "))
suma = 0
for i in range(2, n + 1, 2):
    suma += i
print("Suma de pares:", suma)
