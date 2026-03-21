'''
Script en Python que muestra los números de día de un calendario mensual
cualquiera recibiendo como parámetros el día de inicio y el total días 
del mes.
Que comience en miércoles y tiene 30 días.
'''
def calendario(dia_inicio=None,mes=None):
    mes = int(input("Escoge un mes: "))
    dia_inicio=int(input("Escriba el día: "))

    meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril",
            5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto",
            9:"Septiembre", 10:"Octubre",11:"Noviembre",
            12:"Diciembre"}

    
    s = 0

    dia_inicio += s % 7
    dia_inicio = dia_inicio % 7


    espacio = ''
    espacio = espacio.rjust(2,' ')

    print(meses[mes], dia_inicio)
    print('Mo','Tu','We','Th','Fr','Sa','Su')


    if mes == 9 or mes == 4 or mes == 6 or mes ==11:
        for i in range(31+dia_inicio):

            if i <= dia_inicio:
                print(espacio, end=' ')

            else:
                print("{:02d}".format(i-dia_inicio),end=' ')
                if(i + 1)%7 == 0:
                    print()
    else:
        print("El mes seleccionado no tiene 30 días")

calendario(dia_inicio=int,mes=int)