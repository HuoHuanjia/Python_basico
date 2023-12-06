#from numpy import * # invoca todas las funciones
from numpy import around # solo invoca la funcion que redondea
#import numpy as np # se utiliza cuando vas a llamar a mas librerias

#PROB-EJEMPLO

#ENTRADAS
periodos= 30
tasa= 2.8 /100
Vfuturo = 3500000

#ALGORITMO

inversion= Vfuturo / (1+tasa*periodos)

#SALIDA

print("La inversion inicial fue :",around(inversion,2), "$") # redondeo con numpy
#print(round(2.5)) # NO ES RECOMENDABLE /  NUMPY


