#creando un conjunto con set([])
conjunto = set(["yosmel","matos",16])
#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)


#teoria de conjunto
conjuntoA = {1,3,5,7,9}
conjuntoB = {1,3,5} 
#si es un subconjunto
resultado = conjuntoB.issubset(conjuntoA)
resultado2 = conjuntoB <= conjuntoA
#si es un superconjunto
resultado3 = conjuntoB.issuperset(conjuntoA)
resultado4 = conjuntoB > conjuntoA
#verificar si hay algun numero en comun
resultado5 = conjuntoB.isdisjoint(conjuntoA) #false es true #true es false 


print(resultado5)