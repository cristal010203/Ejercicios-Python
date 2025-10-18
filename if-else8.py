num = input("Ingresa un numero positivo cualquiera")
num = int(num)
if (num%5==0) or (num%7==0):
    if (num%5==0):
        print(f"El número {num} es múltiplo de 5")
    elif (num%7==0):
        print(f"El número {num} es múltiplo de 7")
else:
    print(f"El número {num} no es múltiplo de 5 ni de 7")
    