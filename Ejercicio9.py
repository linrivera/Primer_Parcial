#Practica 9
s = int(input('Ingrese la cantidad de Sierras: \n' ))
d = int(input('Ingrese la cantidad de Barrenos : \n' ))
cantidad = pow(75,s)
cant = pow(112,d)
print(" El total de peso de Barrenos es de: " +str(cantidad))
print(" El total de peso de Sierras es de: " +str(cant))
total= cantidad + cant
print(" El total del peso es de: " +str(total))