"Condicionales"
operadores_uno = int(input("Dame el primer operador "))
operadores_dos = int(input("Dame el segundo operador "))
if operadores_uno == operadores_dos:
    print("El operador uno es igual al operador dos")
print("fin \n")

"Menú de calificaciones"
print("Hola! Es hora de sacar tu promedio")
nombre = input("¿Cuál es tu nombre? ")
cant = 0

print("Mucho gusto", nombre)
cant = int(input("Cúantas materias llevas? "))
if cant <= 0 and cant > 9:
    print("Lo siento pero solo puedo promediar 9 materias")
print("Muy bien, entonces dame tus calificaciones")
