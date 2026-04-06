'''
En un examen hay 40 preguntas y cada fallo quita 0.10 puntos.
Haz una función que calcule la nota con base en 10 puntos
a partir de las preguntas acertadas del examen.
'''

def calcula_nota(aciertos):
    nota =(aciertos * 0.25) - (40 - aciertos) * 0.10
    return nota

aciertos = int(input("Introduce el número de aciertos: "))
print(calcula_nota(aciertos))
