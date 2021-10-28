"""
    El bucle while se ejecuta mientras la condición sea verdadera.
    Su sintaxis es:
        while <condicion>:
            <bloque de instrucciones>
        
"""
users = [
    {
        "name": "John",
        "surname": "Smith",
        "age": 25,
        "city": "New York",
        "password": "beh9wi",
        "email": "Odell47@hotmail.com",
    },
    {
        "name": "Jane",
        "surname": "Doe",
        "age": 30,
        "city": "London",
        "password": "Sa2h6",
        "email": "Kiley.Langosh64@gmail.com",
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
    Crear algoritmo que recorra todos la lista de usuarios y muestre por pantalla
    su correo, contraseña y nombre si su provedor de correo es de hotmail.
"""

"""usersHacked = []

while users:
    user = users.pop()
    if "hotmail" in user["email"]:
        usersHacked.append(user)


print(
    "===El patron de busqueda encontro los siguientes usuarios con el provedor de hotmail==="
)
while usersHacked:
    user = usersHacked.pop()
    print(
        f"Nombre: {user['name']} - Email: {user['email']} - Password {user['password']}"
    )
"""
"""
    Recorrer las contraseñas de los usuarios y mostrar por pantalla
    que usarios tiene la contraseña mas debil deacuerdo a la 
    longitud menor de 8.
"""

while users:
    user = users.pop()
    if len(user["password"]) < 8:
        print(
            f"La contraseña del usuario {user['name']} es muy debil -  {user['password']}"
        )
    else:
        print(
            f"La contraseña del usuario {user['name']} es muy fuerte -  {user['password']}"
        )
