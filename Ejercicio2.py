print("*******************")
print("*   Par o impar   *")
print("*******************")

print(
    "Hola! Este es un programa que puede ayudarte a descubrir si un número es par o impar."
)
num = int(input("Proporciona el número el cual deseas saber si es par o impar: "))

if num % 2 == 0:
    print("El número", num, "es par")
else:
    print("El número", num, "es impar")
