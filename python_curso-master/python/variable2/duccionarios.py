#creando un diccionario con dict()
diccionario = dict(nombre="yosmel",apellido="matos,palomino")

#las listas no pueden ser claves

diccionario1 = {frozenset(["shair","palomino"]):"es huapo"}

#creando diccionarios con fromkeys
diccionario2 = dict.fromkeys(["nombre","apellido"])
diccionario3 = dict.fromkeys(["nombre","apellido"],"desconocido")


print(diccionario2)
print(diccionario3)
print(diccionario1)
print(diccionario["nombre"])