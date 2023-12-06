#ENTRADA
veces=int(input("Cuantas veces desea iterar? "))
tasa=3/100

for i in range(veces):
    print("ITERACION #",i+1)
    Vn=int(input("Valor de inversion: "))
    periodos=int(input("Ingrese los meses: "))
    monto=Vn*(1+tasa)**periodos
    print("el valor a recibir es: ",monto,"$")
    

    








