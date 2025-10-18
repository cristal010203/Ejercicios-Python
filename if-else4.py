year = input("Ingresa un año")
year = int(year)
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(f"{year} es un año bisiesto")
        else:
            print(f"{year} no es un año bisiesto")
    else:
        print(f"{year} es un año bisiesto")
        