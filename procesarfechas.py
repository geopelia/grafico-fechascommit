import csv
import datetime 
import dateutil.parser
import matplotlib.pyplot as plt

# TODO list compresion
# TODO reglas para nombrar variables y metodos
# TODO para las horas llenar el dict con todas las horas de 0 a 23, inicializadas en 0
def leer_archivo():
    lista_fechas = []
    with open('fechasgit.txt','r') as archivotxt:
            #print('open file')
            #cant_lineas = 0
        for linea in archivotxt:
            fecha = dateutil.parser.parse(linea)
            lista_fechas.append(fecha)
                #cant_lineas = cant_lineas + 1
                #if (cant_lineas  > 5):
                #    break;
    archivotxt.close()
        #print('hay ' + str(len(lista_fechas)))
        #print(str(lista_fechas[0].timetuple()))
    return lista_fechas

def agrupar_horas(lista_fechas):
    cant_horas = {}
    for fecha in lista_fechas:
        hora = fecha.timetuple().tm_hour
        if (hora in cant_horas):
            cont = cant_horas[hora] 
            cant_horas[hora] = cont + 1
        else:
            cant_horas[hora] = 1
        #print(cant_horas)
        #validar_sumahoras(cant_horas)
    return cant_horas
                
def validar_sumahoras(dict_horas):
    acumulador = 0
    for valores in dict_horas.values():
        acumulador = acumulador + valores
    print('la suma de los valores del dict es ' + str(acumulador))    

def dibujar_diagrama(diccionario):
    valores_x = list(diccionario)
    valores_y = list(diccionario.values())
    plt.bar(valores_x, valores_y)
    plt.ylabel('Cant commits')
    plt.xlabel('Horas')
    plt.title('Commits en determinadas horas en un repositorio')
    plt.show()

fechas = leer_archivo()
print('cant registros ' + str(len(fechas)))
dict_horas = agrupar_horas(fechas)
dibujar_diagrama(dict_horas)
