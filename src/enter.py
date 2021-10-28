"""
    Para pedir una entrada al usuario se usa la función input()
    se asigna a una variable y se encierra en el tipo de dato 
    que se quiere obtener.
"""

print("Introduce un número entero")
num = int(input())

if num > 0:
    print("El número es positivo")
else:
    print("El número es negativo")


print("Agrega un nombre de usuario")
user = input()

print("Hola " + user)


print("Introduce un decimal")
dec = float(input())

# Se encierra la variable dec en str para que se pueda imprimir
print("El decimal es: " + str(dec))
