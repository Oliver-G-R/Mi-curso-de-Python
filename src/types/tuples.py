"""
    Las tuplas son parecidas a las listas pero son 
    inmutables y con menos posible acceso, son utilizadas 
    para mantener datos que no se van a modificar. 
    De esta manera su datos almacenados son más seguros.
"""

privateIps = ("226.15.27.32", "125.122.161.197", "47.42.194.98")

# segunda forma de declarar una tupla
privateIps2 = tuple(("226.15.27.32", "125.122.161.197", "47.42.194.98"))

# De esta forma se elimina toda la tupla
del privateIps

# Se muestra el dato que se encuentra en la posición 0
print(privateIps2[0])
