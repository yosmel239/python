animales = ["perro", "gato", "conejo", "hamster"]
numeros = [2, 2, 3, 4, 5]

#recorriendo la lista de animales
for animal in animales:
    print(animal)


#recorriendo la lista de numeros multiplicado por 10    
for numero in numeros:
    numeros_10 = numero * 10
    print(numeros_10)
    
    
#recorriendo ambos listas al mismo tiempo con la función zip
for animal, numero in zip(animales, numeros):
    print(f"el : {animal} , tiene: {numero} años")    
    
for distancia in range(1,3):
    print(f"la distancia es: {distancia} km")    
    
for num in range(len(numeros)):
    print(numeros[num])