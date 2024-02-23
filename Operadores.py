print("-------------------------")
print("|Operadores relacionales|")
print("-------------------------")

num_uno = int(input("\nIngresa el primer número que quieres comparar: "))
num_dos = int(input("\nIngresa el segundo número que quieres comprar: "))

if num_uno == num_dos:
    print("El", num_uno, "y el", num_dos, "son iguales")
else:
    print("El", num_uno, "y el", num_dos, "son diferentes")

if num_uno < num_dos:
    print("El número", num_dos, "es mayor que", num_uno)
else:
    print("El número", num_uno, "es mayor que", num_dos)

if num_uno >= num_dos:
    print("El numero", num_uno, "es mayor igual que", num_dos)
else:
    print("El numero", num_uno, "es menor igual que", num_dos)
