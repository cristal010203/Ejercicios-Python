numero1 = input("Ingresa un número positivo")
numero1 = float(numero1)

numero2 = input("Ingresa un número positivo")
numero2 = float(numero2)

numero3 = input("Ingresa un número positivo")
numero3 = float(numero3)

if numero1 >= numero2 and numero1 >= numero3:
    print("El numero mayor es: ", numero1); 
elif numero2 >= numero1 and numero2 >= numero3:
    print("El numero mayor es: ", numero2);  
else:
    print("El numero mayor es: ", numero3)