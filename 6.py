#Parqueadero: cobro por horas

print("Bienvenido al parqueadero")

primera_hora = 5000
horas_adicionales = 3000

print("Ingrese el número de horas que desea parquear: ")

horas = int(input())
total_a_pagar = primera_hora + (horas * horas_adicionales)

print("El total a pagar es: ", total_a_pagar)