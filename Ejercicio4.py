#ejercicio #4
contador = 0
suma = 0
hora = 0
promedio = 0

for hora in range(0, 7):
    hora =int(input("ingreso de hora: \n"))
    suma += hora
    promedio = suma/7

    if hora >= 0 and hora <=24:
        
        contador +=1

print("La suma es de: " +str(suma))
print("El promedio es de: " +str(promedio))
print("el numero de hora es de: " +str(contador))

input()