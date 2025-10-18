letra = input("Ingresa una letra")
letra = letra.lower()
if letra in ['a', 'e', 'i', 'o', 'u']:
    print(f"{letra} es una vocal")
elif letra.isalpha() and len(letra) == 1:
    print(f"{letra} es una consonante")
else:
    print("No has ingresado una letra válida")