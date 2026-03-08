diccionario = {"name": "yosmel",
               "age": 30,
               "city": "New York",
               "country": "USA"
               }
claves = diccionario.keys() #devuelve las claves del diccionario

claves = diccionario.get("name") #devuelve el valor de la clave especificada

#diccionario.clear() #elimina todos los elementos del diccionario

diccionario.pop("name") #elimina el elemento con la clave especificada

diccionario_iterable = diccionario.items() #devuelve una vista de los pares clave-valor del diccionario


print(diccionario_iterable)
