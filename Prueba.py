"Menú de calificaciones"
print("Hola! Es hora de sacar tu promedio")
nombre = input("¿Cuál es tu nombre? ")
cant = 0
arreglo_calif = []
i = -1

print("Mucho gusto", nombre)
cant = int(input("¿Cúantas materias llevas? "))
if cant >= 1 or cant <= 9:
    print("Lo siento pero solo puedo promediar 9 materias")
else:
    print("Muy bien, entonces dame tus calificaciones")
