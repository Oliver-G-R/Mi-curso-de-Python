"""
    Los errores en Python son excepciones que se lanzan cuando ocurre un error en el
    código y de esta manera se puede detectar y manejar manejando la acción o mandando
    un mensaje de error personalizado.
"""


"""
    Try - Except
    try:
        # Código que puede generar un error
    except:
        # Código que se ejecuta si se genera un error
    
    except  keybordInterrupt:
        # Código que se ejecuta si se interrumpe la ejecución del programa 
    
    finally:
        # Código que se ejecuta siempre sin importar si se genera un error o no
"""

"""
    Si da error al ingresar una cadena de texto, se ejecuta el código que está
    dentro del except, ya que este debía de ser un número entero.
"""

print("Ingresa la cantidad de registros")
try:
    cantidad = int(input())
    print("La cantidad es: ", cantidad)
except ValueError:
    print("El valor ingresado no correcto")
except KeyboardInterrupt:
    print("Has cancelado el programa")

finally:
    print("Se terminó el programa")
