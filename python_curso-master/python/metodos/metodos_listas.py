#creando una lista con list()
lista = list (["word", "36", "3", "4", "five"])

#devuelve cantidad de elementos de la lista
cantidad_de_elementos = len(lista)

#agregando un elemento a la lista con append()
lista.append("six")

#agrendo varios elementos en un indice especifico con insert()
lista.insert(0, "zero")

#agregando varios elementos a la lista con extend()
lista.extend(["six","seven"])

#eliminando un elemento de la lista con remove()
lista.remove("zero")

#eliminando un elemento de la lista por su indice con pop()
lista.pop(2)

lista.sort(reverse=True) #ordena la lista alfabeticamente #reverse=True ordena de forma descendente
lista.reverse() #invierte el orden de la lista

print(lista)
print(cantidad_de_elementos)
print(lista[0])
