print("+++++++++++++++++++++")
print("+  ¿Cúal es mayor?  +")
print("+++++++++++++++++++++")

print("Hola! Esté programa es utilizado para clasificar los números de mayor a menor.")

valorUno = int(input("Ingresa el primer valor: "))
valorDos = int(input("Ingresa el segundo valor: "))
valorTres = int(input("Ingresa el tercer valor: "))

if valorUno < valorDos < valorTres:
    numeros_ordenados = [valorUno, valorDos, valorTres]
elif valorUno < valorTres < valorDos:
    numeros_ordenados = [valorUno, valorTres, valorDos]
elif valorDos < valorUno < valorTres:
    numeros_ordenados = [valorDos, valorUno, valorTres]
elif valorDos < valorTres < valorUno:
    numeros_ordenados = [valorDos, valorTres, valorUno]
elif valorTres < valorUno < valorDos:
    numeros_ordenados = [valorTres, valorUno, valorDos]
else:
    numeros_ordenados = [valorTres, valorDos, valorUno]

print("Los números ordenados de menor a mayor son:", numeros_ordenados)
