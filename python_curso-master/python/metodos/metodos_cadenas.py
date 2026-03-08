cadena1 = "hola matos"
cadena2 = "bienvenido a la wed"
cadena3 = "12345"
cadena4 = "soyhuapo"

resultado = dir(cadena1)
resultado2 = cadena1.upper()

#convierte en mayusculas
mayuscula = cadena1.upper()

#convierte en minusculas
minuscula = cadena1.lower()

#convierte la primera letra en mayuscula
primera_mayuscula = cadena1.capitalize()

#busca una subcadena y devuelve la posicion
encontrar = cadena1.find("a")

#busca una subcadena y devuelve un error si no la encuentra
busqueda = cadena1.index("hola")

#si  es numerico es true si no false
es_numerico = cadena3.isnumeric()

#si es alfanumerico es true si no false
es_alfanumerico = cadena4.isalpha()

#buscamos una cadena en otra cadena, devuenve las cantidad de veses que coinside
contar_coinsidencias = cadena2.count("a")

#contar cuantos caracteres tiene la cadena
encontrar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada,si es asi devuelve true si no false
empieza_con = cadena2.startswith("bienvenido")

#verificamos si una cadena termina con otra cadena dada,si es asi devuelve true si no false
termina_con = cadena1.endswith("matos")

#si el valor 1 encuentra en la cadena original remplaza el 1 por el valor 2
cadena_nueva = cadena1.replace("hola", "hello")
cadena_nueva2 = cadena_nueva.capitalize()

#separar cadenas con la cadena que le digamos
cadena_separada = cadena2.split(" ")



print(cadena_separada[2])
print(cadena_separada)
print(es_alfanumerico)
print(contar_coinsidencias)
print(resultado2)
print(empieza_con)
print(termina_con)
print(cadena_nueva2)