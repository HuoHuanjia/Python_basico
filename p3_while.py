#ENTRADA
precio=1000
periodos= 3

i=1
print("ITERACION #",i)
tasa=int(input("Ingrese la tasa inflacionaria: ")) /100
Pfuturo = precio*(1+tasa)**periodos
print("El precio futuro del articulo sera: ",Pfuturo, " $") #SALIDAS

while tasa !=0:
    i=i+1 # i  va ir aumentando de 1 en 1 por cada bucle/ciclo /repeticion
    print("ITERACION #",i)
    tasa=int(input("Ingrese la tasa inflacionaria: ")) /100
    Pfuturo = precio*(1+tasa)**periodos
    print("El precio futuro del articulo sera: ",Pfuturo, " $") #SALIDAS
    








