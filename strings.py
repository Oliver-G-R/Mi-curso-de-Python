# Ejemplos de funciones con cadenas
userName = "oliver_834_2"

# usuario en mayusculas
userNameU = userName.upper()

# usuario en minusculas
userNameL = userName.lower()

# usuario en mayusculas y minusculas
userNameC = userName.capitalize()

# busca la posicion de una cadena y arroja el numero de la posicion
"""
    Se empieza a contar desde el 0
    oliver_834_2 -> 11 indices
    o -> 0
    l -> 1
    i -> 2
    v -> 3
    e -> 4
    r -> 5
    _ -> 6
    8 -> 7
    3 -> 8
    4 -> 9
    2 -> 10
"""
userNameFind = userName.find("_")

# Remplaza todas las apariciones de una cadena en otra
userNameR = userName.replace("_", "@")

# Cuenta el numero de caracteres de una cadena
userNameCount = userName.count("_")

# Separa una cadena en una lista
userNameSplit = userName.split("_")

# Cantidad de caracteres de una cadena
userLength = len(userName)

userNameIndex = userName.index("o")
print(userNameIndex)
