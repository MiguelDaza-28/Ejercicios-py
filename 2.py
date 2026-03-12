#Gimnasio: acceso por edad:

edad = int(input("Ingrese su edad: "))

if edad < 13:
    print("No tienes acceso al gimnasio.")

elif 13 <= edad <= 17:
    print("Clase Juvenil.")

elif 18 <= edad <= 59:
    print("Clase General.")

else:
    print("Clase Senior.")