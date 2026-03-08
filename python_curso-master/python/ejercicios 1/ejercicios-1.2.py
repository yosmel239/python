frase = input("decime una frase y yo te dire cuanto te demoras aproximadamente en decirlo, ok ")
palabra_separada =frase.split(" ")
cantidad_de_palabras = len(palabra_separada)
print(f"dijiste {cantidad_de_palabras} palabras, entonces te demorarias aproximadamente {cantidad_de_palabras * 0.5} segundos en decirlo")
if cantidad_de_palabras > 60:
    print("wow, eso es mucho procura aserlo mas corto la proxima vez")