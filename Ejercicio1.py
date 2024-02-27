import sys

print("--------------------------")
print("|   Dias de vacaciones   |")
print("|          Rappi         |")
print("--------------------------")

vacaciones = 0
nombre = input("¿Con quien tengo el gusto? ")
print("¡Hola! Mucho gusto", nombre)
antiguedad = int(input("Ingrese la cantidad de años que a trabajado en la empresa: "))

if antiguedad < 1:
    print("Aún no tienes derecho a vacaciones.")
    sys.exit()

print("Existen 3 departamentos:")
print(
    "1. Departamento de atención a cliente.\n2. Departamento de lógistica.\n3. Gerencia."
)
claveDepartamento = int(input("Ingrese su clave (1, 2 o 3): "))

if claveDepartamento == 1:
    if antiguedad == 1:
        vacaciones = 6
    elif antiguedad >= 2 and antiguedad <= 6:
        vacaciones = 14
    elif antiguedad >= 7:
        vacaciones = 20
elif claveDepartamento == 2:
    if antiguedad == 1:
        vacaciones = 7
    elif antiguedad >= 2 and antiguedad <= 6:
        vacaciones = 15
    elif antiguedad >= 7:
        vacaciones = 22
elif claveDepartamento == 3:
    if antiguedad == 1:
        vacaciones = 10
    elif antiguedad >= 2 and antiguedad <= 6:
        vacaciones = 20
    elif antiguedad >= 7:
        vacaciones = 30
else:
    print("Esa no es una opción valida.\n Por favor vuelva a intentarlo.")

print("La cantidad de vacaciones que le corresponde es de:")
print(vacaciones, "días.")
