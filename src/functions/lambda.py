"""
    Las funciones lambda son funciones anónimas, 
    son funciones que no tienen nombre, pero sí una sintaxis.

    Estructura:
        lambda argumentos: expresión

    Ejemplo:
        lambda x: x + 1
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
    Deacuerdo al parametro name, cuando lo recibe,
    devuelve el valor de la propiedad name más el
    texto de la bienvenida.
"""
welcome = lambda name="User": f"Welcome {name}"

"""
    Valida si al final de la cadena de texto tiene la cadena 
    @gmail.com del parametro email.
"""

validateEmail = lambda email: email.endswith("@gmail.com")

"""
    Recibe el parametro city y devuelve una lista con los usuarios que viven en esa ciudad.
    Esto lo logra hacer recorrriendo la lista de usuarios y comparando el valor de la ciudad.
"""

getEmail = lambda city: [user["email"] for user in users if user["city"] == city]

print(getEmail("Paris"))
print(welcome())
