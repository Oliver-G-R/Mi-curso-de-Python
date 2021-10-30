"""
    Python soporta la programación orientada a objetos, nos 
    permite crear clases representando modelos de datos.
    Por ejemplo, una clase que represente un usuario, 
    podría tener un nombre, una contraseña y un correo.

    Estos vendrían siendo los atributos, también podría tener
    métodos para cambiarlos,  como por ejemplo
    la contraseña o correo, incluso podría tener métodos para
    iniciar sesión, cerrar sesión, etc.

    Entonces una clase es un modelo de datos, y un objeto es
    una instancia de una clase.

    ¿Pero qué es una instancia?
    Una instancia es una copia de una clase, en este caso 
    una copia de la clase Usuario, de este modo podríamos
    utilizar la misma clase para crear varias instancias
    y de este modo poder utilizar los métodos y atributos
    de la misma.

    Por lo que si hacemos uso de esto, podemos utilizarla 
    en culquier parte de nuestro código sin tener que
    repetir cierta lógica.

    =====================================================================
    Algo muy importante a tener en cuenta es es la forma en que 
    se crean las clases, ya que en distitnos lenguajes de programación
    se crean de diferentes formas, y en Python es muy fácil de crear
    una clase, y es muy sencillo de utilizar.

    Estructura base:

    class NombreClase:
        atributo = "valor"
        atributo = "valor"
        atributo = "valor"

        def __init__(self, atributo1, atributo2):
            self.atributo1 = atributo1
            self.atributo2 = atributo2

        def metodo(self):
            pass

    Se utiliza la palabra reservada class, y se le pasa el nombre
    que va tener la clase, se pueden tener atributos globales 
    que sean compartidos en toda la clase, y no dentro de un 
    bloque que tenga una función.

    El método __init__ es un método especial que se
    ejecuta cuando se crea una instancia de la clase, y se
    utiliza para inicializar los atributos de la misma.

    La palabra reservada self, es una referencia a la
    instancia que se está creando, y se utiliza para
    acceder a los atributos de la misma o para modificarlos.
    Esta palabra en otros lenguajes se llama this, la cual 
    tiene el miso trabajo.
    En todo caso es importante pasar la palabra reservada
    self a todos los métodos, ya que es la que se utiliza
    para acceder a los atributos de la misma.

    Dado que ya tenemos atributos globales, un método especial
    para inicializar los atributos, ahora también podemos
    tener más metodos que nos ayuden con la lógica de nuestra 
    clase, como por ejemplo uno que nos sirva para un mensaje de 
    bienvenida, o uno que nos sirva para cerrar sesión.

    Cualquiera de los dos esta bien, en esta estructura, vemos un 
    método 

    def metodo(self):
        pass

    con la palabra reservada pass, esta sirve para indicar que
    no se va a realizar ninguna acción, y que no se va a ejecutar
    ninguna lógica.

    Esto nos funciona para definir los métodos que se van a utilizar
    en la clase para despues incluir su lógica.
    
    =====================================================================

"""

coursesPremium = [
    {
        "name": "Aprende python de 0 a experto",
        "price": 200,
        "description": "Ten la seguirdad que con este curso seras todo un master en python",
    },
    {
        "name": "Kali Linux de 0 a expero",
        "price": 600,
        "description": "¿Cansado de no poder usar Kali Linux como un pro?",
    },
]

coursesBasics = [
    {
        "name": "¿Cómo crear una api rest? - Curso base",
        "price": 100,
        "description": "",
    }
]

"""
    Se crea una clase llamada User, que tendrá los atributos
    name, password, email y premium, la cual estara en True.

    También se crea un método __init__, que recibe como parametro
    estas propiedades para despues inicializarlas.

    Se crea el método get_premium_user, que recibe como parametro
    mony con valor inicial de 0. Este método se crea para cambiar mediante
    una bloque lógico el valor de premium, deacuerdo a el valor de mony.

    Seguido de esto, se crea el método get_courses, el cual evalua
    si el usuario es premium o no, y dependiendo de eso, retorna
    una lista con los cursos que le corresponden.
"""


class User:
    def __init__(self, name, email, password, premium=False):
        self.name = name
        self.email = email
        self.password = password
        self.premium = premium

    def get_premium_user(self, mony=0):
        if mony >= 465:
            self.premium = True
        else:
            self.premium = False

    def get_courses(self):
        if self.premium:
            return coursesPremium + coursesBasics
        else:
            return coursesBasics


# Se hace una instancia de la clase User y se le asignan los valores
user = User("John", "Timmy62@yahoo.com", "jsjij8s")

# Accedemos a los métodos de la clase User y pasamos su valor
user.get_premium_user(700)

# Imprimimos el valor del atributo nombre
print(f"{user.name} Tienes acceso a los siguientes cursos")

# Recorremos la lista de cursos y los imprimimos
"""
    Ya que el método get_courses retorna una lista ya evaluada
    segun el tipo de usuario, podemos utilizar un for para 
    recorrerla e imprimirla.
"""
for course in user.get_courses():
    print("============")
    print(course["name"])
    print(course["price"])
    print(course["description"])
