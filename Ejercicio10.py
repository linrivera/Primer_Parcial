#practica 10
m = int(input('Cuanta memoria RAM usadas se vendieron: \n'))
mnuevas = m * 20
musadas = ((m*20)*0.60)
print("El precio de las memorias nuevas es de: $20")
print("La cantidad de memorias usadas es de: " + str(mnuevas))
print("El total de memoria con descuento es de: " + str(musadas))
total = mnuevas - musadas
print("El total a pagar es de: " + str(total))