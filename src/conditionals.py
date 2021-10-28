"""
    Las condiciones son una forma de evaluar una expresión y
    determinar si se cumple o no.
    De esta forma se pueden hacer desiciones logicas en el codigo.

    En python se pueden evaluar condiciones con if, elif y else.
    Cada uno de estos bloques de codigo se ejecuta en el orden que se
    encuentra. Y si se cumple la condicion, se ejecuta el bloque de codigo
    que esta dentro del if.

    Hay diferentes operadores que se pueden usar para evaluar condiciones.
    Los operadores son:
        - == (igual a)
        - != (no igual a)
        - > (mayor que)
        - < (menor que)
        - >= (mayor o igual que)
        - <= (menor o igual que)
        - and (y)
        - or (o)
        - not (no)
    
    Cada uno de estos operadores se puede usar en una condicion y 
    se puede usar en una condicion con una expresion.
    
"""
ageMaria = 20
ageJuan = 18

if ageMaria == ageJuan:
    print("Maria y Juan tienen la misa edad")
elif ageMaria != ageJuan:
    print("Maria y Juan tienen edades distintas")


if ageMaria > ageJuan:
    print("Maria es mayor que Juan")
else:
    print("Maria es menor que Juan")
