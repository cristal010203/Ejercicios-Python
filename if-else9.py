nota = input("Ingresa tu calificación para connocer tu resultado: ")
nota = int(nota)
if nota >= 90 and nota <= 100:
    print("Tu calificación es A")
elif nota >= 80 and nota <= 90:
    print("Tu calificación es B")
elif nota >= 70 and nota <= 80:
    print("Tu calificación es C")   
elif nota >= 60 and nota <= 70:
    print("Tu calificación es D")
elif nota < 60:
    print("Tu calificación es F")
    print("Reprobaste el curso")
else:
        print("Numero fuera del rango aprobado")
        
        

