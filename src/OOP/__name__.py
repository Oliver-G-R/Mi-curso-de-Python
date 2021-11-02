"""
    En python hay variables privadas, las cuales ya estan 
    definidas por el lenguaje.

    Un ejemplo sería __name__, que es una variable privada
    que se usa para saber si el archivo se esta ejecutando
    como modulo o como script.

    Ees decir, si __name__ es igual a __main__, entonces
    el archivo se esta ejecutando como script, de lo contrario
    se esta ejecutando como modulo.

    Aunque ya esta definida por el lenguaje, podemos
    usarlo para estructurar nuestros codigos. Y saber si se 
    trata de un modulo o de un script.
    
"""


class ProccessNote:
    def __init__(self, notes):
        self.notes = notes

    def showNotes(self):
        for i in self.notes:
            print("=========")
            for key in i:
                print(key, i[key])

    def getNotesForId(self, id):
        for i in self.notes:
            if i["id"] == id:
                return i
        return []


"""
    Sin importar cuantas clases o funciones hay en el archivo,
    siempre se podrá identificar de donde se esta ejecuta nuestro 
    codigo.
"""

if __name__ == "__main__":
    notes = []

    amount = int(input("Cantidad de notas: "))

    for i in range(amount):
        print(f"Nota {i+1}: ")

        title = input("Titulo: ")
        content = input("Contenido: ")

        notes.append({"id": i + 1, "title": title, "content": content})

    pNote = ProccessNote(notes)
    pNote.showNotes()

    searchNote = int(input("Buscar nota por id: "))
    print(pNote.getNotesForId(searchNote))
