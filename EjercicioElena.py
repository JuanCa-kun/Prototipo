# Entrada de la palabra
palabra = input("Ingrese una palabra: ")

# Recortar la palabra a máximo seis caracteres
palabra_recortada = palabra[:6]

# Ordenar las letras de acuerdo a su valor ASCII
letras_ordenadas = sorted(palabra_recortada)

# Generar cadena de ADN
cadena_adn = "".join(letras_ordenadas)

# Calcular el valor ASCII total de la cadena y negarla a 32 bits
valor_ascii_total = sum(ord(c) for c in cadena_adn)
cadena_negada = "{:032b}".format(~valor_ascii_total & 0xFFFFFFFF)

# Convertir la cadena de 32 bits a un número decimal
numero = int(cadena_negada, 2)

# Verificar si el número sobrepasa 122
if numero > 122:
    resultado = str(numero)
else:
    resultado = chr(numero)

# Mostrar el resultado
print("ADN:", cadena_adn)
print("Negación de la palabra:", resultado)
