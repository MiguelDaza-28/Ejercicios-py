#Cine: entrada según edad

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("El precio de la entrada es: 8000 pesos.")

elif 12 <= edad <= 59:
    print("El precio de la entrada es: 12000 pesos.")

else:
    print("El precio de la entrada es: 9000 pesos.")

    