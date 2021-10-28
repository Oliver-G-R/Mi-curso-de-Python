"""
    Una función sirve para reutilizar lógica en cualquier parte 
    de nuestro código.

    Una función se ve así:
    def nombre_funcion(parametros):
        # código
        return valor
    
    Para declarar una función, se utiliza la palabra reservada "def"
    y se le asigna un nombre. Seguido de este nombre se le asigna 
    un paréntesis que contiene los parámetros que recibe la función, 
    si es que los va a recibir. En el paréntesis se pueden poner 
    los parámetros separados por coma, en el cuerpo de la función se pueden poner instrucciones que se ejecutarán cuando la función sea llamada.
    Finalmente si hay que retornar un valor, se utiliza la palabra reservada
    "return" y se le asigna un valor.
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

# Se pasa un parametro a la función con un valor por defecto y se usa para imprimirlo en pantalla


def welcome(userName="USER"):
    print(f"Hola, bienvenido {userName}")


"""
    Cuando hay mas de un parametro, se pueden pasar separados por coma he inlcuso
    se puede asignar un valor por defecto a los parametros que no sean obligatorios
"""
"""
    La funcion login recibe dos parametros, el primero es el correo y el segundo
    es la contraseña.
    Para que la funcion funcione, se debe pasar como parametro el usuario y la contraseña
    que se encuentran en el arreglo users.

    Dentro de la funcion se recorre el arreglo users y se compara la contraseña junto con el correo, con los parametros que se pasan a la funcion.
    Si el correo y la contraseña coinciden, se manda a llamar a la función welcome y se le pasa como parametro el nombre del usuario.
"""


def login(email, password):
    for user in users:
        if user["email"] == email and user["password"] == password:
            welcome(user["name"])
            break
    else:
        print("Usuario o contraseña incorrectos")


login("Kiley.Langosh64@hotmail.com", "SHNKnDaxsdDlth6")
