#creando una lista se puede modifivar
lista = ["yosmel", "shair", 20, 1.65, True]
#creando una tupla no se puede modificar
tupla = ("yosmel", "shair", 20, 1.65, True)

print(lista[3])#acceder a un elemento de la lista

print(lista[-1])#acceder al ultimo elemento de la lista

lista[0] = "el pepe" #modificar un elemento de la lista

#tupla[0] = "el pepe" esto da error porque las tuplas no se pueden modificar

#ceramdo conjuntos no se pueden modificar y no tienen orden (set)
conjunto = {"yosmel", "shair", 20, 1.65, True}

#creando un diccionario (key:value)
diccionario = {
    "nombre": "yosmel",
    "apellido": "shair",
    "edad": 20,
    "estatura": 1.65,
    "soltero": True
}
print(diccionario["estatura"])#acceder a un elemento del diccionario