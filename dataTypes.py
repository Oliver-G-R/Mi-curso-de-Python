# tipo string
"""
    El tipo string es una secuencia de caracteres,
    esto nos sirve para almacenar cadenas de 
    caracteres, como por ejemplo:
    "Hola mundo", para despues mostrarlo en pantalla
    y asi poder manipularlo.

"""
userName = "olivero83_root"

# tipo int
"""
    El tipo int es un numero entero.
"""

userAge = 30.3

# tipo float
"""
    Este tipo de dato es un decimal, 
    nos sirve para representar números 
    más reales para una cantidad mas exacta. 

"""
userHeight = 1.75

# tipo boolean
"""
    El tipo boolean es un tipo de dato que solo puede tener dos valores: True o False, 
    y estos valores sirven para definir si una condición es verdadera o falsa.
"""
userIsActiv = False

# tipo list
"""
    Las listas son un tipo de dato que se puede crear con una serie de elementos, estos pueden
    tener cualquier tipo de dato, estan separados por comas (,) y que puede tener una longitud variable segun sea el caso de uso.

"""
mailFollowers = [
    "Cyril_Hettinger@hotmail.com",
    "Winona_Nader@hotmail.com",
    "Victor24@yahoo.com",
]

# tipo tuple
"""
    Las tuplas son lo contrario de las listas, 
    son un tipo de dato que se puede crear con una serie de elementos, estos pueden
    tener cualquier tipo de dato, estan separados por comas (,) pero sin embargos es una lista
    que no se puede modificar (no mutable).
"""
userTuple = (1, 2, 3, 4, 5)

# tipo dict
"""
    Los diccionarios son un tipo de dato que se puede crear con una serie de elementos, estos pueden tener cualquier tipo de dato y se crean 
    mediante llaves y valores.
"""
userDict = {"name": "olivero83_root", "age": 30, "height": 1.75, "userIsActiv": False}

# De esta manera podemos imprimir todos los datos
print(userDict["name"])
