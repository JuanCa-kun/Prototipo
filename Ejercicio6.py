palabra = input("Hola! Dame la cadena a modificar a continuación: ")
eliminar = input("Dame la subcadena a eliminar: ")
substring = ""

var = palabra.count(eliminar, 0)

indice = palabra.find(eliminar)

substring = palabra[0:indice] + palabra[indice + len(eliminar) :]

substring = substring.replace("  ", " ")

subsubstring = palabra.replace(eliminar, "")

print(var)
print(f"La nueva cadena es: {substring}")
print(f"La nueva cadena es: {subsubstring}")
