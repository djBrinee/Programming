# Escribir un programa que reciba una secuencia de DNA o RNA, indetifique el tipo de molecula y la imprima letra por letra en la pantalla.


# ADN -> T
# ARN -> U

secu = input("Introduzca una secuencia: ")
resp = ""

if ("T" in secu):
    resp = "ADN"
elif("U" in secu):
    resp = "ARN"
else:
    resp = "Inválida"

print("LA secuencia introducida es: " + resp)
print("\n\n")

print("Letra por letra")
for i in secu:
    print(i)
