#defivir una variable con canelCase
nombreCompleto = "yosmel shair"
#definir una variable con snake_case
nombre_completo ="yosmel shair"
nombre = "yosmel"
edad ="20"
estatura = "1.65"
#concatenar con f-string
datos = f"{nombre_completo} tienes {edad} años y mides {estatura} metros"
print(datos)

del edad#del es para borrar una variable

print( (edad) in datos)#devuelve true o false si la variable esta en el string
print( (estatura) not in datos)#devuelve true o false si la variable no esta en el string

#concatemar con +
datos2 = "hola" + "como estas"