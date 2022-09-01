#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.


horas = input("Horas trabajadas: ")
precio = input("Precio: ")

salida = int(horas) * int(precio)

print("El total es ", salida)


