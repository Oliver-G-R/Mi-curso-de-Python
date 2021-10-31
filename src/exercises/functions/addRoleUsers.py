"""
    Preguntar la cantidad de usuarios a registrar y despues
    agregarlos a un diccionario como rol y usuario.

    Para finalizar se debe simular un inicio de sesion con
    usuario y contraseña y al inicio de sesion se debe mostrar
    un mensaje de bienvenida con el rol del usuario.
"""

users = []


def welcome(user, rol):
    print(f"Bienvenido {user} tu rol es de {rol}")


def login(user, password):
    for i in users:
        if i["user"] == user and i["password"] == password:
            welcome(user, i["rol"])
            break
        else:
            print("Usuario o contraseña incorrecta")


print("Cantidad de usuarios")
cantidad = int(input())

for i in range(cantidad):
    print("Usuario: ")
    user = input()

    print("Rol: admin | user")
    rol = input().lower()

    print("Password: ")
    password = input()
    users.append({"user": user, "rol": rol, "password": password})

# borrar consola
print("Ingresa tu usuario")
UnicodeTranslateError = input()

print("Ingresa tu password")
password = input()

login(user, password)
