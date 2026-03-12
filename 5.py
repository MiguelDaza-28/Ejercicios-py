#tienda de mascotas: alimento por tipo de animal

animal = input("¿Qué tipo de animal es? (perro, gato, conejo): ")

if animal == "perro":
    print("El alimento recomendado para perros es: croquetas para perros.")

elif animal == "gato":
    print("El alimento recomendado para gatos es: croquetas para gatos.")

elif animal == "conejo":
    print("El alimento recomendado para conejos es: zanahorias.")

else:
    print("Tipo de animal no válido.")