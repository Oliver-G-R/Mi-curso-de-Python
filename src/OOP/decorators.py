"""
    Los decoradores son propiedades de clases o funciones que se pueden
    aplicar a una propiedad o método de una clase.

    Estos son:
        - @classmethod -> Modifica el comportamiento de una clase sin necesidad de instanciarla.
        - @staticmethod -> Permite tener una función sin parámetros.
        - @property ->  Permite tener una función como propiedad.

"""

# implementa todos los decoradores que hay en python


class validateUserFields:
    def __init__(self):
        self.errors = []

    """
        @classmethod -> Nos ayuda a usar una función sin que esta se convierta en un 
        objeto.
        El cls es una variable que se puede usar para acceder a las funciones de una clase.
    """

    @classmethod
    def validateEmail(cls, email):
        if len(email) > 5:
            if "@" in email:
                return True
        else:
            return False

    @classmethod
    def validatePassword(cls, password):
        if len(password) > 5:
            return True
        else:
            return False

    """
        @staticmethod -> Ayuda a tener una funcion dentro de una clase
        sin tener que pasarle parametros. A diferiencia de @classmethod, 
        si es necessario convertir la clase primero en un objeto.
    """

    @staticmethod
    def welcomeMessage():
        print("Bienvenido ingresa tus datos")

    """
        @property -> Nos ayuda a crear una funcion que se pueda llamar 
        como una propiedad retornando un valor. Y al igual que 
        @staticmethod, es necesario convertir la clase primero en un objeto.
    """

    @property
    def getErrors(self):
        return self.errors


userV = validateUserFields()

userV.welcomeMessage()

print("Ingresa el correo elctronico")
email = input()


if validateUserFields.validateEmail(email):
    print("Correo valido")
else:
    userV.errors.append("Correo invalido")
    print("Correo invalido")

print("Ingresa la contraseña")
password = input()


if validateUserFields.validatePassword(password):
    print("Contraseña valida")
else:
    userV.errors.append("Contraseña invalida")
    print("Contraseña invalida")

print(f"Cantidad de errores: {len(userV.getErrors)}")
for error in userV.getErrors:
    print(error)
