# Forma uno de declarar una lista
userNames = ["juan", "pedro", "maria", "jose"]

# Forma dos de declarar una lista de usuarios
userNames2 = list(("juan", "pedro", "maria", "jose"))

# lista basada en un rango
userNames3 = list(range(1, 10))

"""
   De esta forma se puede agregar elementos a la lista,
   con el metodo append(), a este se le puede agregar cualquier tipo de dato.
"""
userNames.append("Ernesto")

"""
    Con el método pop() se puede eliminar un elemento de la lista, pasando su indice.
    Y de no pasarle un indice, se eliminara el ultimo elemento de la lista.

    RECUERDA QUE EL INDICE COMIENZA EN 0
"""
userNames.pop(0)

"""
    El método extend() permite agregar una lista a otra, tomando todos los elementos de la lista y los agrega 
    haciendolos parte de la lista que se le pasa como parametro.
"""
userNames.extend(["Jhoana", "Pepe"])

"""
    insert() permite insertar un elemento en una posicion especifica de la lista. Pasando el indice y el elemento.
"""
userNames.insert(1, "OLiver")

# Elimina todos los elementos de la lista
# userNames.clear()

"""
  sort orndena los elementos de la lista de menor a mayor.
  Pero si se quiere ordenar de mayor a menor, se puede pasar el parametro reverse=True.  
"""
userNames.sort()


print(userNames)
