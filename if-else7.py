anioNaciemiento = input("Ingresa tu año de nacimiento: ")   
anioNaciemiento = int(anioNaciemiento)
anioActual = 2025
if anioNaciemiento < 2025 | anioNaciemiento > 1900:   
    edad = anioActual - anioNaciemiento
    print(f"Tu edad es {edad}") 
else:
    print("El año ingresado no es válido")
    