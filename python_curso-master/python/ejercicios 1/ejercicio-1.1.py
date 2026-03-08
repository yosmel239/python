#duracion de los cursos
cursos_max = 7
cursos_promedio = 4
cursos_minimo = 2.5
curso_dalto = 1.5

#diferencia de la duracion de los cursos
diferencia_max = 100 - curso_dalto * 1000 // cursos_max / 10
diferencia_promedio = 100 - curso_dalto / cursos_promedio * 100
diferencia_minima = 100 - curso_dalto / cursos_minimo * 100

#tiempo vasio
tiempo_vasio_promedio = 5
tiempo_vasio_dalto = 3.5

#calculando el tiempo vasio reducido
tiempo_vasio_reducido = 100 - cursos_promedio *1000 // tiempo_vasio_promedio / 10
tiempo_vasio_reducido_dalto = 100 - curso_dalto * 1000 // tiempo_vasio_dalto / 10

print("-------------------------")
print("diferencias de los cursos:")
print(f" - La diferencia entre la duracion del curso mas largo y el curso de dalto es: , {diferencia_max}%" )
print(f" - La diferencia entre la duracion del curso promedio y el curso de dalto es: , {diferencia_promedio}%")
print(f" - La diferencia entre la duracion del curso mas corto y el curso de dalto es: , {diferencia_minima}%")
print("-------------------------")
print("reduccion del tiempo vasio:")
print(f" - La reduccion del tiempo vasio promedio es: {tiempo_vasio_reducido}% y el tiempo reducido del curso de dalto es: {tiempo_vasio_reducido_dalto}%")
print("-------------------------")
print("equivalencia de horas:")
print(f" - ver 10 horas de este curso equivale a ver {cursos_promedio *100// curso_dalto /10 } horas de cursos de promedio")
print(f" - ver 10 horas de otros cursos equivale a ver {curso_dalto *100// cursos_promedio /10 } horas del curso de dalto")