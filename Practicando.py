mensaje = "folder"
mensaje += " de pasajeros"
print(mensaje)

aperitivo = " premium"
print(mensaje + aperitivo)

numero_uno = 56
numero_dos = 74
print("El resultado es")
print(numero_uno + numero_dos)

numero_tres = 24
numero_cuatro = 46
resultado = numero_tres + numero_cuatro
print("El resultado de tu suma es ", resultado)

buscar = "Juan paso matematicas"
posicion_subcadena = buscar.find("matematicas")
print(posicion_subcadena)
extraer_subcadena = buscar[10:21]
print(extraer_subcadena)
print(buscar == mensaje)

operadores_uno = 10
operadores_dos = 5
print("Los numeros utilizados en las operaciones son:  1 =", operadores_uno)
print("2 =", operadores_dos)

print("suma:")
resultado_op = operadores_uno + operadores_dos
print("El resultado de la suma", resultado_op)

print("resta:")
resultado_op = operadores_uno - operadores_dos
print("El resultado de la resta", resultado_op)

print("multiplicación:")
resultado_op = operadores_uno * operadores_dos
print("El resultado de la multiplicación", resultado_op)

print("exponente:")
resultado_op = operadores_uno**operadores_dos
print("El resultado de la exponente", resultado_op)

print("división:")
resultado_op = operadores_uno / operadores_dos
print("El resultado de la división", resultado_op)

print("Modulo:")
resultado_op = operadores_uno % operadores_dos
print("El resultado del modulo", resultado_op)

print("división real:")
resultado_op = operadores_uno // operadores_dos
print("El resultado de la división", resultado_op)

palabra = input("Escribe una palabra: ")
valor = int(input("Escribe un valor:"))
print("Esta es tu palabra ", palabra)
print("Esta es tu número ", valor)
