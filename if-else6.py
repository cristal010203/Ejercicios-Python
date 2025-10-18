num = input("Ingresa un número positivo cualquiera")
num = int(num)
numeroprimo = True
if num <= 1:
    numeroprimo = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            numeroprimo = False
            break   
if numeroprimo:
    print(f"El número {num} es primo")
else:
    print(f"El número {num} no es primo")
    