palabra = input("Ingrese la oración que desea invertir: ")
string = []
cadenaInvertida = ""

for inver in palabra:
    string.append(inver)

for i in range(len(palabra) - 1, -1, -1):
    cadenaInvertida += string[i]
print(f"Está es la oración: {cadenaInvertida}")
