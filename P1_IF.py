#ENTRADA
nombre= input("Nombre: ")
empresa= input("Tiene ud. empresa? : ")

#ALGORITMO

impuestos=50

if empresa.lower()=="si":
    impuestos+=500 # al valor de la variable impuestos le aumentaremos 500

#SALIDA

print("Los impuestos a pagar son: ",impuestos, " $ ")


