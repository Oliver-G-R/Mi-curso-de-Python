"""
    El bucle for se usa para iterar sobre una secuencia de valores.
    El bucle for tiene una sintaxis muy similar a la de una función.
    La sintaxis es la siguiente:
    
    for <variable> in <secuencia>:
        <instrucciones>
    
"""

users = [
    {
        "name": "John",
        "surname": "Smith",
        "age": 25,
        "city": "New York",
        "password": "beh0KR7o6qRXpFq",
        "email": "Odell47@hotmail.com",
    },
    {
        "name": "Jane",
        "surname": "Doe",
        "age": 30,
        "city": "London",
        "password": "SHNKnDaxsdDlth6",
        "email": "Kiley.Langosh64@hotmail.com",
    },
    {
        "name": "Jack",
        "surname": "Doe",
        "age": 35,
        "city": "Paris",
        "password": "ju2tj6uEGcCI9wc",
        "email": "Shannon70@hotmail.com",
    },
]

"""
    Itera sobre la lista de usuarios y los imprime 
    en pantalla, sin la necesidad de ponerlos
    uno a uno.
"""
"""for user in users:
    print(user)"""

"""
    Podemos iterar cada uno de los datos de nuestra 
    lista y mediante un condicional nos aseguramos
    de sacar en pantalla solo los usuarios 
    mayores a 35 años.

    Para ello, vamos a usar un condicional if
    dentro de nuestro for para que nos permita 
    saber si el usuario es mayor de 35 años.
    Y haciendo uso de la clave "age" y "nombre"
    de nuestro diccionario de usuarios podemos 
    acceder a los datos de cada uno.

    Si es mayor, imprimimos en pantalla el usuario,
    y sino es mayor, no imprimimos nada.


"""

for user in users:
    if user["age"] > 30:
        print(f'El usuario {user["name"]} es mayor a 30 años')

"""
    Iteramos sobre la lista de usuarios y vamos a cambiar el provedor 
    de correo de cada uno de ellos.
    Evaluando que si su provedor de correo no es de gmail este 
    cambiara y si es de gmail no se cambiara.
"""

for user in users:
    if "@gmail.com" in user["email"]:
        user["email"] = user["email"] + ".com"
    else:
        user["email"] = user["email"] + "@gmail.com"

"""
    Mostar por pantalla los usuarios que tienen derecho a un bono
    de 400 dollars si su edad es mayor de 65 años y si su edad es
    menor de 65 pero vive en la ciudad de paris mostrar que si tiene derecho
    al bono.
"""

for user in users:
    if user["age"] > 65:
        print(f'El usuario {user["name"]} tiene derecho al bono de 400 dollars')
    elif user["age"] < 65 and user["city"] == "Paris":
        print(f'El usuario {user["name"]} tiene derecho al bono de 400 dollars')
    else:
        print(f'El usuario {user["name"]} no tiene derecho al bono de 400 dollars')
