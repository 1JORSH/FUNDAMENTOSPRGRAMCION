n1 = int(input("ingresa el numero: "))
n2 = int(input("ingrese el segundo numero: "))
distancia = n1 - n2
if distancia < 0:
    distancia = distancia * (-1)
    print("la distancia entre: ",n1," y: ",n2, " es de: ",distancia)
    