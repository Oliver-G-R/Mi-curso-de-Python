users = [
    {
        "name": "John",
        "surname": "Smith",
        "age": 25,
        "city": "New York",
        "email": "Odell47@hotmail.com",
    },
    {
        "name": "Jane",
        "surname": "Doe",
        "age": 30,
        "city": "London",
        "email": "Kiley.Langosh64@hotmail.com",
    },
    {
        "name": "Jack",
        "surname": "Doe",
        "age": 35,
        "city": "Paris",
        "email": "Shannon70@hotmail.com",
    },
]

# Se obtiene el usuario por medio de su indice
oneuser = users[0]

"""
    Se obtiene el correo del usuario por medio de su clave
    en el diccionario. De este modo se podría acceder a
    cualquier elemento del diccionario con la propiedas 
    que se quiera sacar.
"""
usersForEmail = oneuser.get("email")

# Obtiene las claes del diccionario
oneuser.keys()
# Obtiene los valores del diccionario
oneuser.values()

newusers = {
    "name": "Rick",
    "surname": "Lennon",
    "age": 25,
    "city": "New York",
    "email": "Khalid_Blick@yahoo.com",
}

# Agregando un nuevo usuario
users.append(newusers)

print(users)
