"""
    Los imports son una forma de importar librerías de terceros.
    o archivos como clases, funciones, etc.

    En Python, los imports se realizan de la siguiente manera:

    import random -> importa la librería random cuando la instalas en tu proyecto.

    from directorio.fichero import funcion_clase_etc -> toma un directorio, un fichero e 
    importa una funcion.

    from directorio import fichero1.func1, fichero2.func2, fichero3.func3 -> toma un 
    directorio e importa los archivos con sus funciones correspondientes.

    from directorio.fichero import func1 as rename_func1 -> toma un directorio, un
    fichero e importa una funcion y la renombra.

"""

from helpers.filters import filter_gmail, filter_low_password

users = [
    {
        "id": "d8034b9e-4c13-4052-9bf1-a372c97e9cce",
        "username": "Tommie_Witting63",
        "password": "3t8r52t",
        "email": "Rosalia91@yahoo.com",
    },
    {
        "id": "f5bb56b9-d42c-415f-9901-ef52974e473a",
        "username": "Larissa_OConnell",
        "password": "I9ws",
        "email": "Kendall.Fisher@gmail.com",
    },
    {
        "id": "cf7df687-4226-4a55-8178-90407ff8cf75",
        "username": "Mariah_Cronin",
        "password": "zj6QG",
        "email": "Bradly_Bashirian@yahoo.com",
    },
    {
        "id": "c444971e-1d33-4444-8d5c-aa6b2b9d7211",
        "username": "Nicolette_Hintz13",
        "password": "xoPv8vWwZew0zfP",
        "email": "Myles.VonRueden42@yahoo.com",
    },
    {
        "id": "a5e4761c-2a8b-4525-9db2-900a2cc45086",
        "username": "Aurelie.Runolfsdottir66",
        "password": "6E0oBcNo013RilS",
        "email": "Raegan_Schinner98@gmail.com",
    },
    {
        "id": "ea776cb9-8863-43e0-9817-308210e5d60c",
        "username": "Magdalena.Ernser",
        "password": "jMMxQbNCU8LaTw1",
        "email": "Halle_Quigley@gmail.com",
    },
]

print("Correos de gmail")
for user in filter_gmail(users):
    print("====")
    print(f"{user['username']} - {user['email']} ")


print("\nCorreos con una contraseña no segura")

for user in filter_low_password(users):
    print("====")
    print(f"{user['username']} - {user['email']} - {user['password']} ")
