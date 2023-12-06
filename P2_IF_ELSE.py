#ENTRADA
nombre= input("Nombre: ")
inversion= int(input("Monto a invertir: "))
premium= False

#ALGORITMO

if premium: # premium == True
    #calcular modo premium
    
    tasa= 2.5 /100
    periodo= 24
    monto=inversion*(1+tasa)**periodo
    print("Ud. recibira: ",monto, "$") #SALIDA
else:
    #calcular modo normal
    tasa= 2 /100
    periodo= 18
    monto=inversion*(1+tasa)**periodo
    print("Ud. recibira: ",monto, "$") #SALIDA








