#practica 8
a = float(input('Ingrese el monto a invertir: \n'))
b = float(input('Ingrese el interes anual: \n'))
c = int(input('Ingrese el numero de anios: \n'))
cap =  a * (pow ((1 + b),c))
print("El capital obtenido es de: " + str(cap))