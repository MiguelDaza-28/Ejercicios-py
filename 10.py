#Academia de baile: asistencia

clases = int(input("clases asistidas: "))

if clases < 5:
    print("asistencia baja")

elif 5 <= clases <=8:
    print("asistencia media")

else:
    print("asistencia alta")