#Heladería: sabor más pedido

Vainilla = 0
Chocolate = 0
Fresa = 0

while(Vainilla + Chocolate + Fresa) < 5:

    sabor = input("Ingrese el sabor del helado (V, C, F): ")

    if sabor == "V":
        Vainilla += 1

    elif sabor == "C":
        Chocolate += 1

    elif sabor == "F":
        Fresa += 1

    else:
        print("Sabor no válido. Por favor, ingrese V, C o F.")

    if Vainilla > Chocolate and Vainilla > Fresa:
        print("El sabor más pedido es Vainilla.")

    elif Chocolate > Vainilla and Chocolate > Fresa:
        print("El sabor más pedido es Chocolate.")

    elif Fresa > Vainilla and Fresa > Chocolate:
        print("El sabor más pedido es Fresa.")

    elif Vainilla == Chocolate and Vainilla > Fresa:
        print("Los sabores más pedidos son Vainilla y Chocolate.")

    elif Vainilla == Fresa and Vainilla > Chocolate:
        print("Los sabores más pedidos son Vainilla y Fresa.")

    elif Chocolate == Fresa and Chocolate > Vainilla:
        print("Los sabores más pedidos son Chocolate y Fresa.")
    
    elif Vainilla == Chocolate == Fresa:
        print("Empate entre Vainilla, Chocolate y Fresa.")