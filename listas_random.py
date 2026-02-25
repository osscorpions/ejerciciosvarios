'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> 
es cada una de las asignaturas de la lista. '''

import os

materias = []
while True:
    materia = input("Escribe las materias: ")
    os.system("cls")
    materias.append(materia)
    
    if materia == "q":
            break
    
    for i in materias:
        print(f'Yo estudio {i}')
    