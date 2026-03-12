#spa: servicio disponible

servicios_validos = ["masaje", "facial", "spa"]

servicio = input("servicios: (masaje, facial, spa): ")

while servicio not in servicios_validos:
    print("servicio desconocido")
    servicio = input("servicios: (masaje, facial, spa): ")

if servicio == "masaje":
        print("servicio disponible")

if servicio == "facial":
        print("servicio no disponible")

if servicio == "spa":
        print("servicio disponible")