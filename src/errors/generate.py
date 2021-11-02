"""
    Se pueden generar error de forma dinámica.

    Esto se hace con la función raise.

    La función raise es una función que se puede usar para lanzar una excepción.
    Ejemplo: 
        raise ValueError('No se puede dividir por cero')

    Esta función lanza una excepción de tipo ValueError, el mensaje de error es el que se le pasa como parámetro. DE esta forma tenemos un error de tipo ValueError personalizado.

"""

try:
    raise ValueError("Este es un error personalizado")
except ValueError as e:
    print(e)
