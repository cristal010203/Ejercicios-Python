num = input("Ingresa el precio del producto para aplicar el descuento")
num = int(num)
descuento = input("Ingresa el porcentaje de descuento a aplicar (sin el símbolo %)")
descuento = int(descuento)
if descuento >= 0 and descuento <= 100:
    precio_final = num - (num * descuento / 100)
    print(f"El precio final del producto con un descuento del {descuento}% es: {precio_final}")
else:
    print("El porcentaje de descuento ingresado no es válido")