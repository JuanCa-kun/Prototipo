print("+++++++++++++++++++++")
print("+    Operaciones    +")
print("+++++++++++++++++++++")

print("Hola! Soy un programa para poder hacer operaciones aritmeticas.")
while True:
    print("Menú:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. División entera")
    print("6. Exponente")
    print("6. Modulo")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    x = float(input("Ingrese el primer valor que quiere utilizar en la operación: "))
    y = float(input("Ingrese el segundo valor que quiere utilizar en la operación: "))

    if opcion == "1":
        x += y
        print("Ha seleccionado la Opción 1. El resultado de la Suma es:", x)
    elif opcion == "2":
        x -= y
        print("Ha seleccionado la Opción 2. El resultado de la Resta es:", x)
    elif opcion == "3":
        x *= y
        print("Ha seleccionado la Opción 3. El resultado de la Multiplicación es:", x)
    elif opcion == "4":
        x /= y
        print("Ha seleccionado la Opción 4. El resultado de la División es:", x)
    elif opcion == "5":
        x //= y
        print("Ha seleccionado la Opción 5. El resultado de la División entera es:", x)
    elif opcion == "6":
        x **= y
        print("Ha seleccionado la Opción 6. El resultado de la Exponente es:", x)
    elif opcion == "7":
        x %= y
        print("Ha seleccionado la Opción 7. El resultado de la Modulo es:", x)
    elif opcion == "8":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 8.")
